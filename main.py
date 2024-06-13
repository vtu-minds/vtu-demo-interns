import streamlit as st
from multiapp import MultiApp
import timetable
import aec_courses

app = MultiApp()

# Add all your application here
app.add_app("Timetable", timetable.app)
app.add_app("Ability Enhancement Courses", aec_courses.app)

# The main app
app.run()
