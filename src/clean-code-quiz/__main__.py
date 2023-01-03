import streamlit as st
from components import get_quiz_question

quizzes = [{"What is Clean Code?" : 
                ["Elegant and efficient", "Written by someone who cares", "Well written prose"]},
           {"What else is Clean Code?" : 
                ["Elegant and efficient", "Written by someone who cares", "Well written prose"]},
           {"What ELSE is Clean Code?" : 
                ["Elegant and efficient", "Written by someone who cares", "Well written prose"]}
            ]


if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage(): 
    st.session_state.page += 1

def restart(): 
    st.session_state.page = 0

placeholder = st.empty()

question = list(quizzes[st.session_state.page].keys())[0]
answers = list(quizzes[st.session_state.page].values())[0]

get_quiz_question(question, answers)

st.button("Next", on_click=nextpage, disabled=(st.session_state.page > len(quizzes) - 2))