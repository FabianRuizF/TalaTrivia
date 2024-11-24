from pydantic import BaseModel
from typing import List, Optional
from .question import QuestionResponse

class TriviaParticipationRead(BaseModel):
    trivia_id: int

class TriviaQuestionListResponse(BaseModel):
    question_list: List[QuestionResponse]

class TriviaParticipationAnswer(BaseModel):
    trivia_id: int
    user_id: int
    question_answer_list: List[int]


class TriviaParticipationScoreResponse(BaseModel):
    score: int
