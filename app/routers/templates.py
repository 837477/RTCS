from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


router = APIRouter()
router.mount("/static", StaticFiles(directory="assets/static"), name="static")
templates = Jinja2Templates(directory="assets")


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
