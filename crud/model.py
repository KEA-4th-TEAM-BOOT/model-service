from sqlalchemy.orm import Session
from models.model import Model

def upsert_model(db: Session, user_id: int, model_link: str, index_link: str):
    db_model = db.query(Model).filter(
        Model.user_id == user_id
    ).first()

    if db_model:
        db_model.model_link = model_link
        db_model.index_link = index_link
    else:
        db_model = Model(
            user_id=user_id,
            model_link=model_link,
            index_link=index_link
        )
        db.add(db_model)

    db.commit()
    db.refresh(db_model)
