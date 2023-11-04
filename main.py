from typing import Dict, List
import uuid
import fastapi

from models import Film

app = fastapi.FastAPI()

FILMS: Dict[str, Film] = dict()

@app.get("/films")
def get_films() -> List[Film]:
    return FILMS.values()

@app.post("/film")
def create_film(film: Film) -> Film:
    FILMS[str(uuid.uuid4())] = film
    return film

@app.get("/test")
def test() -> str:
    return "test"