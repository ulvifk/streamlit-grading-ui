import pandas as pd
import yaml
import os
import zipfile
import json

from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.workbook import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

from src.question import Question
from src.settings_loader import questions
from src.student import Student
from unidecode import unidecode

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

def get_student_names(students: Student):
    df = pd.read_csv("student_list.csv")

    for student in students:
        row = get_corresponding_row(student, df)
        print(row["NAME"], row["SURNAME"])

def get_corresponding_row(student: Student, df: pd.DataFrame):
    for index, row in df.iterrows():
        unidecoded_name = unidecode(row["NAME"]).lower().split(" ")
        unidecoded_surname = unidecode(row["SURNAME"]).lower()
        for name in unidecoded_name:
            if name in student.name.lower() and unidecoded_surname in student.surname.lower():
                return row

    raise ValueError(f"Student {student.name} {student.surname} not found in the student list")


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

def save_to_excel(q_name):
    students = load_students("students.json")

    question = next((question for question in questions if question.question == q_name), None)
    columns = ["Name", "Surname"] + [partial_q.partial_question for partial_q in question.partial_questions] + ["Total Grade"]
    df = pd.DataFrame(columns=columns)
    for student in students:
        student_q_info = next((q_info for q_info in student.question_info if q_info.question.question == q_name), None)
        row = [student.name, student.surname]
        for p_q_info in student_q_info.partial_question_info:
            row.append(p_q_info.grade)
        row.append(student_q_info.grade)

        df.loc[len(df)] = row

    wb = Workbook()
    ws = wb.active

    # Add DataFrame rows to Excel worksheet
    for r in dataframe_to_rows(df, index=False, header=True):
        ws.append(r)

    # Define a table style
    tab = Table(displayName="Table1", ref=f"A1:{chr(65 + len(df.columns) - 1)}{len(df) + 1}")



    # Add the table to the worksheet
    ws.add_table(tab)

    # Save the workbook
    wb.save(q_name + ".xlsx")

def re_init_question(student: Student, question: Question):
    q_info = next((q_info for q_info in student.question_info if q_info.question.question == question.question), None)

    submission_files = student.initialize_submission_files()
    if q_info is not None:
        student.question_info.remove(q_info)

    student.initialize_question_info(submission_files, question)
    student.update()


def re_init_question_of_all_students(students, question: Question):
    for student in students:
        re_init_question(student, question)



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
    # unzip_all_in_directory("./submissions")
    students = load_students()
    get_student_names(students)
    x=0


