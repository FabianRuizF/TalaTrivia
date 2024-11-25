from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.trivia import create_trivia
from schemas.trivia import TriviaCreate, TriviaResponse
from database import database
from utils.exception import DatabaseError

router = APIRouter(prefix="/trivia")

@router.post("/create/", response_model=TriviaResponse)
def create_trivia_endpoint(trivia: TriviaCreate, db: Session = Depends(database.get_db)):
    try:
        new_trivia = create_trivia(trivia=trivia, db=db)
        return new_trivia
    except DatabaseError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
