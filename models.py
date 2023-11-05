from pydantic import BaseModel
from redis_om import HashModel

class Film(HashModel):
    name: str
    release_date: str

class FilmDto(BaseModel):
    name: str
    release_date: str