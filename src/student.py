import multiprocessing
import os
from dataclasses import dataclass, field

from src.student_question_info import StudentQuestionInfo
from .settings_loader import questions

@dataclass
class Student:
    name: str
    surname: str
    student_number: str
    submission_directory: str
    total_grade: float
    question_info: list[StudentQuestionInfo]
    is_graded: dict[str, bool]

    def __init__(self, name, surname, submission_directory, student_number="", total_grade=None, question_info=None, is_graded=None):
        self.name = name
        self.surname = surname
        self.student_number = student_number
        self.submission_directory = submission_directory

        self.total_grade = 0 if total_grade is None else total_grade

        submission_files = self.initialize_submission_files()

        if question_info is not None:
            self.question_info = [StudentQuestionInfo(**info) for info in question_info]
        else:
            self.question_info = []
            for question in questions:
                self.initialize_question_info(submission_files, question)

        if is_graded is not None:
            self.is_graded = is_graded
        else:
            self.is_graded = {q_info.question.question: False for q_info in self.question_info}

    def initialize_question_info(self, submission_files, question):
        respective_submission_file = next((file for file in submission_files
                                          if any(key in file.lower() for key in question.keys)), None)

        if respective_submission_file is None:
            code = ""
        else:
            with open(respective_submission_file, "r") as f:
                code = f.read()

        self.question_info.append(StudentQuestionInfo(
            question = question,
            code=code,
            grade=0
        ))

    def initialize_submission_files(self):
        submission_files = []
        for root, dirs, files in os.walk(self.submission_directory):
            for file in files:
                if "macos" in root.lower():
                    continue
                if file.endswith(".py"):
                    submission_files.append(os.path.join(root, file))

        return submission_files

    def __dict__(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "student_number": self.student_number,
            "total_grade": self.total_grade,
            "submission_directory": self.submission_directory,
            "question_info": [info.__dict__() for info in self.question_info],
            "is_graded": self.is_graded
        }

    def update(self):
        for question_info in self.question_info:
            question_info.update()
        self.total_grade = sum([question_info.grade for question_info in self.question_info])

    def get_question_info(self, question_name):
        return next((info for info in self.question_info if info.question.question == question_name), None)

    def __hash__(self):
        return hash(self.name + self.surname)