from pydantic import BaseModel

class Model(BaseModel):
    user_id: int
    model_link: str
    index_link: str

    class Config:
        orm_mode = True
        from_attributes = True