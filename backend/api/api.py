"""api main file."""

from api.endpoints import task_manager, work_time_manager
from fastapi import APIRouter

router = APIRouter()

router.include_router(task_manager.router, prefix="/tasks", tags=["tasks"])
router.include_router(work_time_manager.router, prefix="/work-time", tags=["work-time"])
