from pydantic import BaseModel
from typing import Optional

class TaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class Task(TaskAdd):
    id: int


class TaskId(BaseModel):
    ok: bool = True
    task_id: int