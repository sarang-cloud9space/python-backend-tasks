
from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import engine
from routers.auth_routes import router as auth_router
from routers.task_routes import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run startup and shutdown logic here.
    yield
    await engine.dispose()


app = FastAPI(
    title="Tasks API",
    description="Tasks API with PostgreSQL and JWT authentication",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(task_router)


@app.get("/")
async def root():
    return {"message": "Tasks API is running"}
