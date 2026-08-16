from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)


class Seat(Base):
    __tablename__ = "seats"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    available: Mapped[bool] = mapped_column(default=True)

    screen_id: Mapped[int] = mapped_column(ForeignKey("screens.id"))
    screen: Mapped["Screen"] = relationship(back_populates="seats")


class Screen(Base):
    __tablename__ = "screens"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()

    seats: Mapped[list["Seat"]] = relationship(back_populates="screen")

    theatre_id: Mapped[int] = mapped_column(ForeignKey("theatres.id"))
    theatre: Mapped["Theatre"] = relationship(back_populates="screens")


class Theatre(Base):
    __tablename__ = "theatres"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()

    screens: Mapped[list["Screen"]] = relationship(back_populates="theatre")


class Booking(Base):
    __tablename__ = "bookings"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    seat_id: Mapped[int] = mapped_column(ForeignKey("seats.id"))
