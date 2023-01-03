import streamlit as st
import numpy as np
import session_state
from streamlit.ScriptRunner import RerunException
from streamlit.ScriptRequestQueue import RerunData

state = session_state.get(question_number=0)

@st.cache
def get_question(question_number):
    arr = np.random.randint(0, 100, 2)
    q = f"{arr[0]} * {arr[1]}"
    ans = arr[0]*arr[1]
    choices = ["Please select an answer", ans, ans-1, ans+1, ans+2]
    return arr, q, ans, choices

arr, q, ans, choices = get_question(state.question_number)

st.text(f"Solve: {q}")
a = st.selectbox('Answer:', choices)

if a != "Please select an answer":
    st.write(f"You chose {a}")
    if (ans == a):
        st.write("Correct!")
    else:
        st.write(f"Wrong!, the correct answer is {ans}")
            
if st.button('Next question'):
    state.question_number += 1
    raise RerunException(RerunData(widget_state=None))