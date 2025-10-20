from fastapi import APIRouter, Depends
from typing import Annotated
from repository import TaskAdd, TaskRepository
from schemas import Task, TaskId

router = APIRouter(
    prefix="/tasks",
    tags=['Таски']
)

@router.post("")
async def add_task(task: Annotated[TaskAdd, Depends()]) -> TaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.find_all() 
    return {"tasks": tasks}
