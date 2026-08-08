import time

from fastapi import FastAPI
from database import engine, Base
from middleware import setup_middleware
from routers.user import router as user_router
from routers.dummy import router as dummy_router



# delete the tables in the database
# start from scratch, so that we can test the CRUD operations
# uncomment the below line to delete the tables in the database
# Base.metadata.drop_all(bind=engine) 

"""
create the tables in the database
take every class inheriting from Base and creates its table if it does not exist

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

"""
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.title = "User Management API"
app.state.start_time = time.time()

setup_middleware(app)

app.include_router(user_router, prefix="/users")
app.include_router(dummy_router, prefix="/dummy")


