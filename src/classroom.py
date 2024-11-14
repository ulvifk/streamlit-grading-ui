import os
import zipfile
from dataclasses import dataclass

from src.student import Student


@dataclass
class Classroom:
    students: list[Student]


class ClassroomBuilder:
    directory: str

    def __init__(self, directory: str):
        self.directory = directory

    def unzip(self) -> "ClassroomBuilder":
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                try:
                    if file.endswith(".zip"):
                        zip_path = os.path.join(root, file)
                        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                            zip_ref.extractall(root)
                except Exception as e:
                    print(f"Failed to unzip {file}. Reason: {e}")

        return self

    def build(self) -> Classroom:
        def get_all_student_submission_paths() -> list[str]:
            student_submission_paths = []
            for name in os.listdir(self.directory):
                full_path = os.path.join(self.directory, name)
                if os.path.isdir(full_path):
                    student_submission_paths.append(full_path)

            return student_submission_paths

        def get_name_surname_from_path(path: str) -> tuple[str, str]:
            try:
                name = path.split("/")[-1].split("_")[0].split(" ")[0]
                surname = path.split("/")[-1].split("_")[0].split(" ")[1]
                return name, surname
            except Exception as e:
                # print(f"Failed to get name and surname from path {path}.")
                name = path.split("/")[-1]
                return name, ""

        student_submission_dirs = get_all_student_submission_paths()

        students = []
        for student_submission_dir in student_submission_dirs:
            name = get_name_surname_from_path(student_submission_dir)[0]
            surname = get_name_surname_from_path(student_submission_dir)[1]

            students.append(Student(
                name=name,
                surname=surname,
                submission_directory=student_submission_dir,
            ))

        return Classroom(students=students)
