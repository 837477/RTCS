from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request
from model.mongodb import DataManager, get_session


# Application Settings
app = FastAPI(
    docs_url="/documentation"
)
app.add_middleware(BaseHTTPMiddleware, dispatch=get_session)

@app.on_event("startup")
async def startup():
    """Server Initialization"""
    print("Server Start ...")

    # DB Init
    DataManager().init_model()

    

@app.on_event("shutdown")
async def shutdown():
    """Server Clean-Up"""
    print("Server Shutdown ...")


# Routers Settings
from routers import templates
from routers.v1 import borough
app.include_router(templates.router)
app.include_router(borough.router)
