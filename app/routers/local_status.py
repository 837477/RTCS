from fastapi import APIRouter
from dependencies import Dependencies, Config
from controller.local_status import get_all_local_status


router = APIRouter(
    prefix="/api/v1/local"
)


@router.get("/status")
async def status():
    data = get_all_local_status(Dependencies.db)
    return data
