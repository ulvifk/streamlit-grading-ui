from utils import load_students, save_students

students = load_students("students.json")

for student in students:
    q_info = next(q_info for q_info in student.question_info if q_info.question.question == "Question4")
    partial_q_info = q_info.partial_question_info[2]
    partial_q_info.partial_question.grade = 5
    partial_q_info.partial_question.grade_options[-1] = 5

    if partial_q_info.grade == 4:
        partial_q_info.grade = 5

    student.update()

save_students(students)