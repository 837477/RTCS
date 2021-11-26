from fastapi import APIRouter, Request
from pydantic import BaseModel

from dependencies import Dependencies, Config
from controller.local_status import get_all_local_status
from controller import map_naming


router = APIRouter(
    prefix="/api/v1/local"
)


class RegionValidation(BaseModel):
	location: str


@router.get("/status")
async def status():
    data = get_all_local_status(Dependencies.db)
    return map_naming(Dependencies.db, data, "region")


@router.post("/region/")
async def region(data: RegionValidation):
    location = data.location
    target_1 = location.split(' ')[1] + " 전체"
    target_2 = location.split(' ')[1] + " 추가"
    value = map_naming(
        Dependencies.db,
        get_all_local_status(Dependencies.db),
        "region"
    )
    if target_1 not in value:
        return None

    return {
        target_1: value[target_1],
        target_2: value[target_2],
    }
