from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.trivia_participation import list_question_from_trivia
from schemas.trivia_participation import TriviaParticipationRead, TriviaQuestionListResponse
from database import database
from utils.exception import DatabaseError

router = APIRouter(prefix="/trivia_participation")

@router.post("/read/", response_model=TriviaQuestionListResponse)
def list_question_from_trivia_endpoint(trivia_participation: TriviaParticipationRead, db: Session = Depends(database.get_db)):
    try:
        question_list = list_question_from_trivia(trivia_participation=trivia_participation, db=db)
        return question_list
    except DatabaseError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
