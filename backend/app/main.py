from fastapi import FastAPI
from app.api.router import router
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

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Tasks API"}