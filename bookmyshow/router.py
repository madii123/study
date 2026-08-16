from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import Crud
from database import get_db
from models import Theatre, User

user_router = APIRouter()
theatre_router = APIRouter()
book_router = APIRouter()

"""
users
"""


@user_router.post("/")
def create_user(user: User, db: Session = Depends(get_db)):
    user = Crud.create_user(db, user)
    if user:
        return {"id": user.id}
    return HTTPException(status_code=400, detail="unable to create a user")


@user_router.get("/")
def list_users(db: Session = Depends(get_db)):
    users = Crud.list_users(db)
    return users


@user_router.get("/paginated")
def list_users_paged(offset: int, limit: int, db: Session = Depends(get_db)):
    users = Crud.list_users_paged(db, offset, limit)
    return users


@user_router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = Crud.get_user(db, user_id)
    return user


"""
theatres
"""


@theatre_router.post("/")
def create_theatre(theatre: Theatre, db: Session = Depends(get_db)):
    theatre = Crud.create_theatre(db, theatre)
    return theatre


@theatre_router.get("/")
def list_theatres(db: Session = Depends(get_db)):
    theatres = Crud.list_theatres(db)
    return theatres


@theatre_router.get("/paginated")
def list_theatres_paged(offset: int, limit: int, db: Session = Depends(get_db)):
    theatres = Crud.list_theatres_paged(db, offset, limit)
    return theatres


@theatre_router.get("/screen/{theatre_id}")
def list_all_screens(theatre_id: int, db: Session = Depends(get_db)):
    theatres = Crud.list_all_seats(db, theatre_id)
    return theatres


@theatre_router.get("/seats/{screen_id}")
def list_all_seats(screen_id: int, db: Session = Depends(get_db)):
    theatres = Crud.list_all_seats(db, screen_id)
    return theatres


"""
bookings
"""


@book_router.get("/")
def get_bookings(user_id: int, db: Session = Depends(get_db)):
    bookings = Crud.get_bookings(db, user_id)
    return bookings


@book_router.post("/")
def book_seat(user_id: int, seat_id: int, db: Session = Depends(get_db)):
    bookings = Crud.book_seat(db, seat_id, user_id)
    return bookings
