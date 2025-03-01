from pydantic import BaseModel
from typing import Optional

class JokeBase(BaseModel):
    category: str
    type: str
    joke: Optional[str] = None
    setup: Optional[str] = None
    delivery: Optional[str] = None
    nsfw: bool
    political: bool
    sexist: bool
    safe: bool
    lang: str

    class Config:
        orm_mode = True
