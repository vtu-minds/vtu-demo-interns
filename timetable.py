import streamlit as st
import pandas as pd

def app():
    st.title('VTU Current Year Timetable')

    # Replace this with the actual timetable data
    data = {
        "Semester": ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"],
        "Start Date": ["01-08-2023", "01-01-2024", "01-08-2023", "01-01-2024", "01-08-2023", "01-01-2024", "01-08-2023", "01-01-2024"],
        "End Date": ["31-12-2023", "31-06-2024", "31-12-2023", "31-06-2024", "31-12-2023", "31-06-2024", "31-12-2023", "31-06-2024"],
        "Exams Start": ["10-12-2023", "10-06-2024", "10-12-2023", "10-06-2024", "10-12-2023", "10-06-2024", "10-12-2023", "10-06-2024"],
        "Exams End": ["20-12-2023", "20-06-2024", "20-12-2023", "20-06-2024", "20-12-2023", "20-06-2024", "20-12-2023", "20-06-2024"],
    }

    df = pd.DataFrame(data)

    st.dataframe(df)

    st.write("Refer to the official VTU website for the most accurate and detailed timetable.")

