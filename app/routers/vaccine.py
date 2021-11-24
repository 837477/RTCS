from fastapi import APIRouter
from dependencies import Dependencies, Config
from controller.vaccine import get_vaccine_status


router = APIRouter(
    prefix="/api/v1/vaccine"
)


@router.get("/status")
async def status():
    data = get_vaccine_status(Dependencies.db)
    return data
