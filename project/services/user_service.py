from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from database import database
from models.user import User
from schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session
from config.settings import Settings

settings = Settings()

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user: UserCreate, db: Session ):
    hashed_password = password_context.hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return UserOut.from_orm(db_user)
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already exists")
