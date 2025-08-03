from pydantic import BaseModel

class Advice(BaseModel):
    phrase: str