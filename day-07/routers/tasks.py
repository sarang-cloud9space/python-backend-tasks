
from fastapi import APIRouter, Depends, HTTPException
from schemas import TaskCreate,TaskRead, TaskUpdate


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


def pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


# Temporary in-memory storage
tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build a Tasks API", "completed": False},
]



@router.get("/", response_model=list[TaskRead])
def get_tasks(paging: dict = Depends(pagination)):
    skip = paging["skip"]
    limit = paging["limit"]

    return tasks[skip : skip + limit]





@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@router.post("/", response_model=TaskRead, status_code=201)
def create_task(task_data: TaskCreate):
    new_task = {
        "id": max(task["id"] for task in tasks) + 1,
        **task_data.model_dump()
    }

    tasks.append(new_task)
    return new_task


@router.patch("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task_data: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            update_data = task_data.model_dump(exclude_unset=True)
            task.update(update_data)
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
