"""api main file."""

from fastapi import APIRouter

from api.endpoints import task_manager

router = APIRouter()

router.include_router(task_manager.router, prefix="/tasks", tags=["tasks"])
