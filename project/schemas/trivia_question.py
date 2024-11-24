from pydantic import BaseModel
from typing import List, Optional
from .question import QuestionResponse


class TriviaQuestionRead(BaseModel):
    trivia_id: int


class TriviaQuestionListResponse(BaseModel):
    question_list: List[QuestionResponse]

class DummyResponse(BaseModel):
    dummy: int
