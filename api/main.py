from fastapi import APIRouter
from api.routes import train
from api.routes import get

api_router = APIRouter()

api_router.include_router(train.router, prefix="/train", tags=["train"])
api_router.include_router(get.router, prefix="/get", tags=["get"])