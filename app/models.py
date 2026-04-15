from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class TimeLog(Base):
    __tablename__ = "timelogs"

    id = Column(Integer, primary_key=True, index=True)

    # Task description
    task = Column(String, nullable=False)

    # Project name
    project = Column(String, nullable=False, index=True)

    # Time spent (stored as string for now)
    time_spent = Column(String, nullable=False)

    # NEW: timestamp (very important)
    created_at = Column(DateTime, default=datetime.utcnow)
