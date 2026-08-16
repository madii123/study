from fastapi import FastAPI

from database import engine
from router import book_router, theatre_router, user_router
from schemas import Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(user_router, prefix="/users")
app.include_router(theatre_router, prefix="/theatres")
app.include_router(book_router, prefix="/book")
