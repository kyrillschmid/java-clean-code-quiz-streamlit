import pandas as pd
import streamlit as st
import json


# Read and write to CSV for leaderboard
def save_score(name, department, score):
    try:
        # Load existing scores
        df = pd.read_csv('leaderboard.csv')
    except FileNotFoundError:
        # Initialize empty DataFrame if file doesn't exist
        df = pd.DataFrame(columns=['Name', "Department", 'Score'])
    
    # Create a new DataFrame for the new entry
    new_entry = pd.DataFrame({'Name': [name], 'Department': [department], 'Score': [score]})
    
    # Concatenate the old DataFrame with the new entry
    df = pd.concat([df, new_entry], ignore_index=True)
    
    # Save back to CSV
    df.to_csv('leaderboard.csv', index=False)


def show_plot():
    try:
        # Load the CSV file
        df = pd.read_csv('leaderboard.csv')

        # Aggregate scores by department
        # Calculate total scores and count of participants per department
        department_data = df.groupby('Department')['Score'].agg(['sum', 'count'])
        
        # Calculate the average score per department
        department_data['Average Score'] = department_data['sum'] / department_data['count']
        
        # Sort the average scores in descending order
        department_data = department_data.sort_values(by='Average Score', ascending=False)

        # Sort the DataFrame by 'Score' in descending order for leaderboard
        df = df.sort_values(by='Score', ascending=False)

        # Reset the index to prevent pandas from adding an unwanted index column in Streamlit table
        df.reset_index(drop=True, inplace=True)

        st.subheader("Normalized Scores by Department")
            # Prepare chart data
        chart_data = department_data[['Average Score']].reset_index()
        chart_data.columns = ['Department', 'Average Score']
        st.bar_chart(chart_data.set_index('Department'))

        # Display the DataFrame and the plot in Streamlit
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.subheader("Leaderboard")
            st.markdown(df.style.hide(axis='index').to_html(), unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)  # To add spacing if needed

        
    except FileNotFoundError:
        st.error("No scores available yet.")


def reset_leaderboard():
    import os
    # Check if the file exists
    if os.path.exists('leaderboard.csv'):
        os.remove('leaderboard.csv')  # Remove the CSV file
        # Optionally, recreate the file with headers if you don't want to check file existence when saving scores
        df = pd.DataFrame(columns=['Name', "Department", 'Score'])
        df.to_csv('leaderboard.csv', index=False)
        return "Leaderboard reset successfully."
    else:
        return "Leaderboard file does not exist."

