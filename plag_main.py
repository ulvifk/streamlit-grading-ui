import os
import shutil
import unicodedata
import pickle

from fpdf import FPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.plag_checker.clusterer import cluster
from src.plag_checker.plag_checker import PlagiarismChecker
from src.plag_checker.pair_wise import *
from utils import load_students
from sentence_transformers import SentenceTransformer, util

def pair_wise_output(plagiarism_results, question_name):
    data = sorted(list(plagiarism_results), key=lambda x: x[2], reverse=True)
    dir = f"{question_name}_plag_pairs"
    clear_directory(dir)

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
    question_name = "Question1"
    students = load_students("students.json")

    # cluster(students, question_name)
    plagiarism_results = pair_wise(students, question_name)
    pair_wise_output(plagiarism_results, question_name)

    plagiarism_results = pair_wise_df(students, question_name)
    plagiarism_results.to_csv(f"{question_name}_plagiarism_results.csv", index=False)




def strings_to_pdf(string1, note):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, string1)

    return pdf

def clear_directory(directory_path):
    # Check if the directory exists
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        # Iterate over all the files and directories within the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            try:
                # If it's a file, delete it
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                # If it's a directory, delete it and all its contents
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

if __name__ == "__main__":
    main()

