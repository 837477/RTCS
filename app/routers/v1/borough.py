from fastapi import APIRouter
from dependencies import Config
from controller.v1.borough import get_data, mapping_location

router = APIRouter(
    prefix="/api/v1/borough"
)


@router.get("/all")
async def all():
    data = get_data(Config.DATA_SECRET_KEY, 'json')
    result = {}
    for key, value in data['infected'].items():
        result[mapping_location(key)] = value
    
    return result
    

@router.get("/{location}")
async def all(location: str):
    data = get_data(Config.DATA_SECRET_KEY, 'json')
    result = {}
    for key, value in data['infected'].items():
        name = mapping_location(key)
        if location in name:
            result[name] = value
    
    return result
