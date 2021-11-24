"""
Current status of infected people (limited to the metropolitan area)
"""

from fastapi import APIRouter
from dependencies import Dependencies, Config
from controller.patient import get_patients, get_infected_persons


router = APIRouter(
    prefix="/api/v1/patients"
)


@router.get("/status")
async def status():
    data = get_patients(Dependencies.db)
    return data


@router.get("/infected/status")
async def infected():
    data = get_infected_persons()
    return data
