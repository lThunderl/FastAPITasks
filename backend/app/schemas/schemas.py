from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime

class TaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class Task(TaskAdd):
    id: int
    created_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)


class TaskId(BaseModel):
    ok: bool = True
    task_id: int