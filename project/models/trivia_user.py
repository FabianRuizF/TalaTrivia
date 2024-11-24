from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import Base


class TriviaUser(Base):
    __tablename__ = "trivia_user"
    trivia_id = Column(Integer,ForeignKey('trivia.trivia_id'), primary_key=True)
    user_id = Column(Integer,ForeignKey('user.user_id'), primary_key=True)
