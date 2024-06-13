import pandas as pd
import streamlit as st


def load_aec_courses():
    aec_courses = {
        "3rd Semester": {
            "Computer Engineering": [
                "BCS358A Data analytics with Excel", "BCS358C Project Management with Git",
                "BCS358B R programming", "BCS358D Data Visualization with Phyton"
            ],
            "Electronics and Communication Engineering": [
                "BEC358A LABVIEW programming", "BEC358C C++ Basics",
                "BEC358B MATLAB Programming", "BEC358D IOT for Smart Infrastructure"
            ],
            "Artificial Intelligence and Machine Learning": [
                "BCS358A Data Analytics with Excel", "BCS358C Project Management with Git",
                "BAI358B Ethics and Public Policy for AI", "BAI358D PHP Programming"
            ],
        },
        "4th Semester": {
            "Computer Engineering": [
                "BCS456A Green IT and Sustainability", "BDSL456C MERN (0:0:2)",
                "BCS456B Capacity Planning for IT", "BCSL456D Technical writing using LATEX (Lab) (0:0:2)"
            ],
            "Electronics and Communication Engineering": [
                "BEC456A Microcontroller Lab", "BEC456C Octave Programming",
                "BEC456B Programmable Logic Controllers",
                "BEC456D Data Structures Lab using C"
            ],
            "Artificial Intelligence and Machine Learning": [
                "BDSL456A Scala (0:0:2)", "BDSL456C MERN (0:0:2)",
                "BDSL456B MangoDB (0:0:2)", "BDSL456D Julia (0:0:2)"
            ],
        },
        "5th Semester": {
            "Computer Engineering": [
            ]
        },
        "6th Semester": {
            "Computer Engineering": [
                "BCE657A UI/UX", "BCE657C Cyber Law",
                "BCE657B Tosca – Automated Software Testing", "BCE657D FOSS"
            ],
            "Electronics and Communication Engineering": [
                "BEC358A LABVIEW programming", "BEC358C C++ Basics",
                "BEC358B MATLAB Programming", "BEC358D IOT for Smart Infrastructure"
            ],
            "Artificial Intelligence and Machine Learning": [
                "BAI657A Explainable AI", "BAI657C Generative AI",
                "BAI657B PyTorch", "BAI657D Devops"
            ],
        },
        "7th Semester": {
            "Computer Engineering": [
            ]
        },
        "8th Semester": {
            "Computer Engineering": [
            ]
        }
    }
    return aec_courses


def app():
    st.title("VTU Ability Enhancement Courses")
    st.header("Select a Semester to View the AECs")

    aec_courses = load_aec_courses()
    semester = st.selectbox("Semester", list(aec_courses.keys()))

    if semester:
        courses = aec_courses[semester]
        st.write(f"Ability Enhancement Courses for {semester}")
        for course in courses:
            df = pd.DataFrame({course: courses[course]})
            st.dataframe(df)
