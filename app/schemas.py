from pydantic import BaseModel, Field
from datetime import datetime


# ==============================
#  Base Schema
# ==============================
class TimeLogBase(BaseModel):
    task: str = Field(..., example="Developed API endpoints")
    project: str = Field(..., example="AI Logger")
    time_spent: str = Field(..., example="2 hours")


# ==============================
#  Create Schema (Input)
# ==============================
class TimeLogCreate(TimeLogBase):
    pass


# ==============================
#  Response Schema (Output)
# ==============================
class TimeLogResponse(TimeLogBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
