import streamlit as st
import json
from components import get_quiz_form
from leaderboard import save_score, reset_leaderboard, show_plot

with open("style_default.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


if "quiz" not in st.session_state:
    with open("quizzes/chat_gpt.json") as json_file:
        data = json.load(json_file)
        st.session_state.quiz = data["quiz"]
        st.session_state.references = data["references"]
        st.session_state.info = data["info"]


if "page" not in st.session_state:
    st.session_state.page = -1

if "progress" not in st.session_state:
    st.session_state["progress"] = 0

if "score" not in st.session_state:
    st.session_state["score_saved"] = False
    st.session_state["score"] = 0

def previous_page():
    st.session_state.page -= 1
    st.session_state["progress"] -= 1

def nextpage():
    st.session_state.page += 1
    st.session_state["progress"] += 1

def restart():
    st.session_state.page = 0
    st.session_state["progress"] = 0

# Admin Tools with password protection
with st.sidebar:
    st.header("Admin Tools")
    admin_password = st.text_input("Enter admin password:", type="password")
    if admin_password == "your_secure_password":  # Replace "your_secure_password" with your actual password
        if st.button("Reset Leaderboard"):
            reset_leaderboard()
            st.success("Leaderboard has been reset.")

if st.session_state.page == -1:
    st.subheader(f"Welcome to this week's quiz about {st.session_state.info['title']}")
    st.markdown(f"{st.session_state.info['description']}")
    
    # Using columns to center buttons and show highscore
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        # align the button center
        if st.button("Start Quiz"): 
            st.session_state.page = 0
            st.experimental_rerun()
    show_plot()


elif st.session_state.page >= 0 and st.session_state.page < len(st.session_state.quiz):
        
        st.subheader(f"Question {st.session_state.page + 1} of {len(st.session_state.quiz)}")

        quiz = st.session_state.quiz[st.session_state.page]
        get_quiz_form(quiz)

        col1, col2 = st.columns(2)
        col1.button("Back", on_click=previous_page, disabled=(st.session_state.page == 0))
        col2.button("Next", on_click=nextpage, disabled=(st.session_state.page >= len(st.session_state.quiz)))

        my_bar = st.progress(0)
        my_bar.progress(st.session_state["progress"] / len(st.session_state.quiz))

elif st.session_state.page == len(st.session_state.quiz):
    st.markdown("<h2 style='text-align: center;'>Well done - Quiz Over</h2>", unsafe_allow_html=True)
    name = st.text_input("Enter your name to save your score:")
    department = st.selectbox("Enter your department:", ["Accounting", "CMP", "CSS", "CST", "CRD", "ESC", "Events", "GMS", "Legal", "OM", "Marketing", "TA", "TI", "ACE", "CNS", "CEA", "CybSec", "Data & AI", "DevOps", "DiE", "ICE", "IoT", "IT Stabilization", "Mobile", "Ojemba", "PED", "PQE", "Smart Devices", "Venturing", "Web"])
    col1, col2, col3 = st.columns([1, 1, 1])
    saved = False
    with col2:
        saved = st.button("Submit Score")
        
        if saved:
            score = st.session_state["score"]
            if st.session_state["score_saved"] == False:
                save_score(name, department, score)
                st.session_state["score_saved"] = True

    if saved:        
        st.success("Score saved!")
        show_plot()
        st.balloons()
    
    # empty space
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Additional Resources")
    for ref in st.session_state.references:
        st.markdown(f"[{ref['description']}]({ref['url']})", unsafe_allow_html=True)

