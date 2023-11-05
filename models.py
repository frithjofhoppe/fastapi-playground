from redis_om import HashModel

class Film(HashModel):
    name: str
    release_date: str