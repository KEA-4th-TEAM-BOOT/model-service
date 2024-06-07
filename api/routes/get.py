from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.recommend import get_db
from crud.model import get_model
from schemas.model import Model

router = APIRouter()

@router.get('/{user_id}')
async def get(user_id: int, db: Session = Depends(get_db)) -> Model:
    model = get_model(db, user_id)
    return model






