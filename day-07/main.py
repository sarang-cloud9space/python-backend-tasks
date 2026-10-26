
from fastapi import FastAPI
from routers.tasks import router as tasks_router

app = FastAPI(title="Tasks API")

app.include_router(tasks_router)


@app.get("/")
def home():
    return {"message": "Welcome to the Tasks API"}
