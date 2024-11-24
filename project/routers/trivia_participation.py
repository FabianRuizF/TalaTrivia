from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.trivia_participation import list_question_from_trivia
from schemas.trivia_question import TriviaQuestionRead, DummyResponse, TriviaQuestionListResponse
from database import database
from utils.exception import DatabaseError

router = APIRouter(prefix="/trivia_participation")

@router.post("/read/", response_model=TriviaQuestionListResponse)
def list_question_from_trivia_endpoint(trivia_question: TriviaQuestionRead, db: Session = Depends(database.get_db)):
    try:
        list_question = list_question_from_trivia(trivia_question=trivia_question, db=db)
        return list_question
    except DatabaseError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
