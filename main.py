from typing import Dict, List
import uuid
import fastapi
import redis
import os
from redis.commands.json.path import Path
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query
from models import Film

app = fastapi.FastAPI()
r = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), password=os.getenv("REDIS_PW"),decode_responses=True, ssl=True)
schema = (
    TextField("$.name", as_name="name"), 
    TextField("$.release_date", as_name="release_date")
)
rs = r.ft("idx:films")
rs.create_index(
    schema,
    definition=IndexDefinition(
        prefix=["film:"], index_type=IndexType.JSON
    )
)


@app.get("/film/{id}")
def get_films(id: str) -> Film:
    return Film.model_validate_json(r.json().get(f"film:{id}"))

@app.post("/film")
def create_film(film: Film) -> str:
    id = str(uuid.uuid4())
    print(f"Store {id}")
    r.json().set(f"film:{id}", Path.root_path(), film.model_dump())
    return id