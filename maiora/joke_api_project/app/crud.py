from sqlalchemy.orm import Session
from app import models, schemas

def create_joke(db: Session, joke: schemas.JokeBase):
    db_joke = models.Joke(
        category=joke.category,
        type=joke.type,
        joke=joke.joke,
        setup=joke.setup,
        delivery=joke.delivery,
        nsfw=joke.nsfw,
        political=joke.political,
        sexist=joke.sexist,
        safe=joke.safe,
        lang=joke.lang
    )
    db.add(db_joke)
    db.commit()
    db.refresh(db_joke)
    return db_joke
