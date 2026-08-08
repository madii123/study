from sqlalchemy.orm import Session
import models, schemas

# fast api already created one session using Depends(get_db)
# Every CRUD operation uses same session during that request
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)

    #it tells SQLalchemy that keept track of this object, I intend to save it.
    db.add(db_user)

    #this executes SQL
    #permanently saved now
    db.commit()

    # the db_user.id is still none, it reloads the row
    # so that the user.id has some value
    # auto-incremented primary key
    db.refresh(db_user)

    return db_user

def get_user(db: Session, user_id: int):
    # The query does not go to the database until you call .first() or .all() or .one() etc.[any terminal operation]
    return db.query(models.User).filter(models.User.id == user_id).first()

def list_users(db: Session):
    # The query does not go to the database until you call .first() or .all() or .one() etc.[any terminal operation]
    return db.query(models.User).all()

def delete_user(db: Session, user_id: int):
    # The query does not go to the database until you call .first() or .all() or .one() etc.[any terminal operation]
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()