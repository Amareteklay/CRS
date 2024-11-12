import streamlit as st
from models.pollution_models import pollution_phase_portrait

# Configure page layout
st.set_page_config(page_title="Pollution Models App", layout="wide")

# Top Navigation
st.title("Cascading Regime Shifts Dashboard")
navigation = st.selectbox(
    "Navigate to",
    ["Pollution Models", "Resource Models", "Control Mechanisms"],
    key="navigation",
)

# Sidebar for Parameters
with st.sidebar:
    st.header("Adjust Parameters")
    if navigation == "Pollution Models":
        st.subheader("Pollution Models Parameters")
        U1 = st.slider("U1 (Pollution usage 1)", 0.0, 5.0, 0.2, 0.01)
        V1 = st.slider("V1 (Pollution release 1)", 0.0, 5.0, 2.0, 0.1)
        S1 = st.slider("S1 (Pollution supply 1)", 0.0, 1.0, 0.9, 0.01)
        alpha1 = st.slider("α1 (Exponent 1)", 2, 10, 5, 1)
        U2 = st.slider("U2 (Pollution usage 2)", 0.0, 5.0, 0.3, 0.01)
        V2 = st.slider("V2 (Pollution release 2)", 0.0, 5.0, 3.0, 0.1)
        S2 = st.slider("S2 (Pollution supply 2)", 0.0, 1.0, 0.95, 0.01)
        alpha2 = st.slider("α2 (Exponent 2)", 2, 10, 5, 1)
        delta = st.slider("δ (Dispersion factor)", 0.01, 1.0, 0.9, 0.01)
        Z = st.slider("Z (Interaction coefficient)", 0.01, 2.0, 0.6, 0.01)

# Main Content
if navigation == "Pollution Models":
    st.subheader("Pollution Models: Phase Portrait")
    pollution_phase_portrait(U1, V1, S1, U2, V2, S2, alpha1, alpha2, delta, Z)

elif navigation == "Resource Models":
    st.subheader("Resource Models")
    st.write("Resource Models will be implemented soon.")

elif navigation == "Control Mechanisms":
    st.subheader("Control Mechanisms")
    st.write("Control Mechanisms will be implemented soon.")
