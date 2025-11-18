from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional
from sqlalchemy import DateTime
import datetime
from app.utils import Settings

settings = Settings()

DATABASE_URL = f"postgresql+asyncpg://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow=20
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class TasksTable(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, 
        default=datetime.datetime.now
    )

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)