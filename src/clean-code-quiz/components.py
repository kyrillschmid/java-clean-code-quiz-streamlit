import streamlit as st
from functools import reduce

def get_quiz_form(quiz):

    question = quiz["question"]
    correct_answers = quiz["answers"]
    with st.form(f"my_form_{question}"):
    
        if "code" in quiz.keys():
            code = quiz["code"]
            code = f'{code}'
            st.code(code, language='java')

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
        all_answers_correct = reduce(lambda x, y: x and y, map(lambda k, l : k == l, answers, correct_answers), True)
        if all_answers_correct:
            with open('style_correct.css') as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        else:
            with open('style_wrong.css') as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
        