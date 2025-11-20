from app.database import new_session
from app.models import Tasks
from app.schemas import TaskAdd, Task
from sqlalchemy import insert, select

class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            stmt = insert(Tasks).values(**data.model_dump()).returning(Tasks.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one() 
        
    @classmethod
    async def find_all(cls) -> list[Task]:
        async with new_session() as session:
            query = select(Tasks)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [Task.model_validate(task_model) for task_model in task_models]
            return task_schemas