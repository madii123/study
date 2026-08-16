from pydantic import BaseModel


class Seat(BaseModel):
    name: str


class Screen(BaseModel):
    name: str
    seats: list[Seat]


class Theatre(BaseModel):
    name: str
    screens: list[Screen]


class User(BaseModel):
    name: str
    email: str


class Booking(BaseModel):
    name: str
    usr_id: int
    seat_id: int
