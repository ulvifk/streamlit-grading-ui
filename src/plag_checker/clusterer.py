import numpy as np
import pandas as pd

from src.plag_checker.plag_checker import PlagiarismChecker
from src.student import Student
import src.plag_checker.utils as utils
from sklearn.cluster import DBSCAN
from itertools import combinations


def cluster(students: list[Student], question_name: str):
    plagiarisim_checker = PlagiarismChecker(students, question_name)

    X = plagiarisim_checker.vectors

    combs = combinations(X, 2)
    for comb in combs:
        print(utils.similarity_minus_one(comb[0], comb[1]))

    clustering = DBSCAN(eps=1e-10, p=1, min_samples=1, metric=utils.similarity_minus_one).fit(X)

    print(np.unique(clustering.labels_))
    df = pd.DataFrame(columns=["Student Name", "Student Surname", "Cluster"])
    for i, student in enumerate(students):
        df.loc[i] = [student.name, student.surname, clustering.labels_[i]]

    print(df)




