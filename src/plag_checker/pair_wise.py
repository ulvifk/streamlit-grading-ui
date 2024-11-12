import pandas as pd

import src.plag_checker.utils as utils
from src.classroom import Classroom
from src.plag_checker.plag_checker import PlagiarismChecker


def pair_wise(classroom: Classroom, question):
    students = classroom.students

    plag_checker = PlagiarismChecker(students, question)

    pairs = set()
    plagiarism_results = set()
    for student_a, text_vector_a in plag_checker.s_vectors:
        new_vectors = plag_checker.s_vectors.copy()
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

def pair_wise_df(students, question):
    plag_results = pair_wise(students, question)

    df = pd.DataFrame(columns=["Student1", "Student2", "Similarity"])
    for student1, student2, score in plag_results:
        df.loc[len(df)] = [f"{student1.name} {student1.surname}", f"{student2.name} {student2.surname}", score]

    return df

