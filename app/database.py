from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ SQLite Database URL
DATABASE_URL = "sqlite:///./timelogs.db"

# ✅ Create Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # needed for SQLite
)

# ✅ Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ✅ Base class for models
Base = declarative_base()


# 🔥 OPTIONAL (but recommended)
# Call this once when app starts to create tables automatically
def init_db():
    from app import models  # import all models here
    Base.metadata.create_all(bind=engine)