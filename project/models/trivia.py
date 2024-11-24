from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import Base



class Trivia(Base):
    __tablename__ = "trivia"
    trivia_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True)
    description = Column(String(200), index=True)

#    questions = relationship("TriviaQuestion", back_populates="trivia")
