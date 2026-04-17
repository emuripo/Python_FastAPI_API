from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter()


@router.get("")
async def list_tasks():
    return await TaskService.list_tasks()


@router.post("")
async def create_task(payload: TaskCreate):
    return await TaskService.create_task(
        payload.title,
        payload.description
    )


@router.get("/{task_id}")
async def get_task(task_id: str):
    task = await TaskService.get_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.patch("/{task_id}")
async def update_task(task_id: str, payload: TaskUpdate):
    task = await TaskService.update_task(
        task_id,
        payload.model_dump()
    )

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.delete("/{task_id}")
async def delete_task(task_id: str):
    task = await TaskService.delete_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}