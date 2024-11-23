from sqlalchemy.exc import IntegrityError, ProgrammingError
from passlib.context import CryptContext
from database import database
from models.user import User
from schemas.user import UserCreate, UserResponse, UserDelete, UserListResponse
from sqlalchemy.orm import Session
from config.settings import Settings
from utils.exception import DatabaseError

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user: UserCreate, db: Session ):
    hashed_password = password_context.hash(user.password)
    db_user = User(email=user.email, password=hashed_password, name=user.name)
    try:
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



def delete_user(user: UserDelete, db: Session ):
    try:
        db_user = db.query(User).filter(User.email == user.email).first()
        if db_user is None:
            raise ValueError("User not found")
        db.delete(db_user)
        db.commit()
        return UserResponse.from_orm(db_user)
    except ProgrammingError as error:
        db.rollback()
        raise DatabaseError(f"Database error: {str(error)}")
    except Exception as error:
        db.rollback()
        raise ValueError(f"An unexpected error occurred: {str(error)}")


def list_all_user(db: Session) -> UserListResponse:
    try:
        db_user_list = db.query(User).all()
        if db_user_list is None:
            raise ValueError("There are no users")
        return UserListResponse(user_list = db_user_list)
    except ProgrammingError as error:
        db.rollback()
        raise DatabaseError(f"Database error: {str(error)}")
    except Exception as error:
        db.rollback()
        raise ValueError(f"An unexpected error occurred: {str(error)}")
