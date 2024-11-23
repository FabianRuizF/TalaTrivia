from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.user_service import create_user
from schemas.user import UserResponse, UserCreate
from database import database

router = APIRouter(prefix="/users")

@router.post("/create/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(database.get_db)):
    try:
        new_user = create_user(db=db, user=user)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{email}", response_model=UserResponse)
def update_user(email: str, db: Session = Depends(database.get_db)):
    # TODO: Implement user update logic here
    pass

@router.delete("/{email}")
def delete_user(email: str, db: Session = Depends(database.get_db)):
    # TODO: Implement user deletion logic here
    pass
