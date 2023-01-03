import streamlit as st


def get_quiz_question(question, answers):

    with st.form(f"my_form_{question}"):
    
        st.write(f'**{question}**')
        checkbox_vals = []

        for answer in answers:
            checkbox_vals.append(st.checkbox(answer))
        
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")

    if submitted:
        for i, answer in enumerate(checkbox_vals):
            st.write(f"Question: {i} - Answer: {answer}")