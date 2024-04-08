import multiprocessing
import os
from dataclasses import dataclass, field

from src.student_question_info import StudentQuestionInfo
from .settings_loader import questions

@dataclass
class Student:
    name: str
    surname: str
    submission_directory: str
    total_grade: float
    question_info: list[StudentQuestionInfo]

    def __init__(self, name, surname, submission_directory, total_grade=None, question_info=None):
        self.name = name
        self.surname = surname
        self.submission_directory = submission_directory

        self.total_grade = 0 if total_grade is None else total_grade

        submission_files = []
        for root, dirs, files in os.walk(self.submission_directory):
            for file in files:
                if "macos" in root.lower():
                    continue
                if file.endswith(".py"):
                    submission_files.append(os.path.join(root, file))

        if question_info is not None:
            self.question_info = [StudentQuestionInfo(**info) for info in question_info]
        else:
            self._initialize_question_info(submission_files)

    def _initialize_question_info(self, submission_files):
        self.question_info = []
        for question in questions:
            respective_submission_file = next((file for file in submission_files
                                              if any(key in file for key in question.keys)), None)

            with open(respective_submission_file, "r") as f:
                code = f.read()

            self.question_info.append(StudentQuestionInfo(
                question = question,
                code=code,
                grade=0
            ))

    def __dict__(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "total_grade": self.total_grade,
            "submission_directory": self.submission_directory,
            "question_info": [info.__dict__() for info in self.question_info]
        }

    def update(self):
        for question_info in self.question_info:
            question_info.update()
        self.total_grade = sum([question_info.grade for question_info in self.question_info])