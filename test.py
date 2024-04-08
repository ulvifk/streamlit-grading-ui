import streamlit as st
from utils import load_students, save_students
from src.settings_loader import questions
from streamlit_extras.switch_page_button import switch_page

def main():
    st.title('IE246 Grader')

    col1, col2 = st.columns(2)

    with col1:
        option = st.radio("Choose an action:", ('Initialize', 'Import'))
    with col2:
        confirm_button = st.button("Confirm")

    file_content = None
    students = []

    if option == 'Initialize':
        students = load_students()
    elif option == 'Import':
        file = st.file_uploader("Choose a file")
        if file is not None:
            file_content = file.getvalue().decode("utf-8")
            students = load_students(json_string=file_content)

    if confirm_button:
        st.session_state["questions"] = questions
        st.session_state["students"] = students
        switch_page("grader page")

if __name__ == "__main__":
    main()







