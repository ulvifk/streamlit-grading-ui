import os
import shutil

from fpdf import FPDF

from src.classroom import ClassroomBuilder
from src.plag_checker.pair_wise import *
from src.student import Student


def pair_wise_output(plagiarism_results, question_name):
    data = sorted(list(plagiarism_results), key=lambda x: x[2], reverse=True)
    dir = f"{question_name}_plag_pairs"
    shutil.rmtree(dir, ignore_errors=True)

    for data_point in data:
        if data_point[2] < 0.5:
            continue
        # print(f"{data_point[0].name} - {data_point[1].name}: {data_point[2]}")

        folder_name = (f"{dir}/{data_point[2]:.5f}_{data_point[0].name}-{data_point[0].surname}"
                       f"_{data_point[1].name}-{data_point[1].surname}/")
        os.makedirs(folder_name, exist_ok=True)

        (strings_to_pdf(data_point[0].get_question_info(question_name).code,
                        f"{data_point[0].name} - {data_point[1].name}")
         .output(folder_name + f"{data_point[0].name}_{data_point[0].surname}.pdf"))
        (strings_to_pdf(data_point[1].get_question_info(question_name).code,
                        f"{data_point[0].name} - {data_point[1].name}")
         .output(folder_name + f"{data_point[1].name}_{data_point[1].surname}.pdf"))


def strings_to_pdf(string1, note):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, string1)

    return pdf


def write_results_to_python(results: set[tuple[Student, Student, any]], *question_names: str):
    concat_name = "_".join(question_names)

    data = sorted(list(results), key=lambda x: x[2], reverse=True)
    dir = f"{concat_name}_plag_pairs"
    shutil.rmtree(dir, ignore_errors=True)

    for data_point in data:
        if data_point[2] < 0.5:
            continue

        folder_name = (f"{dir}/{data_point[2]:.5f}_{data_point[0].name}-{data_point[0].surname}"
                       f"_{data_point[1].name}-{data_point[1].surname}/")
        os.makedirs(folder_name, exist_ok=True)

        concat_code_student_1 = "\n".join(
            [data_point[0].get_question_info(question_name).code for question_name in question_names])
        concat_code_student_2 = "\n".join(
            [data_point[1].get_question_info(question_name).code for question_name in question_names])

        with open(f"{folder_name}/{data_point[0].name}_{data_point[0].surname}.py", "w", encoding="utf-8") as f:
            f.write(concat_code_student_1)

        with open(f"{folder_name}/{data_point[1].name}_{data_point[1].surname}.py", "w", encoding="utf-8") as f:
            f.write(concat_code_student_2)


def write_csv(results: set[tuple[Student, Student, any]], file_name: str):
    data = [
        (data_point[0].name, data_point[0].surname, data_point[1].name, data_point[1].surname, data_point[2])
        for data_point in results if data_point[2]
    ]

    df = pd.DataFrame(data,
                      columns=["Student1 Name", "Student1 Surname", "Student2 Name", "Student2 Surname", "Similarity"])

    df.to_csv(file_name, index=False)


def main():
    question_names = ["Question1a", "Question1b"]
    classroom = ClassroomBuilder("submissions").unzip().build()

    # cluster(students, question_name)
    plagiarism_results = (PlagiarismChecker(classroom.students, *question_names)
                          .cast_to_lower()
                          .drop_piece_of_text("#", "\n")
                          .drop_piece_of_text('"""', '"""')
                          .drop_char(" ")
                          .drop_char("\n")
                          .check())

    write_results_to_python(plagiarism_results, *question_names)
    write_csv(plagiarism_results, "plag_results.csv")


if __name__ == "__main__":
    main()
