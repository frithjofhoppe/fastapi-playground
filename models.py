from pydantic import BaseModel


class Film(BaseModel):
    name: str
    release_date: str