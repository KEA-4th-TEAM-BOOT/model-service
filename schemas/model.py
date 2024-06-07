from pydantic import BaseModel

class Model(BaseModel):
    user_id: int
    model_link: str
    index_link: str