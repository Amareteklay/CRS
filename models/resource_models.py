import streamlit as st
from utils.plotting_utils import generate_phase_portrait

def resource_model_page():
    st.title("Resource Models")
    st.write("Explore dynamics of Resource Models under various conditions.")

    # Sub-Level Navigation
    tab1, tab2, tab3 = st.tabs(["Without Dispersion", "With Dispersion", "With Control"])

    with tab1:
        st.subheader("Resource Dynamics Without Dispersion")
        st.write("Section will be updated soon.")

    with tab2:
        st.subheader("Resource Dynamics With Dispersion")
        # Add sliders and plots specific to this case
        st.write("Section will be updated soon.")

    with tab3:
        st.subheader("Resource Dynamics With Control")
        # Add sliders and plots specific to this case
        st.write("Section will be updated soon.")
