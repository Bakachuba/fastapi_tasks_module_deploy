from typing import Annotated, List

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId
from fastapi import Depends, APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    """
    -> STaskId аннотация типов для авто документирования в http://127.0.0.1:8000/docs#/
    Она создает получаемый пример на основе Схемы бд
    """
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
