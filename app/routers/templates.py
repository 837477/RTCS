from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from dependencies import Config


router = APIRouter()
templates = Jinja2Templates(directory="assets")


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,
            "kakao_key": Config.KAKAO_MAP_API_KEY
        }
    )
