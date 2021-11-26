from fastapi import APIRouter
from dependencies import Dependencies, Config
from controller.patient import get_patients, get_infected_persons
from controller import map_naming


router = APIRouter(
    prefix="/api/v1/patients"
)


@router.get("/status")
async def status():
    data = get_patients(Dependencies.db)
    return map_naming(Dependencies.db, data, "naming")


@router.get("/infected/status")
async def infected():
    data = get_infected_persons()
    return data
