from sqlalchemy.orm import Session
from schemas.trivia import TriviaCreate, TriviaResponse
from models.trivia_question import TriviaQuestion
from models.trivia_user import TriviaUser

from models.trivia import Trivia
from utils.exception import DatabaseError

def create_trivia(trivia: TriviaCreate, db: Session):
    # Create trivia
    db_trivia = Trivia(name=trivia.name, description=trivia.description)
    db.add(db_trivia)
    db.commit()
    db.refresh(db_trivia)

    # Add questions to trivia_question junction table
    for question_id in trivia.question_list_id:
        trivia_question = TriviaQuestion(trivia_id=db_trivia.trivia_id, question_id=question_id)
        db.add(trivia_question)

    # Add users to trivia_user junction table
    for user_id in trivia.user_list_id:
        trivia_question = TriviaUser(trivia_id=db_trivia.trivia_id, user_id=user_id)
        db.add(trivia_question)

    db.commit()
    return TriviaResponse.from_orm(db_trivia)
