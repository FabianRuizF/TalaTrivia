from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import Base


class TriviaQuestion(Base):
    __tablename__ = "trivia_question"
    trivia_id = Column(Integer,ForeignKey('trivia.trivia_id'), primary_key=True)
    question_id = Column(Integer,ForeignKey('question.question_id'), primary_key=True)
