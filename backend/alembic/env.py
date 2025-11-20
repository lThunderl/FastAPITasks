# alembic/env.py
import os
from dotenv import load_dotenv
from pathlib import Path
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from sqlalchemy.engine import Connection
from alembic import context

# 🔽 Загружаем .env
dotenv_path = Path(__file__).parent.parent / ".env.local"
load_dotenv(dotenv_path)

# 🔽 Импортируем модели
from app.models import Base, Tasks

# 🔽 Импортируем settings
from app.core import Settings

settings = Settings()

config = context.config

# Настройка логов
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Устанавливаем URL для Alembic
config.set_main_option("sqlalchemy.url", settings.SYNC_DATABASE_URL)

# Метаданные
target_metadata = Base.metadata


def run_migrations_offline():
    """Offline mode"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Online mode — синхронное подключение"""
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
