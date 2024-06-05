from fastapi import APIRouter, Depends
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from database.model import get_db
from schemas.voice import Voice
from core.download import download_wav
from core.upload import upload_model
from core.train import train_model
from core.cleaning import cleaning_directory
from crud.model import upsert_model

load_dotenv()

router = APIRouter()

@router.post('/')
async def train(voice: Voice, db: Session = Depends(get_db)):
    dataset_path = download_wav(voice)

    model_path, index_path = train_model(voice)

    index_file = f'{index_path}/added*.index'
    model_link, index_link = upload_model(voice.user_id, model_path, index_file)

    upsert_model(db, voice.user_id, model_link, index_link)

    cleaning_directory(dataset_path, model_path, index_path)

    return {"message": "Training finished."}




