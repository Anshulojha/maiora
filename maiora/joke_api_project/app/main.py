from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine
from app.utils import fetch_jokes

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/fetch-jokes")
def fetch_and_store_jokes(db: Session = SessionLocal()):
    """
    Fetches jokes from JokeAPI, processes them, and stores them in the database.
    """
    jokes_data = fetch_jokes()
    if not jokes_data:
        raise HTTPException(status_code=500, detail="Failed to fetch jokes")

    for joke in jokes_data:
        crud.create_joke(db, joke)

    return {"message": "Jokes fetched and stored successfully."}
