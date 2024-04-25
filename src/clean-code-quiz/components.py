import streamlit as st
from functools import reduce


def get_quiz_form(quiz):
    question = quiz["question"]
    correct_answers = quiz["answers"]

    explanation_key = f"show_explanation_{question}"
    if explanation_key not in st.session_state:
        st.session_state[explanation_key] = False


    with st.form(key=f"form_{question}"):
        if "code" in quiz:
            st.code(quiz["code"], language="python")

        answers = []
        options = quiz["options"]
        st.markdown(f"**{question}**")
        for i, option in enumerate(options):
            answers.append(st.checkbox(option, key=f"{question}_{i}"))

        submitted = st.form_submit_button("Check answers")

    if submitted:
        # Calculate correctness immediately after form submission
        all_answers_correct = reduce(
            lambda x, y: x and y,
            [a == c for a, c in zip(answers, correct_answers)],
            True,
        )

        # Set the correctness state for use in main.py
        st.session_state['current_correct'] = all_answers_correct

        if all_answers_correct:
            st.success("Correct! Great job.")
            if "score" in st.session_state:
                st.session_state["score"] += 1
        else:
            st.error("Incorrect. Try again!")
            st.session_state[explanation_key] = True

    # Conditionally show explanation based on state
    if st.session_state[explanation_key]:
        if st.button("Show Explanation", key=f"btn_explanation_{question}"):
            explanation_text = f"## Explanation\n{quiz['explanation']}"
            st.markdown(explanation_text)
            st.session_state[explanation_key] = False  # Reset after showing



def get_quiz_form_(quiz):

    question = quiz["question"]
    correct_answers = quiz["answers"]
    with st.form(f"my_form_{question}"):

        if "code" in quiz.keys():
            code = quiz["code"]
            code = f"{code}"
            st.code(code, language="java")

        answers = []
        options = quiz["options"]
        st.write(f"**{question}**")
        for option in options:
            answers.append(st.checkbox(option))

        # Every form must have a submit button.
        submitted = st.form_submit_button("Check answers")

        # st.write(correct_answers)
        # st.write(question)
        # st.write(answers)

    if submitted:
        all_answers_correct = reduce(
            lambda x, y: x and y,
            map(lambda k, l: k == l, answers, correct_answers),
            True,
        )
        if all_answers_correct:
            with open("style_correct.css") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        else:
            with open("style_wrong.css") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
