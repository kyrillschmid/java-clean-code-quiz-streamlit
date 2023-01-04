import streamlit as st
import json
from components import get_quiz_form


with open('style_default.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if "quiz" not in st.session_state:
    with open('quizzes/m1_clean_code.json') as json_file:
        st.session_state.quiz = json.load(json_file)["quiz"]
    # st.write(st.session_state.quiz)

if "page" not in st.session_state:
    st.session_state.page = 0

if "progress" not in st.session_state:
    st.session_state["progress"] = 0


def previous_page(): 
    st.session_state.page -= 1
    st.session_state["progress"] -= 1

def nextpage(): 
    st.session_state.page += 1
    st.session_state["progress"] += 1

def restart(): 
    st.session_state.page = 0   
    st.session_state["progress"] = 0

placeholder = st.empty()

if st.session_state.page < len(st.session_state.quiz):
    quiz = st.session_state.quiz[st.session_state.page]
    # st.write(quiz)
    get_quiz_form(quiz)
else:
    emoji = ":rocket:"
    st.markdown("<h2 style='text-align: center;'>Well done - Quiz Over</h2>", unsafe_allow_html=True)
    # st.write(f"Well done - Quiz Over!  {emoji}")
    

col1, col2 = st.columns(2)
col1.button("Back", on_click=previous_page, disabled=(st.session_state.page == 0))
col2.button("Next", on_click=nextpage, disabled=(st.session_state.page > len(st.session_state.quiz) - 1))


my_bar = st.progress(0)
my_bar.progress(st.session_state["progress"] / len(st.session_state.quiz))
