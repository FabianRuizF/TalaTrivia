from sqlalchemy.orm import Session
from database import database
from schemas.trivia_participation import TriviaParticipationRead, TriviaQuestionListResponse
from models.trivia_question import TriviaQuestion
from models.question import Question

from models.trivia import Trivia
from utils.exception import DatabaseError

def list_question_from_trivia(trivia_participation: TriviaParticipationRead, db: Session):
    db_question_list = db.query(TriviaQuestion).filter(TriviaQuestion.trivia_id == trivia_participation.trivia_id).all()
    question_list = []
    for question  in db_question_list:
        db_question = db.query(Question).filter(Question.question_id == question.question_id).first()
        question_list.append(db_question)
    trivia_question_list = TriviaQuestionListResponse(question_list=question_list)
    return trivia_question_list
