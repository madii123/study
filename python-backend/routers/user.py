from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import get_db


# Best practice:
# - keep router definition separate from the main FastAPI app instance
# - do not import app from main.py into router modules
# - export the router object and let main.py include it with app.include_router(...)
# This avoids circular imports and makes routers reusable and easier to test.
router = APIRouter()

"""
Depends(get_db)
FastAPI calls it by default
for each request, it creates a new session, yields it to the route, and then closes it after the request is done.
one request = one session, so that all the CRUD operations in that request use the same session
"""


@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        return HTTPException(status_code=404, detail="user not found")
    return user


@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return crud.list_users(db)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)
