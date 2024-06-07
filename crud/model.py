from sqlalchemy.orm import Session
from models.model import Model as ModelModel
from schemas.model import Model as ModelSchema

def upsert_model(db: Session, user_id: int, model_link: str, index_link: str):
    db_model = db.query(ModelModel).filter(
        ModelModel.user_id == user_id
    ).first()

    if db_model:
        db_model.model_link = model_link
        db_model.index_link = index_link
    else:
        db_model = ModelModel(
            user_id=user_id,
            model_link=model_link,
            index_link=index_link
        )
        db.add(db_model)

    db.commit()
    db.refresh(db_model)

def get_model(db: Session, user_id: int) -> ModelSchema:
    model = db.query(ModelModel).filter(ModelModel.user_id == user_id).first()
    if model:
        return ModelSchema.from_orm(model)
    return None
