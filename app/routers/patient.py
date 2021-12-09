from fastapi import APIRouter, Request
from dependencies import Dependencies, Config
from controller.patient import get_patients, get_infected_persons
from controller import map_naming
from model.mongodb.logs import Logs


router = APIRouter(
    prefix="/api/v1/patients"
)


@router.get("/status")
async def status(request: Request):   
    data = get_patients(Dependencies.db)

    log = {
        "host": request.client.host,
        "api": request.url.path,
        "parameters": [None]
    }
    Logs(Dependencies.db).insert_log(log)
    return map_naming(Dependencies.db, data, "naming")


@router.get("/infected/status")
async def infected():
    data = get_infected_persons()
    return data
