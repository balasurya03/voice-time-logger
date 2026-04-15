import os
import json
import re
from dotenv import load_dotenv
from pydub import AudioSegment
import whisper

# LangChain + LangGraph
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END


# ==============================
# LOAD ENV VARIABLES
# ==============================
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY not found in .env file")


# ==============================
#  LLM CONFIG
# ==============================
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    api_key=OPENAI_API_KEY
)


# ==============================
#  PROMPTS
# ==============================
intent_prompt = ChatPromptTemplate.from_template("""
Classify the user input.

Text: {input}

Is this a work/task log? Answer only "yes" or "no".
""")

extract_prompt = ChatPromptTemplate.from_template("""
Extract the following details from the text:

- task
- project
- time_spent

Text: {input}

Return ONLY JSON:
{
    "task": "...",
    "project": "...",
    "time_spent": "..."
}
""")


# ==============================
#  LOAD WHISPER MODEL
# ==============================
model = whisper.load_model("base")


# ==============================
#  AUDIO UTILS
# ==============================
def convert_to_wav(input_path: str, output_path: str) -> None:
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="wav")
    except Exception as e:
        raise RuntimeError(f"Audio conversion failed: {str(e)}")


def speech_to_text(file_path: str) -> str:
    try:
        result = model.transcribe(file_path, language="en")
        text = result.get("text", "").strip()

        if not text:
            return "Could not understand audio"

        return text

    except Exception:
        return "Could not understand audio"


# ==============================
# SAFE JSON PARSER
# ==============================
def safe_json_load(content: str) -> dict:
    try:
        return json.loads(content)
    except Exception:
        return {
            "task": content,
            "project": "General",
            "time_spent": "Not specified"
        }


# ==============================
#  AGENT FUNCTIONS
# ==============================
def detect_intent(text: str) -> bool:
    try:
        response = llm.invoke(intent_prompt.format(input=text))
        return "yes" in response.content.lower()
    except Exception:
        return True  # fallback


def extract_data(text: str) -> dict:
    try:
        response = llm.invoke(extract_prompt.format(input=text))
        return safe_json_load(response.content)
    except Exception:
        return {
            "task": text,
            "project": "General",
            "time_spent": "Not specified"
        }


# ==============================
#  LANGGRAPH NODES
# ==============================
def router_node(state: dict) -> dict:
    text = state["text"]

    if detect_intent(text):
        return {"next": "extract", "text": text}

    return {"next": "fallback", "text": text}


def extract_node(state: dict) -> dict:
    text = state["text"]
    parsed = extract_data(text)
    return {"parsed": parsed}


def fallback_node(state: dict) -> dict:
    text = state["text"]

    return {
        "parsed": {
            "task": text,
            "project": "General",
            "time_spent": "0"
        }
    }


# ==============================
#  BUILD AGENT GRAPH
# ==============================
graph = StateGraph(dict)

graph.add_node("router", router_node)
graph.add_node("extract", extract_node)
graph.add_node("fallback", fallback_node)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    lambda state: state["next"],
    {
        "extract": "extract",
        "fallback": "fallback"
    }
)

graph.add_edge("extract", END)
graph.add_edge("fallback", END)

# FINAL AGENT
app_graph = graph.compile()
