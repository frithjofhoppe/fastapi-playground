from typing import List
import fastapi
from models import Film

app = fastapi.FastAPI()

@app.get("/film/{id}")
def get_film(id: str) -> Film:
    return Film.get(pk=id)

def get_films() -> any:
    return Film.all_pks()

@app.post("/film")
def create_film(film: Film) -> str:
    filmObject = film.save()
    print(f"Store {filmObject.pk}")
    return filmObject.pk