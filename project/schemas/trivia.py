from pydantic import BaseModel
from typing import List, Optional



class TriviaCreate(BaseModel):
    name: str
    description: str
    question_list_id: List[int]


class TriviaResponse(BaseModel):
    name: str
    description: str
    class Config:
        from_attributes = True
