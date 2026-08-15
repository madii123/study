from sqlalchemy import Column, Integer, String
from database import Base


# this inherits base,
# this class represents a database table
# equivalent to a CREATE TABLE users (...)
class User(Base):
    # this tells SQLAlchemy
    # Python Class(User) ---> DataBaseTable(users)
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # id INTEGER
    name = Column(String)  # name VARCHAR
    email = Column(String, unique=True, nullable=False)


# primary_key = True - uniquley identifies each row
# index=True -> Creates DB index for faster lookups
# unique=True, duplicte values not allowed
# nullable=False -> value is mandatory
