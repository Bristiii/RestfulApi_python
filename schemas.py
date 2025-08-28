# schemas.py
from pydantic import BaseModel
from typing import Optional

# Schema for creating a task (input)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Schema for updating a task (input)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Schema for reading a task (output)
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    class Config:
        orm_mode = True # Helps Pydantic work with SQLAlchemy models