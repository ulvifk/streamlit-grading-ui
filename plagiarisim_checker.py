import os
import shutil
import unicodedata

from fpdf import FPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.classroom import ClassroomBuilder, Classroom
from src.utils import load_students


def transliterate_to_ascii(s):
    # Normalize unicode characters to their closest ASCII representation
    normalized = unicodedata.normalize('NFKD', s)

    # Encode to ASCII bytes, then decode back to string, ignoring non-ASCII characters
    ascii_encoded = normalized.encode('ascii', 'ignore').decode('ascii')

    # Custom replacements for specific characters
    replacements = {
        'ı': 'i',
        'ğ': 'g',
        "ç": "c",
        "ö": "o",
        "ü": "u",
    }

    # Apply custom replacements
    result = ''.join(replacements.get(char, char) for char in ascii_encoded)

    return result

def vectorize(Text):
    return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2):
    return cosine_similarity([doc1, doc2])

def check_plagiarism(s_vectors) -> set:
    plagiarism_results = set()

    for student_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b), key=lambda x: x.name)
            score = (student_pair[0], student_pair[1], sim_score)
            plagiarism_results.add(score)
    return plagiarism_results

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

def main():
    question_name = "Question1"
    students = load_students("students.json")
    for student in students:
        student.get_question_info(question_name).code = transliterate_to_ascii(
            student.get_question_info(question_name).code)
    student_file_mapping = {student: student.get_question_info(question_name).code for student in students}

    vectors = vectorize(list(student_file_mapping.values()))
    s_vectors = list(zip(student_file_mapping.keys(), vectors))

    # Usage example, replace 'your_directory_path' with the path to your directory
    directory_to_clear = 'your_directory_path'
    clear_directory(directory_to_clear)

    data = sorted(list(check_plagiarism(s_vectors)), key=lambda x: x[2], reverse=True)

    # cleea plag_pairs dir

    clear_directory("plag_pairs")

    for data_point in data:
        if data_point[2] < 0.5:
            break
        print(f"{data_point[0].name} - {data_point[1].name}: {data_point[2]}")

        note = f"Plagiarism between {data_point[0].name} and {data_point[1].name} is {data_point[2]}."

        folder_name = (f"plag_pairs/{data_point[2]}_{data_point[0].name}-{data_point[0].surname}"
                       f"_{data_point[1].name}-{data_point[1].surname}/")
        os.makedirs(folder_name, exist_ok=True)

        (strings_to_pdf(data_point[0].get_question_info(question_name).code,
                                f"{data_point[0].name} - {data_point[1].name}")
         .output(folder_name + f"{data_point[0].name}_{data_point[0].surname}.pdf"))
        (strings_to_pdf(data_point[1].get_question_info(question_name).code,
                                  f"{data_point[0].name} - {data_point[1].name}")
         .output(folder_name + f"{data_point[1].name}_{data_point[1].surname}.pdf"))

def check_for_plag(classroom: Classroom, question_name: str, output_dir: str):
    students = classroom.students
    for student in students:
        student.get_question_info(question_name).code = transliterate_to_ascii(
            student.get_question_info(question_name).code)
    student_file_mapping = {student: student.get_question_info(question_name).code for student in students}

    vectors = vectorize(list(student_file_mapping.values()))
    s_vectors = list(zip(student_file_mapping.keys(), vectors))

    data = sorted(list(check_plagiarism(s_vectors)), key=lambda x: x[2], reverse=True)

    clear_directory(output_dir)

    for data_point in data:
        if data_point[2] < 0.5:
            break
        print(f"{data_point[0].name} - {data_point[1].name}: {data_point[2]}")

        note = f"Plagiarism between {data_point[0].name} and {data_point[1].name} is {data_point[2]}."

        folder_name = (f"plag_pairs/{data_point[2]}_{data_point[0].name}-{data_point[0].surname}"
                       f"_{data_point[1].name}-{data_point[1].surname}/")
        os.makedirs(folder_name, exist_ok=True)

        (strings_to_pdf(data_point[0].get_question_info(question_name).code,
                        f"{data_point[0].name} - {data_point[1].name}")
         .output(folder_name + f"{data_point[0].name}_{data_point[0].surname}.pdf"))
        (strings_to_pdf(data_point[1].get_question_info(question_name).code,
                        f"{data_point[0].name} - {data_point[1].name}")
         .output(folder_name + f"{data_point[1].name}_{data_point[1].surname}.pdf"))


if __name__ == "__main__":
    # main()
    classroom = ClassroomBuilder("submissions").unzip().build()
    check_for_plag(classroom, "Question1", "plag_pairs")