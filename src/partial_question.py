from dataclasses import dataclass

@dataclass
class PartialQuestion:
    partial_question: str
    description: str
    grade: int
    grade_options: list[int]

    def __dict__(self):
        return {
            "partial_question": self.partial_question,
            "description": self.description,
            "grade": self.grade,
            "grade_options": self.grade_options
        }
