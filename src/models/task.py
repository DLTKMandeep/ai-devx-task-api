from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4

class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    completed: bool = False
    assigned_to: Optional[str] = None

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    assigned_to: Optional[str] = None
