from fastapi import APIRouter
from typing import List
from repository import TaskAdd, TaskRepository
from schemas import Task, TaskId

router = APIRouter(
    prefix="/tasks",
    tags=['Таски']
)

@router.post("",  response_model=TaskId)
async def add_task(task: TaskAdd) -> TaskId:
    task_id = await TaskRepository.add_one(task)
    return TaskId(task_id = task_id)

@router.get("", response_model=List[Task])
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.find_all() 
    return tasks
