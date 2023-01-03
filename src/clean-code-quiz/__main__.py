import streamlit as st
from components import get_quiz_question

quizzes = [{
    "q1" : "Elegant and efficient",
    "q2" : "Written by someone who cares",
    "q3" : "Well written prose"
    },
    {"q1" : "Elegant and efficient",
    "q2" : "Written by someone who cares",
    "q3" : "Well written prose"
    }]


if "page" not in st.session_state:
    current_quiz = 0
    st.session_state.page = 0

def nextpage(): 
    current_quiz += 1
    st.session_state.page += 1

def restart(): 
    current_quiz = 0
    st.session_state.page = 0

placeholder = st.empty()
st.button("Next", on_click=nextpage, disabled=(st.session_state.page > 3))

if st.session_state.page == 0:
    # Replace the placeholder with some text:
    # placeholder.text(f"Hello, this is page {st.session_state.page}")
    get_quiz_question(placeholder, current_quiz, quizzes[current_quiz])

elif st.session_state.page == 1:
    # Replace the text with a chart:
    get_quiz_question(placeholder, current_quiz, quizzes[current_quiz])

elif st.session_state.page == 2:
# Replace the chart with several elements:
    get_quiz_question(placeholder, current_quiz, quizzes[current_quiz])

elif st.session_state.page == 3:
    placeholder.markdown(r"$f(x) = \exp{\left(x^🐈\right)}$")

else:
    with placeholder:
        st.write("This is the end")
        st.button("Restart",on_click=restart)