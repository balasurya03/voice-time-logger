# 🎤 Voice Time Logging Assistant (AI Agent)

An **AI-powered voice logging system** that converts speech into structured work logs using a **LangGraph-based agentic workflow with tool calling**.

This project demonstrates a **real-world AI agent pipeline** combining speech processing, LLM reasoning, and action execution.

---

## 🚀 Features

* 🎙️ Voice-to-text using Whisper
* 🧠 LangGraph-based AI agent (decision + routing)
* 🔧 Tool calling for action execution
* 📊 Automatic task logging & analytics dashboard
* 🔊 Audio response generation (Text-to-Speech)
* 💾 Structured storage using SQLAlchemy
* 🔐 Secure API key handling using `.env`

---

## 🧠 AI Agent Workflow

```text
User Voice Input
      ↓
Speech-to-Text (Whisper)
      ↓
LangGraph Agent
   ├── Intent Detection
   ├── Conditional Routing
   ├── Data Extraction (LLM)
   └── Fallback Handling
      ↓
Tool Execution (log_tool)
      ↓
Database Storage
      ↓
Audio Response (gTTS)
      ↓
API Response (FastAPI)
```

---

## 🔧 Tool Calling (Agent Capabilities)

This system follows a **tool-based agentic architecture**, where the AI agent not only understands input but also **executes actions using tools**.

### 🧠 How It Works

1. User provides voice input
2. Agent processes and extracts structured data
3. Agent invokes a tool to perform an action (e.g., save log)

---

### ⚙️ Example Tool

```python
def log_tool(data: dict, db):
    log = TimeLog(**data)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
```

---

### 🔄 Tool-Based Flow

```text
User Input → Agent → Extract Data → Tool Call → Database → Response
```

---

### 🎯 Benefits

* Enables **action-driven AI systems**
* Improves **modularity and scalability**
* Aligns with modern **LLM agent architectures**
* Moves beyond chatbots → **real AI assistants**

---

### 🎤 Interview Explanation

> “I implemented a LangGraph-based AI agent with tool-calling capabilities, where the system performs structured extraction and executes actions like database operations through tools.”

---

## 🏗️ System Architecture

```text
                🎙️ User Voice Input
                         │
                         ▼
              🧠 Speech-to-Text (Whisper)
                         │
                         ▼
                🤖 LangGraph Agent
              ┌──────────┼──────────┐
              ▼                     ▼
     🔍 Intent Detection     🔄 Fallback Logic
              │
              ▼
       🧩 Data Extraction (LLM)
              │
              ▼
        🔧 Tool Execution Layer
              │
              ▼
        💾 Database (SQLAlchemy)
              │
              ▼
       🔊 Audio Response (gTTS)
              │
              ▼
              📤 API Response (FastAPI)
```

---

## 🏗️ Tech Stack

* **Backend**: FastAPI
* **AI/LLM**: LangChain + LangGraph
* **Speech Recognition**: Whisper
* **Database**: SQLite + SQLAlchemy
* **Text-to-Speech**: gTTS
* **Frontend**: Jinja2 Templates

---

## 📂 Project Structure

```text
app/
 ├── routes/        # API endpoints
 ├── utils.py       # AI agent + speech processing
 ├── models.py      # Database models
 ├── schemas.py     # Pydantic schemas
 ├── database.py    # DB configuration
 └── main.py        # Entry point

static/
templates/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/voice-time-logger.git
cd voice-time-logger
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Application

```bash
uvicorn app.main:app --reload
```

---

## 📡 API Endpoints

| Endpoint          | Method | Description               |
| ----------------- | ------ | ------------------------- |
| `/log-voice`      | POST   | Upload voice & create log |
| `/dashboard-data` | GET    | Get analytics data        |
| `/logs`           | GET    | Fetch all logs            |
| `/health`         | GET    | Health check              |

---

## 📊 Example

### 🎙️ Input:

> “Worked on backend API for 2 hours in AI project”

### 📤 Output:

```json
{
  "task": "Worked on backend API",
  "project": "AI project",
  "time_spent": "2 hours"
}
```

---

## 🔐 Security

* API keys managed using environment variables
* `.env` excluded from version control
* No hardcoded secrets

---

## 🎯 Key Highlights

* Built a **LangGraph-based agentic system**
* Implemented **tool-calling architecture**
* Designed a **real-world AI workflow pipeline**
* Integrated **speech + LLM + backend system**
* Followed **clean backend practices**

---

## 🚀 Future Improvements

* Add memory (conversation history)
* Multi-tool agent system
* Upgrade to GPT-4o
* Docker deployment

---

## 🎤 Interview Summary

> “I built an end-to-end AI agent system using LangGraph that processes voice input, performs intent detection, extracts structured data, and executes actions using tool-calling to store results in a database.”

---

## 👨‍💻 Author

**Bala Surya R**
AI & Data Science Engineer (2025 Graduate)

---
