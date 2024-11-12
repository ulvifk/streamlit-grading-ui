import os
import shutil

from fpdf import FPDF

from src.classroom import ClassroomBuilder
from src.plag_checker.pair_wise import *


def pair_wise_output(plagiarism_results, question_name):
    data = sorted(list(plagiarism_results), key=lambda x: x[2], reverse=True)
    dir = f"{question_name}_plag_pairs"
    shutil.rmtree(dir, ignore_errors=True)

    for data_point in data:
        if data_point[2] < 0.5:
            continue
        print(f"{data_point[0].name} - {data_point[1].name}: {data_point[2]}")

        folder_name = (f"{dir}/{data_point[2]:.5f}_{data_point[0].name}-{data_point[0].surname}"
                       f"_{data_point[1].name}-{data_point[1].surname}/")
        os.makedirs(folder_name, exist_ok=True)

        (strings_to_pdf(data_point[0].get_question_info(question_name).code,
                        f"{data_point[0].name} - {data_point[1].name}")
         .output(folder_name + f"{data_point[0].name}_{data_point[0].surname}.pdf"))
        (strings_to_pdf(data_point[1].get_question_info(question_name).code,
                        f"{data_point[0].name} - {data_point[1].name}")
         .output(folder_name + f"{data_point[1].name}_{data_point[1].surname}.pdf"))


def main():
    question_name = "Question3"
    classroom = ClassroomBuilder("submissions").unzip().build()

    # cluster(students, question_name)
    plagiarism_results = (PlagiarismChecker(classroom.students, question_name)
                          .cast_to_lower()
                          .drop_piece_of_text("#", "\n")
                          .drop_piece_of_text('"""', '"""')
                          .drop_char(" ")
                          .drop_char("\n")
                          .check())
    pair_wise_output(plagiarism_results, question_name)

    # plagiarism_results = pair_wise_df(classroom, question_name)
    # plagiarism_results.to_csv(f"{question_name}_plagiarism_results.csv", index=False)


def strings_to_pdf(string1, note):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, string1)

    return pdf


if __name__ == "__main__":
    main()
