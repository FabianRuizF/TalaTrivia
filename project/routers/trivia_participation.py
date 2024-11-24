from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.trivia_participation import list_question_from_trivia, answer_trivia
from schemas.trivia_participation import TriviaParticipationRead, TriviaParticipationAnswer, TriviaQuestionListResponse, TriviaParticipationScoreResponse
from database import database
from utils.exception import DatabaseError

router = APIRouter(prefix="/trivia_participation")

@router.post("/read/", response_model=TriviaQuestionListResponse)
def list_question_from_trivia_endpoint(trivia_participation_read: TriviaParticipationRead, db: Session = Depends(database.get_db)):
    try:
        question_list = list_question_from_trivia(trivia_participation_read=trivia_participation_read, db=db)
        return question_list
    except DatabaseError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/answer/", response_model=TriviaParticipationScoreResponse)
def answer_trivia_endpoint(trivia_participation_answer: TriviaParticipationAnswer, db: Session = Depends(database.get_db)):
    try:
        score = answer_trivia(trivia_participation_answer=trivia_participation_answer, db=db)
        return score
    except DatabaseError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
