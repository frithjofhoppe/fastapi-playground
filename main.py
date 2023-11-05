from typing import List
import fastapi
from models import Film, FilmDto
from redis_om.model.model import NotFoundError

app = fastapi.FastAPI()

@app.get("/film/{id}")
def get_film(id) -> FilmDto:
    try:
        film = Film.get(pk=id)
        return FilmDto(name=film.name, release_date=film.release_date)
    except NotFoundError as error:
        raise fastapi.HTTPException(status_code=404, detail=f"Film with id {id} wasn't found")

@app.get("/films")
def get_films():
    films: List[FilmDto] = []
    for filmId in Film.all_pks():
        film = Film.get(pk=filmId)
        films.append(
            FilmDto(name=film.name, release_date=film.release_date)
        )
    return films

@app.post("/film")
def create_film(filmDto: FilmDto) -> str:
    film = Film(
        name=filmDto.name,
        release_date=filmDto.release_date
    )
    film.save()
    print(f"Store {film.pk}")
    return film.pk