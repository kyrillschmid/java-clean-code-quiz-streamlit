import streamlit as st
import pandas as pd
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




def main():

    current_quiz = 0
    
    get_quiz_question(quizzes[current_quiz])

    if st.button('Next'):
        current_quiz += 1
        get_quiz_question(current_quiz, quizzes[current_quiz])
    

if __name__ == "__main__":
    main()