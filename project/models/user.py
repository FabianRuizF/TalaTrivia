from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(64))
    name = Column(String(50))

    def __repr__(self):
        return f"<User(user_id={self.user_id}, name={self.name}, email={self.email})>"
