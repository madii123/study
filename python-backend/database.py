from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# sqlite:/// means use SQLite.
# for SQLite, the database is a file, so we need to give the path to the file.
DATABASE_URL = "sqlite:///users.db"


# engine is the starting point for any SQLAlchemy application, it manages the connection pool and provides a source of database connections.
engine = create_engine(DATABASE_URL)

# sessionmaker is a factory for creating new Session objects, which are used to interact with the database.
session_local = sessionmaker(bind=engine)

# declarative_base() is a factory function that constructs a base class for declarative class definitions.
# It maintains a catalog of classes and tables relative to that base.
Base = declarative_base()


# The get_db function is a dependency that can be used in FastAPI routes to get a database session.
# for every request, it creates a new session, yields it to the route, and then closes it after the request is done.
# one request = one session, so that all the CRUD operations in that request use the same session.
def get_db():
    # session_local() creates a new Session object, which is used to interact with the database.
    db = session_local()
    try:
        # hands over the session to the route, so that it can be used to perform CRUD operations.
        yield db
    finally:
        # closes the session after the request is done, which releases the connection back to the connection pool.
        db.close()
