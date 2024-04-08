from dataclasses import dataclass
from .partial_question import PartialQuestion

@dataclass()
class Question:
    question: str
    keys: list[str]
    grade: float
    partial_questions: list[PartialQuestion]

    def __dict__(self):
        return {
            "question": self.question,
            "keys": self.keys,
            "grade": self.grade,
            "partial_questions": [pq.__dict__() for pq in self.partial_questions]
        }

    def __post_init__(self):
        partial_questions = []

        for pq in self.partial_questions:
            pq: dict
            partial_questions.append(PartialQuestion(**pq))

        self.partial_questions = partial_questions