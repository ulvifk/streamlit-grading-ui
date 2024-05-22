import os
import pickle

import numpy as np
from sentence_transformers import SentenceTransformer

from src.student import Student
import src.plag_checker.utils as utils


def cut_string_at_first_occurrence(text, keyword):
    # Split the text at the first occurrence of the keyword
    parts = text.split(keyword, 1)

    # Return the part before the keyword if the keyword exists in the text
    if len(parts) > 1:
        return parts[1]
    else:
        return text  # Return the original text if the keyword is not found


class PlagiarismChecker:
    students: list[Student]
    student_file_mapping: dict[Student, str]
    model: SentenceTransformer
    vectors: np.ndarray
    s_vectors: list[tuple[Student, list[float]]]

    def __init__(self, students: list[Student], question_name: str):
        for student in students:
            student.get_question_info(question_name).code = utils.transliterate_to_ascii(student.get_question_info(question_name).code)

        student_file_mapping = {student: student.get_question_info(question_name).code.replace(" ", "").replace("\n", "").lower() for student in students}

        self.load_model()
        self.vectors = self.vectorize(list(student_file_mapping.values()))
        self.s_vectors = list(zip(student_file_mapping.keys(), self.vectors))

    def load_model(self):
        if not os.path.exists("model.pkl"):
            self.model = SentenceTransformer("all-MiniLM-L6-v2")
            with open("model.pkl", "wb") as f:
                pickle.dump(self.model, f)
        else:
            with open("model.pkl", "rb") as f:
                self.model = pickle.load(f)

    def vectorize(self, text):
        return self.model.encode(text)
