import streamlit as st
import pandas as pd
from components import get_quiz_question

questions = {
    "q1" : "Elegant and efficient",
    "q2" : "Written by someone who cares",
    "q3" : "Well written prose"}


def main():

    get_quiz_question()

    if st.button('Next'):
        st.write('Go to next question')
    

if __name__ == "__main__":
    main()