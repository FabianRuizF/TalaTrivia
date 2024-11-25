from sqlalchemy.orm import Session
from schemas.trivia_participation import TriviaParticipationRead, TriviaQuestionListResponse, TriviaParticipationAnswer, TriviaParticipationScoreResponse
from models.trivia_question import TriviaQuestion
from models.trivia_user import TriviaUser
from models.question import Question
from sqlalchemy.exc import IntegrityError, ProgrammingError

from models.trivia import Trivia
from utils.exception import DatabaseError

def list_question_from_trivia(trivia_participation_read: TriviaParticipationRead, db: Session):
    trivia_to_read_id = trivia_participation_read.trivia_id
    db_question_list = db.query(TriviaQuestion).filter(TriviaQuestion.trivia_id == trivia_to_read_id).all()
    question_list = []
    for question  in db_question_list:
        db_question = db.query(Question).filter(Question.question_id == question.question_id).first()
        question_list.append(db_question)
    trivia_question_list = TriviaQuestionListResponse(question_list=question_list)
    return trivia_question_list


def answer_trivia(trivia_participation_answer: TriviaParticipationAnswer, db: Session):
    user_id = trivia_participation_answer.user_id
    trivia_to_answer_id = trivia_participation_answer.trivia_id
    answer_list = trivia_participation_answer.question_answer_list
    db_question_list = db.query(TriviaQuestion).filter(TriviaQuestion.trivia_id == trivia_to_answer_id).all()
    try:
        assert len(answer_list) == len(db_question_list), f"Answer list has different size from the quantity of questions"
        final_score = 0
        for index,question  in enumerate(db_question_list):
            db_question = db.query(Question).filter(Question.question_id == question.question_id).first()
            correct_answer = db_question.correct_answer
            if(answer_list[index] == correct_answer):
                final_score = final_score + db_question.difficulty


        #We search for the TriviaUser record so we can update its score
        db_trivia_user = db.query(TriviaUser).filter(
            TriviaUser.trivia_id == trivia_to_answer_id,
            TriviaUser.user_id == user_id
        ).first()
        db_trivia_user.score = final_score
        db.commit()
        score_response = TriviaParticipationScoreResponse(score=final_score)
        return score_response

    except AssertionError as error:
        raise ValueError("Answer list is different from the quantity of questions")
    except ProgrammingError as error:
        db.rollback()
        raise DatabaseError(f"Database error: {str(error)}")
    except Exception as error:
        db.rollback()
        raise ValueError(f"An unexpected error occurred: {str(error)}")
