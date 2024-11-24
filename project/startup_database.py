from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from models.user import User
from models.question import Question

settings = settings.get_settings(env="test")
print(settings)
SQLALCHEMY_DATABASE_URL = settings.database_url
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create Tables
User.__table__.create(engine, checkfirst=True)
Question.__table__.create(engine, checkfirst=True)
