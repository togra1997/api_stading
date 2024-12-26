"""api main file."""

from api.endpoints import (
    effort_assignment,
    task_manager,
    work_time_manager,
)
from fastapi import APIRouter

router = APIRouter()

router.include_router(task_manager.router, prefix="/tasks", tags=["tasks"])
router.include_router(work_time_manager.router, prefix="/work-time", tags=["work-time"])

router.include_router(
    effort_assignment.router,
    prefix="/effort-assignment",
    tags=["effort-assignment"],
)
