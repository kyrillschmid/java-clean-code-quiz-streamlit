import pandas as pd
import streamlit as st
import json

# Read and write to CSV for leaderboard
def save_score(name, score):
    try:
        # Load existing scores
        df = pd.read_csv('leaderboard.csv')
    except FileNotFoundError:
        # Initialize empty DataFrame if file doesn't exist
        df = pd.DataFrame(columns=['Name', 'Score'])
    
    # Create a new DataFrame for the new entry
    new_entry = pd.DataFrame({'Name': [name], 'Score': [score]})
    
    # Concatenate the old DataFrame with the new entry
    df = pd.concat([df, new_entry], ignore_index=True)
    
    # Save back to CSV
    df.to_csv('leaderboard.csv', index=False)

def show_leaderboard():
    try:
        df = pd.read_csv('leaderboard.csv')
        df = df.sort_values(by='Score', ascending=False)  # Sort by score descending
        st.table(df)
    except FileNotFoundError:
        st.write("No scores available yet.")


def reset_leaderboard():
    import os
    # Check if the file exists
    if os.path.exists('leaderboard.csv'):
        os.remove('leaderboard.csv')  # Remove the CSV file
        # Optionally, recreate the file with headers if you don't want to check file existence when saving scores
        df = pd.DataFrame(columns=['Name', 'Score'])
        df.to_csv('leaderboard.csv', index=False)
        return "Leaderboard reset successfully."
    else:
        return "Leaderboard file does not exist."

