from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL)
session_maker = sessionmaker(bind=engine)


def get_db():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()
