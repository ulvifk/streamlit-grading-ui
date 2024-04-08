from dataclasses import dataclass
from .partial_question import PartialQuestion

@dataclass
class StudentPartialQuestionInfo:
    partial_question: PartialQuestion
    grade: int

    def __init__(self, partial_question, grade=0):
        self.partial_question = partial_question if isinstance(partial_question, PartialQuestion) else PartialQuestion(**partial_question)
        self.grade = grade

    def __dict__(self):
        return {
            "partial_question": self.partial_question.__dict__(),
            "grade": self.grade
        }