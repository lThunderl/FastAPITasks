from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router
import os
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("ENVIRONMENT") == "development":
        await delete_tables()
        print("База очищена")
        await create_tables()
        print("База запущена")
    else:
        await create_tables()
        print("Таблицы проверены/Созданы")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan, title="Tasks API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:3000',
        "http://127.0.0.1:3000"
    ],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks_router)

@app.get("/")
async def root():
    return {"message": "Tasks API"}