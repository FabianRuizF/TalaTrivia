from pydantic import BaseModel
from typing import List, Optional

class QuestionCreate(BaseModel):
    answer_1: str
    answer_2: str
    answer_3: str
    answer_4: str
    correct_answer: int
    difficulty: int

class QuestionResponse(BaseModel):
    question_id: int
    answer_1: str
    answer_2: str
    answer_3: str
    answer_4: str
    correct_answer: int
    difficulty: int
    class Config:
        from_attributes = True

class QuestionListResponse(BaseModel):
    question_list: List[QuestionResponse]

class QuestionDelete(BaseModel):
    question_id: int
