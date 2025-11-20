from sqlalchemy import text, DateTime
from app.models import Base
from sqlalchemy.orm import mapped_column, Mapped
from typing import Optional
from datetime import datetime


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        server_default=text('CURRENT_TIMESTAMP'),
        nullable=False
    )