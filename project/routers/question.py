from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.question import create_question, delete_question, list_all_question
from schemas.question import QuestionCreate, QuestionResponse, QuestionListResponse, QuestionDelete
from database import database
from utils.exception import DatabaseError

router = APIRouter(prefix="/question")

@router.post("/create/", response_model=QuestionResponse)
def create_question_endpoint(question: QuestionCreate, db: Session = Depends(database.get_db)):
    print(question)
    try:
        new_question = create_question(question=question, db=db)
        return new_question
    except DatabaseError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}/", response_model=QuestionResponse)
def delete_question_endpoint(question: QuestionDelete, db: Session = Depends(database.get_db)):
    try:
        is_deleted = delete_question(question=question, db=db)
        return is_deleted
    except DatabaseError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list/", response_model=QuestionListResponse)
def list_endpoint(db: Session = Depends(database.get_db)):
    try:
        all_questions = list_all_questions(db=db)
        return all_questions
    except DatabaseError as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
