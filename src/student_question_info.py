from dataclasses import dataclass

from src.question import Question
from src.student_partial_question_info import StudentPartialQuestionInfo


@dataclass
class StudentQuestionInfo:
    question: Question
    partial_question_info: list[StudentPartialQuestionInfo]
    code: str
    grade: int
    note: str

    def __init__(self, question, code, grade=0, partial_question_info=None, note=""):
        self.question = question if isinstance(question, Question) else Question(**question)
        self.code = code
        self.grade = grade
        self.note = note

        if partial_question_info is not None:
            self.partial_question_info = [StudentPartialQuestionInfo(**info) for info in partial_question_info]
        else:
            self.partial_question_info = [StudentPartialQuestionInfo(partial_question, 0)
                                          for partial_question in self.question.partial_questions]

    def __dict__(self):
        return {
            "question": self.question.__dict__(),
            "code": self.code,
            "grade": self.grade,
            "partial_question_info": [info.__dict__() for info in self.partial_question_info],
            "note": self.note
        }

    def update(self):
        self.grade = sum(info.grade for info in self.partial_question_info)