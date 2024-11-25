from sqlalchemy.exc import IntegrityError, ProgrammingError
from models.question import Question
from schemas.question import QuestionCreate, QuestionResponse, QuestionDelete, QuestionListResponse
from sqlalchemy.orm import Session
from utils.exception import DatabaseError


def create_question(question: QuestionCreate, db: Session ):
    db_question = Question(answer_1=question.answer_1, answer_2=question.answer_2, answer_3=question.answer_3, answer_4=question.answer_4,
        correct_answer=question.correct_answer,
        difficulty=question.difficulty
    )
    try:
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        print(db_question)
        return QuestionResponse.from_orm(db_question)
    except IntegrityError as error:
        db.rollback()
        raise ValueError(f"There is an integrity error while creating question: {error}")
    except ProgrammingError as error:
        db.rollback()
        raise DatabaseError(f"Database error: {str(error)}")
    except Exception as error:
        db.rollback()
        raise ValueError(f"An unexpected error occurred: {str(error)}")

def delete_question(question: QuestionDelete, db: Session ):
    try:
        db_question = db.query(Question).filter(Question.question_id == question.question_id).first()
        if db_question is None:
            raise ValueError("Question not found")
        db.delete(db_question)
        db.commit()
        return QuestionResponse.from_orm(db_question)
    except ProgrammingError as error:
        db.rollback()
        raise DatabaseError(f"Database error: {str(error)}")
    except Exception as error:
        db.rollback()
        raise ValueError(f"An unexpected error occurred: {str(error)}")


def list_all_question(db: Session) -> QuestionListResponse:
    try:
        db_question_list = db.query(Question).all()
        if db_question_list is None:
            raise ValueError("There are no questions in the database")
        return QuestionListResponse(question_list = db_question_list)
    except ProgrammingError as error:
        db.rollback()
        raise DatabaseError(f"Database error: {str(error)}")
    except Exception as error:
        db.rollback()
        raise ValueError(f"An unexpected error occurred: {str(error)}")
