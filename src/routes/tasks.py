from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from src.models.task import Task, TaskCreate
from src.services.task_service import task_service

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=Task)
async def create_task(task: TaskCreate):
    return task_service.create_task(task)

@router.get("/", response_model=List[Task])
async def list_tasks():
    return task_service.get_all_tasks()

@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: UUID):
    task = task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
async def delete_task(task_id: UUID):
    deleted = task_service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
