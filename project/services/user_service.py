from sqlalchemy.exc import IntegrityError, ProgrammingError
from passlib.context import CryptContext
from database import database
from models.user import User
from schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session
from config.settings import Settings
from utils.exception import DatabaseError

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user: UserCreate, db: Session ):
    hashed_password = password_context.hash(user.password)
    db_user = User(email=user.email, password=hashed_password, name=user.name)
    try:
        print(db_user)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return UserResponse.from_orm(db_user)
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already exists")
    except ProgrammingError as error:
        db.rollback()
        raise DatabaseError(f"Database error: {str(error)}")
    except Exception as error:
        db.rollback()
        raise ValueError(f"An unexpected error occurred: {str(error)}")
