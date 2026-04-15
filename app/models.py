from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class TimeLog(Base):
    __tablename__ = "timelogs"

    id = Column(Integer, primary_key=True, index=True)

    #  Task description
    task = Column(String(255), nullable=False)

    #  Project name
    project = Column(String(100), nullable=False, index=True)

    #  Time spent (e.g., "2 hours", "30 mins")
    time_spent = Column(String(50), nullable=False)

    #  Created timestamp
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True
    )

    def __repr__(self) -> str:
        return f"<TimeLog(task='{self.task}', project='{self.project}', time='{self.time_spent}')>"
