from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    playtime: int
    genre: list[str]

class MovieUpdate(BaseModel):
    title: str
    playtime: int
    genre: list[str]

class MovieResponse(BaseModel):
    id : int
    title: str
    playtime: int
    genre: list[str]