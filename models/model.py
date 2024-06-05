from sqlalchemy import Column, Integer, String, DateTime, func
from database.model import Base

class Model(Base):
    __tablename__ = 'models'

    model_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    model_link = Column(String, nullable=False)
    index_link = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())