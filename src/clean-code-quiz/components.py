import streamlit as st


def get_quiz_question(placeholder, key, questions):

    with placeholder.form(f"my_form_{key}"):
    
        placeholder.write('**What is Clean Code?**')
        checkbox_vals = []

        for key, value in questions.items():
            checkbox_vals.append(st.checkbox(value))
        
        # Every form must have a submit button.
        submitted = placeholder.form_submit_button("Submit")

    if submitted:
        for i, answer in enumerate(checkbox_vals):
            placeholder.write(f"Question: {i} - Answer: {answer}")