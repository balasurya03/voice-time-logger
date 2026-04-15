from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# ==============================
#  DATABASE CONFIG
# ==============================
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./timelogs.db")


# ==============================
# ENGINE
# ==============================
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # needed for SQLite
    pool_pre_ping=True  # ✅ checks DB connection health
)


# ==============================
#  SESSION FACTORY
# ==============================
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ==============================
# BASE MODEL
# ==============================
Base = declarative_base()


# ==============================
# INIT DB
# ==============================
def init_db() -> None:
    from app import models  # ensure models are loaded
    Base.metadata.create_all(bind=engine)
