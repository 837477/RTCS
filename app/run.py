from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from model.mongodb import DataManager, get_session


# Application Settings
app = FastAPI(
    docs_url="/documentation"
)
app.add_middleware(BaseHTTPMiddleware, dispatch=get_session)
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.on_event("startup")
async def startup():
    """Server Initialization"""
    # DB Init
    DataManager().init_model()


@app.on_event("shutdown")
async def shutdown():
    """Server Clean-Up"""
    pass


# Routers Settings
from routers import templates
from routers import local_status
from routers import patient
from routers import vaccine
app.include_router(templates.router)
app.include_router(local_status.router)
app.include_router(patient.router)
app.include_router(vaccine.router)


"""
실시간 감염자 상황 (수도권 한정) - OK
특정 지역의 실시간 감염자 확인 - OK
국내 코로나 백신 현황
코로나 확진자 발생 동향 - OK
"""