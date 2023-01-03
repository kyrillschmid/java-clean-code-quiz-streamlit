import streamlit as st


def get_quiz_question():
    
    with st.form("my_form"):
    
        st.write('**What is Clean Code?**')

        checkbox_val_1 = st.checkbox("Elegant and efficient")
        checkbox_val_2 = st.checkbox("Written by someone who cares")
        checkbox_val_3 = st.checkbox("Well written prose")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("checkbox_val_1", checkbox_val_1, "checkbox_val_2", checkbox_val_2)