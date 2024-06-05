from fastapi import APIRouter
from api.routes import train

api_router = APIRouter()

api_router.include_router(train.router, prefix="/train", tags=["train"])