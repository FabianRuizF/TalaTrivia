from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import Base


class Question(Base):
    __tablename__ = "question"

    question_id = Column(Integer, primary_key=True, autoincrement=True)
    answer_1 = Column(String(200))
    answer_2 = Column(String(200))
    answer_3 = Column(String(200))
    answer_4 = Column(String(200))
    correct_answer = Column(Integer, nullable=False)
    difficulty = Column(Integer, nullable=False)


    def __repr__(self):
        return f"<Question(question_id={self.question_id}, q1='{self.answer_1}', q2='{self.answer_2}', q3='{self.answer_3}', q4='{self.answer_4}')>"
