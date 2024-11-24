from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.user import create_user, delete_user, list_all_user
from schemas.user import UserCreate, UserResponse, UserDelete, UserListResponse
from database import database
from utils.exception import DatabaseError

router = APIRouter(prefix="/user")

@router.post("/create/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(database.get_db)):
    try:
        new_user = create_user(user=user, db=db)
        return new_user
    except DatabaseError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{email}/", response_model=UserResponse)
def delete_user_endpoint(user: UserDelete, db: Session = Depends(database.get_db)):
    try:
        is_deleted = delete_user(user=user, db=db)
        return is_deleted
    except DatabaseError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list/", response_model=UserListResponse)
def list_endpoint(db: Session = Depends(database.get_db)):
    try:
        all_user = list_all_user(db=db)
        return all_user
    except DatabaseError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{email}")
def update_user_endpoint(email: str, db: Session = Depends(database.get_db)):
    # TODO: Implement user deletion logic here
    pass
