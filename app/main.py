from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.routes import log_routes
from app.database import init_db


#  Create FastAPI app
app = FastAPI(
    title="Voice Time Logging Assistant",
    description="AI-powered voice logging with analytics dashboard",
    version="1.0.0"
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize database
@app.on_event("startup")
def on_startup():
    init_db()


# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")


#  Templates
templates = Jinja2Templates(directory="app/templates")


#  API routes
app.include_router(log_routes.router)


#  Home page
@app.get("/", tags=["UI"])
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


#  Dashboard page
@app.get("/dashboard", tags=["UI"])
def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


#  Health check
@app.get("/health", tags=["System"])
def health():
    return {"status": "ok"}
