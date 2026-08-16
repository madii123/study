from sqlalchemy import select, update
from sqlalchemy.orm import Session

from models import Theatre as theatre
from models import User as model_user
from schemas import Booking, Screen, Seat, Theatre, User


class Crud:
    def create_user(db: Session, user: model_user):
        u = User(name=user.name, email=user.email)
        db.add(u)
        db.commit()
        db.refresh(u)
        return u

    def get_user(db: Session, id: int):
        # return db.query(User).filter(User.id == id).first() - old style
        stmt = select(User).where(User.id == id)
        return db.scalar(stmt)

    def list_users(db: Session):
        stmt = select(User)
        return db.scalars(stmt).all()

    def list_users_paged(db: Session, offset: int, limit: int):
        stmt = select(User).order_by(User.id.desc()).offset(offset).limit(limit)
        return db.scalars(stmt).all()

    def create_theatre(db: Session, th: theatre):
        t = Theatre(name=th.name)

        for scrn in th.screens:
            s = Screen(name=scrn.name)

            for stn in scrn.seats:
                st = Seat(name=stn.name)
                s.seats.append(st)
            t.screens.append(s)

        db.add(t)
        db.commit()
        db.refresh(t)
        return t

    def list_theatres(db: Session):
        stmt = select(Theatre)
        return db.scalars(stmt).all()

    def list_theatres_paged(db: Session, offset: int, limit: int):
        stmt = select(Theatre).order_by(Theatre.id.desc()).offset(offset).limit(limit)
        return db.scalars(stmt).all()

    def list_screens(db: Session, theatre_id: int):
        stmt = select(Screen).where(Screen.theatre_id == theatre_id)
        return db.scalars(stmt).all()

    def list_available_seats(db: Session, screen_id: int):
        stmt = select(Seat).where(Seat.screen_id == screen_id, Seat.available == True)
        return db.scalars(stmt).all()

    def list_all_seats(db: Session, screen_id: int):
        stmt = select(Seat).where(Seat.screen_id == screen_id)
        return db.scalars(stmt).all()

    def book_seat(db: Session, seat_id: int, user_id: int) -> Booking | None:
        stmt = (
            update(Seat)
            .where(Seat.id == seat_id, Seat.available.is_(True))
            .values(available=False)
        )
        result = db.execute(stmt)

        if result.rowcount == 0:
            db.rollback()
            return None

        booking = Booking(name=f"{user_id}_{seat_id}", user_id=user_id, seat_id=seat_id)
        db.add(booking)

        db.commit()
        db.refresh(booking)
        return booking

    def get_bookings(db: Session, user_id: int):
        stmt = select(Booking).filter(Booking.user_id == user_id)
        return db.scalars(stmt).all()
