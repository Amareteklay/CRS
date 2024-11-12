import streamlit as st
from models.pollution_models import pollution_phase_portrait

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Pollution Models", "Resource Models", "Control Mechanisms"])

if section == "Pollution Models":
    pollution_phase_portrait()
elif section == "Resource Models":
    st.write("Resource Models will be implemented soon.")
elif section == "Control Mechanisms":
    st.write("Control Mechanisms will be implemented soon.")
