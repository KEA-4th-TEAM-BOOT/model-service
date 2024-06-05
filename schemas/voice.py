from pydantic import BaseModel

class Voice(BaseModel):
    user_id: int
    wav: str
