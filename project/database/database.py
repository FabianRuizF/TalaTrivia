from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

settings = settings.get_settings(env="test")
print(settings)
SQLALCHEMY_DATABASE_URL = settings.database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
