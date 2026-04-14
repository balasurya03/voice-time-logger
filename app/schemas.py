from pydantic import BaseModel
from datetime import datetime


# 🔹 Base schema (shared fields)
class TimeLogBase(BaseModel):
    task: str
    project: str
    time_spent: str


# 🔹 Create schema (input)
class TimeLogCreate(TimeLogBase):
    pass


# 🔹 Response schema (output)
class TimeLogResponse(TimeLogBase):
    id: int
    created_at: datetime   # 🔥 added (important)

    class Config:
        from_attributes = True  # SQLAlchemy compatibility