import contextlib
import io
import sys

import streamlit as st
from streamlit_ace import st_ace

from src.student_question_info import StudentQuestionInfo
from utils import save_students


@contextlib.contextmanager
def capture_stdout():
    new_stdout = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = new_stdout
    try:
        yield new_stdout
    finally:
        sys.stdout = old_stdout

def create_ace_component_for_question_info(question_info: StudentQuestionInfo):
    component = st_ace(value = question_info.code, language="python")
    return component

def grader_page():
    if "questions" not in st.session_state:
        st.error("Questions not found in session state")
        return
    if "students" not in st.session_state:
        st.error("Students not found in session state")
        return

    questions = st.session_state["questions"]
    students = st.session_state["students"]


    student_names = [f"{student.name} {student.surname}" for student in students]

    question_names = [question.question for question in questions]

    info_col, student_select_col = st.columns(2)

    with student_select_col:
        selected_student_name = st.selectbox(label="Students", options=student_names)
        selected_student = students[student_names.index(selected_student_name)]

        selected_question_name = st.selectbox(label="Questions", options=question_names)
        selected_question = questions[question_names.index(selected_question_name)]

        question_info = next((info for info in selected_student.question_info if info.question == selected_question),
                             None)

    with info_col:
        st.write(f"**Name:** {selected_student.name} {selected_student.surname}")
        total_grade_placeholder = st.empty()

    total_grade_placeholder.write(f"**Total Grade:** {selected_student.total_grade}")

    code = create_ace_component_for_question_info(question_info)
    run_code_button = st.button("Run")

    if run_code_button:
        # Try to execute the entered code and catch any errors
        try:
            # The global and local scope for the executed code
            global_scope = {}
            local_scope = {}

            # Use the capture_stdout context manager to capture output
            with capture_stdout() as captured:
                # Execute the code
                exec(code, global_scope, local_scope)

            # Display captured stdout (console output)
            st.text_area("Console Output:", captured.getvalue(), height=150)
            st.success("Execution Successful")

        except Exception as e:
            # Display the error to the user
            st.error(f"Error: {e}")

    st.divider()
    for index, partial_question_info in enumerate(question_info.partial_question_info):
        partial_question = partial_question_info.partial_question

        st.write(f"**{partial_question.partial_question}**")
        st.write(f"**Description:** {partial_question.description}")

        init_index = partial_question.grade_options.index(partial_question_info.grade)

        chosen_grade = st.radio("Grade", options=partial_question.grade_options, index=init_index,
                                key=f"{index}grade {selected_question.question} {selected_student.name} {selected_student.surname}")

        partial_question_info.grade = chosen_grade
        selected_student.update()

        total_grade_placeholder.write(f"**Total Grade:** {selected_student.total_grade}")

    save_students(students)
    save_button = st.button("Save")
    if save_button:
        save_students(students)

if __name__ == "__main__":
    grader_page()