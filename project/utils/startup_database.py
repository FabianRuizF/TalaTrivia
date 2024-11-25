from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from models.user import User
from models.question import Question
from models.trivia import Trivia
from models.trivia_question import TriviaQuestion
from models.trivia_user import TriviaUser
from sqlalchemy.ext.declarative import declarative_base
from models.base import Base

def startup_database():
    database_settings = settings.get_settings(env="test")
    SQLALCHEMY_DATABASE_URL = database_settings.database_url
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(engine, checkfirst=True)

