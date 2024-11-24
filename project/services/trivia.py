from sqlalchemy.orm import Session
from database import database
from schemas.trivia import TriviaCreate, TriviaResponse
from models.trivia_question import TriviaQuestion
from models.trivia import Trivia
from utils.exception import DatabaseError

def create_trivia(trivia: TriviaCreate, db: Session):
    # Create trivia
    db_trivia = Trivia(name=trivia.name, description=trivia.description)
    db.add(db_trivia)
    db.commit()
    db.refresh(db_trivia)

    # Add questions to trivia
    for question_id in trivia.question_list_id:
        print(db_trivia.trivia_id)
        print(question_id)
        trivia_question = TriviaQuestion(trivia_id=db_trivia.trivia_id, question_id=question_id)
        db.add(trivia_question)

    db.commit()
    return TriviaResponse.from_orm(db_trivia)
