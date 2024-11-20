import streamlit as st
from models.pollution_models import pollution_model_page
from models.resource_models import resource_model_page

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Cascading Regime Shifts", layout="wide")

# Load custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state for navigation
if "section" not in st.session_state:
    st.session_state.section = "Welcome"

# Handle navigation using session state
def navigate_to(new_section):
    """Update the current section."""
    st.session_state.section = new_section

# Sidebar Navigation
# Sidebar Navigation with Radio Buttons
with st.sidebar:
    st.title("Navigation")
    section = st.radio(
        "Navigate to:",
        ["Welcome", "Pollution Models", "Resource Models"],
        index=["Welcome", "Pollution Models", "Resource Models"].index(st.session_state.section)
    )
    # Sync sidebar navigation with session state
    if section != st.session_state.section:
        navigate_to(section)



# Welcome Page
if st.session_state.section == "Welcome":
    st.title("Welcome to the Cascading Regime Shifts App")
    st.write("""
        This app explores cascading regime shifts in Pollution and Resource systems.
        Use this tool to visualize dynamics with and without dispersion, and understand
        the effects of control mechanisms on these systems.
    """)
    st.write("""
        You can navigate to different sections of the app using the buttons below.
        Use the sidebar to view, hide, and access different sections of the app.
    """)
    st.write("### Explore Models:")

    # Column buttons for navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Pollution Models"):
            navigate_to("Pollution Models")
    with col2:
        if st.button("Resource Models"):
            navigate_to("Resource Models")

# Pollution Models Page
if st.session_state.section == "Pollution Models":
    st.title("Pollution Models")
    pollution_model_page()

# Resource Models Page
if st.session_state.section == "Resource Models":
    st.title("Resource Models")
    resource_model_page()
