from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy import func
import shutil
import os
import uuid
import base64
import re

from app.database import SessionLocal
from app.models import TimeLog
from app.schemas import TimeLogResponse
from app.utils import speech_to_text, app_graph   
from gtts import gTTS

router = APIRouter()


# ==============================
# DB Dependency
# ==============================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==============================
# DASHBOARD API
# ==============================
@router.get("/dashboard-data")
def dashboard(db: Session = Depends(get_db)):
    logs = db.query(TimeLog).all()

    project_counts = (
        db.query(TimeLog.project, func.count(TimeLog.id))
        .group_by(TimeLog.project)
        .all()
    )

    project_time = {}

    for log in logs:
        time = log.time_spent.lower()

        hours = re.search(r'(\d+)\s*(hour|hr)', time)
        minutes = re.search(r'(\d+)\s*(minute|min)', time)

        total_time = 0
        if hours:
            total_time += int(hours.group(1))
        if minutes:
            total_time += int(minutes.group(1)) / 60

        project_time[log.project] = project_time.get(log.project, 0) + total_time

    return {
        "total_logs": len(logs),
        "project_counts": dict(project_counts),
        "project_time": project_time
    }


# ==============================
# VOICE LOG API
# ==============================
@router.post("/log-voice")
async def log_voice(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = None
    audio_path = None

    try:
        #  Step 1: Save file
        unique_id = str(uuid.uuid4())
        file_path = f"temp_{unique_id}.webm"
        audio_path = f"response_{unique_id}.mp3"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Step 2: Speech → Text
        text = speech_to_text(file_path)

        if not text.strip():
            text = "Could not understand audio"

        print("🎤 Recognized:", text)

        # Step 3: LangGraph Agent (REPLACED parse_text 🔥)
        result = app_graph.invoke({"text": text})
        parsed = result["parsed"]

        # Step 4: Save to DB
        log = TimeLog(**parsed)
        db.add(log)
        db.commit()
        db.refresh(log)

        # Step 5: Generate audio
        tts = gTTS(text=text, lang="en")
        tts.save(audio_path)

        with open(audio_path, "rb") as f:
            audio_base64 = base64.b64encode(f.read()).decode("utf-8")

        return JSONResponse({
            "status": "success",
            "text": text,
            "project": parsed.get("project"),
            "time_spent": parsed.get("time_spent"),
            "audio": audio_base64
        })

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Voice processing failed: {str(e)}"
        )

    finally:
        #  Cleanup
        if file_path and os.path.exists(file_path):
            os.remove(file_path)

        if audio_path and os.path.exists(audio_path):
            os.remove(audio_path)


# ==============================
# GET ALL LOGS
# ==============================
@router.get("/logs", response_model=list[TimeLogResponse])
def get_logs(db: Session = Depends(get_db)):
    return db.query(TimeLog).all()
