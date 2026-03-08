from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(..., min_length=1, max_length=100)
    description: str | None = None
    completed: bool = False
    assigned_to: str | None = None


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    assigned_to: str | None = None
