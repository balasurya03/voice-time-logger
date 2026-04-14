🎤 Voice-Based Time Logging Assistant

📌 Overview

The **Voice-Based Time Logging Assistant** is a FastAPI-based application that allows users to log their daily work using voice commands.
Instead of manually entering data, users can simply speak their work updates, and the system automatically converts them into structured time logs.

This project demonstrates how **AI-powered voice interaction** can simplify routine administrative tasks and improve productivity.

---

🚀 Features

* 🎤 Voice-based time logging
* 🧠 Speech-to-text using Whisper AI
* 🔍 Automatic extraction of task, project, and time
* 🗄️ Database storage using SQLAlchemy
* 📊 Analytics dashboard (logs & time tracking)
* 🔊 Audio feedback using Text-to-Speech (gTTS)
* 🌐 Simple UI with HTML, CSS, and JavaScript

---

🧱 Project Structure

```
VOICE/
│
├── app/
│   ├── main.py              # Entry point of FastAPI app
│   ├── database.py          # Database configuration
│   ├── models.py            # ORM models
│   ├── schemas.py           # Pydantic schemas
│   ├── utils.py             # Speech processing & parsing logic
│   ├── routes/
│   │   └── log_routes.py    # API endpoints
│   └── templates/
│       ├── index.html       # Home page
│       └── dashboard.html   # Dashboard page
│
├── static/
│   ├── script.js            # Frontend logic
│   └── style.css            # Styling
│
├── create_db.py             # Script to initialize database
├── requirements.txt         # Dependencies
├── converted.wav            # Sample audio file
└── timelogs.db              # SQLite database (auto-created)
```

---

⚙️ Tech Stack

* **Backend:** FastAPI
* **Database:** SQLite + SQLAlchemy
* **Frontend:** HTML, CSS, JavaScript (Jinja2 Templates)
* **Speech Recognition:** OpenAI Whisper
* **Audio Processing:** pydub
* **Text-to-Speech:** gTTS
* **Server:** Uvicorn

---

🔄 Application Workflow

1. User records voice input from the UI
2. Audio is sent to the FastAPI backend
3. Whisper model converts speech → text
4. Text is parsed to extract:

   * Task
   * Project
   * Time spent
5. Data is stored in the database
6. Dashboard displays logs and analytics
7. System generates audio response

---

🛠️ Installation & Setup

1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd VOICE
```

---

2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

3️⃣ Create Database

```bash
python create_db.py
```

---

4️⃣ Run the Application

```bash
python -m uvicorn app.main:app --reload
```

---

5️⃣ Open in Browser

```
http://127.0.0.1:8000
```

---

📡 API Endpoints

| Method | Endpoint          | Description               |
| ------ | ----------------- | ------------------------- |
| POST   | `/log-voice`      | Upload voice & create log |
| GET    | `/logs`           | Get all logs              |
| GET    | `/dashboard-data` | Get analytics data        |
| GET    | `/health`         | Health check              |

---

📊 Example Output

```json
{
  "task": "Worked on dashboard project",
  "project": "dashboard",
  "time_spent": "2 hours"
}
```

---

🚧 Challenges

* Extracting structured data from natural speech
* Handling different time formats (hours/minutes)
* Managing audio file processing efficiently

---

🌱 Future Improvements

* 🔥 NLP-based smart parsing
* 🌍 Multi-language support
* 📊 Advanced analytics dashboard
* 🔐 OAuth authentication (Google/GitHub)
* ☁️ Cloud deployment

---

👨‍💻 Author

**Bala Surya R**
Final Year B.Tech – AI & Data Science

---

## 📜 License

This project is for educational and demonstration purposes.
