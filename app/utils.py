import re
import os
from pydub import AudioSegment
import whisper
import speech_recognition as sr

# Load Whisper model once
model = whisper.load_model("base")


# Convert any audio → WAV
def convert_to_wav(input_path, output_path):
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="wav")
    except Exception as e:
        print("Conversion Error:", str(e))
        raise e


# Speech to Text (Whisper + fallback)
def speech_to_text(file_path):
    try:
        result = model.transcribe(
            file_path,
            language="en"   #  FORCE ENGLISH
        )

        text = result["text"]
        print("WHISPER TEXT:", text)

        return text.strip()

    except Exception as e:
        print("Whisper Error:", str(e))
        return "Could not understand audio"


# Parse extracted text
def parse_text(text):
    text_lower = text.lower()

    # Improved regex (hours + minutes)
    time_match = re.search(r'(\d+)\s*(hour|hours|hr|hrs|minute|minutes|min)', text_lower)
    time_spent = time_match.group() if time_match else "Not specified"

    project_match = re.search(r'project\s+(\w+)', text_lower)
    project = project_match.group(1) if project_match else "General"

    return {
        "task": text,
        "project": project,
        "time_spent": time_spent
    }
