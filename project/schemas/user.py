from pydantic import BaseModel
from typing import List, Optional


class UserCreate(BaseModel):
    email: str
    password: str
    name: str

class UserResponse(BaseModel):
    email: str
    name: str
    class Config:
        from_attributes = True

class UserListResponse(BaseModel):
    user_list: List[UserResponse]

class UserDelete(BaseModel):
    email: str

