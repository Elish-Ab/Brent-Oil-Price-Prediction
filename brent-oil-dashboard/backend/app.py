from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Brent Oil API is Running"}

@app.get("/prices/", response_model=list[schemas.Price])
def get_prices(db: Session = Depends(get_db)):
    return crud.get_prices(db)
