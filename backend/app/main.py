from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.app.database.database import create_tables, delete_tables
from backend.app.router import router as tasks_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Tasks API", version="1.0.0")

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