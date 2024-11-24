from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import Base
#from .trivia import Trivia
#from .question import Question


class TriviaQuestion(Base):
    __tablename__ = "trivia_question"
    trivia_id = Column(Integer,ForeignKey('trivia.trivia_id'), primary_key=True)
    question_id = Column(Integer,ForeignKey('question.question_id'), primary_key=True)
#    trivia_id = Column(Integer, trivia_id_fk, primary_key=True)
#    question_id = Column(Integer, ForeignKey(Question.question_id), primary_key=True)


#    trivia = relationship(Trivia, back_populates="questions")
#    question = relationship(Question, back_populates="questions")
