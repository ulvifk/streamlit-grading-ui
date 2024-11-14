import os
import pickle
import re

import numpy as np
from sentence_transformers import SentenceTransformer

import src.plag_checker.utils as utils
from src.student import Student


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
    s_vectors: list[tuple[Student, any]]

    def __init__(self, students: list[Student], *question_names: str):
        for student in students:
            for question_name in question_names:
                student.get_question_info(question_name).code = utils.transliterate_to_ascii(
                    student.get_question_info(question_name).code)

        self.student_file_mapping = {
            student: self._merge_texts(
                [student.get_question_info(question_name).code for question_name in question_names]) for
            student in students}

    def _merge_texts(self, texts):
        return " ".join(texts)

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

    def drop_char(self, char: str) -> "PlagiarismChecker":
        for student, text in self.student_file_mapping.items():
            self.student_file_mapping[student] = text.replace(char, "")

        return self

    def cast_to_lower(self) -> "PlagiarismChecker":
        for student, text in self.student_file_mapping.items():
            self.student_file_mapping[student] = text.lower()

        return self

    def drop_piece_of_text(self, start, end) -> "PlagiarismChecker":
        def drop(text, start_text, end_text):
            pattern = re.escape("#") + ".*?" + re.escape("\n")
            return re.sub(pattern, '', text, flags=re.DOTALL)

        for student, text in self.student_file_mapping.items():
            self.student_file_mapping[student] = drop(text, start, end)

        return self

    def check(self):
        self.load_model()
        self.vectors = self.vectorize(list(self.student_file_mapping.values()))
        self.s_vectors = []
        for student, text in self.student_file_mapping.items():
            if text == "":
                print(f"Skipping {student.name} {student.surname} as the text is empty.")
                continue
            self.s_vectors.append((student, self.vectorize(text)))

        pairs = set()
        plagiarism_results = set()
        for student_a, text_vector_a in self.s_vectors:
            new_vectors = self.s_vectors.copy()
            current_index = new_vectors.index((student_a, text_vector_a))
            del new_vectors[current_index]
            for student_b, text_vector_b in new_vectors:
                sim_score = utils.similarity(text_vector_a, text_vector_b).numpy()[0][0]
                student_pair = sorted((student_a, student_b), key=lambda x: f"{x.name} {x.surname}")
                if tuple(student_pair) in pairs:
                    continue

                score = (student_pair[0], student_pair[1], sim_score)
                pairs.add(tuple(student_pair))
                plagiarism_results.add(score)
        return plagiarism_results
