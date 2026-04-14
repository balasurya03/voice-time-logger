from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware

from app.routes import log_routes
from app.database import init_db


# 🔥 Create FastAPI app
app = FastAPI(
    title="Voice Time Logging Assistant",
    description="AI-powered voice logging with analytics dashboard",
    version="1.0.0"
)


# 🔥 CORS (only once)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 🔥 Initialize DB
init_db()


# 🔥 Static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# 🔥 Templates
templates = Jinja2Templates(directory="app/templates")


# 🔥 API routes
app.include_router(log_routes.router)


# 🏠 Home page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# 📊 Dashboard page
@app.get("/dashboard")
def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


# ❤️ Health check (VERY USEFUL)
@app.get("/health")
def health():
    return {"status": "ok"}