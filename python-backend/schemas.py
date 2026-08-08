from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(UserCreate):
    id: int
    class Config:
        from_attributes = True

"""
from_attributes:
    This is a configuration option in Pydantic that allows you to create a model instance from an object with attributes, rather than from a dictionary.
     When set to True, Pydantic will read values directly from the attributes of the object passed to the model's constructor.
db_user = User(id=1, name="Madhu", email="test@gmail.com")
response = UserResponse.model_validate(db_user)

fast API automatically converts:
@app.get("/users/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    db_user = db.get(User, id)
    return db_user

"""