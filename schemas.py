from typing import Optional
from pydantic import BaseModel


class STaskAdd(BaseModel):
    """Scheme"""
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    """Scheme"""
    id: int

    class Config:
        """Не допускает ошибку Input should be a valid dictionary or instance"""
        from_attributes = True


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
