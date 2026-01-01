from pydantic import BaseModel

class MovieSearchParams(BaseModel):
	title: str | None = None
	genre: str | None = None

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