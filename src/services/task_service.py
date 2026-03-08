from typing import List, Optional
from uuid import UUID
from src.models.task import Task, TaskCreate, TaskUpdate

class TaskService:
    def __init__(self):
        self.tasks = {}

    def create_task(self, task_data: TaskCreate) -> Task:
        task = Task(**task_data.model_dump())
        self.tasks[task.id] = task
        return task

    def get_all_tasks(self) -> List[Task]:
        return list(self.tasks.values())

    def get_task(self, task_id: UUID) -> Optional[Task]:
        return self.tasks.get(task_id)

    def delete_task(self, task_id: UUID) -> bool:
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

task_service = TaskService()
