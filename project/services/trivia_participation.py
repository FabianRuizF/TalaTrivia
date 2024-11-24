from sqlalchemy.orm import Session
from database import database
from schemas.trivia_question import TriviaQuestionRead, DummyResponse, TriviaQuestionListResponse
from models.trivia_question import TriviaQuestion
from models.question import Question

from models.trivia import Trivia
from utils.exception import DatabaseError

def list_question_from_trivia(trivia_question: TriviaQuestionRead, db: Session):
    db_trivia_question = db.query(TriviaQuestion).filter(TriviaQuestion.trivia_id == trivia_question.trivia_id).all()
    d = []
    for a  in db_trivia_question:
        db_question = db.query(Question).filter(Question.question_id == a.question_id).first()
        d.append(db_question)
        print(a.question_id)
        print(db_question)
    print(db_trivia_question)
    dummy = TriviaQuestionListResponse(question_list=d)
    return dummy
