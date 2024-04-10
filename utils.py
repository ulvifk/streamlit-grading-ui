import yaml
import os
import zipfile
import json

from src.question import Question
from src.student import Student


def timeout_handler(signum, frame):
    print("Timeout occurred")
    raise TimeoutError

def get_all_student_submission_paths() -> list[str]:
    directory = "submissions"

    student_submission_paths = []
    for name in os.listdir(directory):
        full_path = os.path.join(directory, name)
        if os.path.isdir(full_path):
            student_submission_paths.append(full_path)

    return student_submission_paths

def load_students(file_path=None, json_string=None):
    if file_path is None and json_string is None:
        student_submission_dirs = get_all_student_submission_paths()

        students = []
        for student_submission_dir in student_submission_dirs:
            students.append(Student(
                name=student_submission_dir.split("\\")[-1].split("_")[0].split(" ")[0],
                surname=student_submission_dir.split("\\")[-1].split("_")[0].split(" ")[1],
                submission_directory=student_submission_dir,
            ))

        return students

    if file_path is not None:
        with open(file_path, "r") as f:
            students = json.load(f)

        return [Student(**student) for student in students]

    if json_string is not None:
        students = json.loads(json_string)
        return [Student(**student) for student in students]


def save_students(students):
    with open("students.json", "w") as f:
        json.dump([student.__dict__() for student in students], f, indent=2)


def unzip_all_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            try:
                if file.endswith(".zip"):
                    zip_path = os.path.join(root, file)
                    print(f"Unzipping: {zip_path}")
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(root)
            except:
                pass


if __name__ == "__main__":
    #unzip_all_in_directory("./submissions")
    students = load_students()
    save_students(students)

    student = students[2]
    question_info_3 = student.question_info[0]
    print(f"{question_info_3.code}")
    exec("""
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

row = len(matrix)
column = len(matrix[0])
transpose = [[matrix[j][i] for j in range(row)] for i in range(column)]
print(transpose)
""", locals())


[[5, 6, 7], [10, 12 ,14]]