import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from utils.math_utils import jacobian_matrix, solve_equilibrium
from utils.plotting_utils import generate_phase_portrait
import streamlit as st

def pollution_phase_portrait():
    st.title("Pollution Models: Phase Portrait")
    st.write("Explore cascading regime shifts in Pollution Systems.")

    # Parameter sliders
    U1 = st.slider("U1 (Pollution usage 1)", 0.0, 5.0, 0.2, 0.01)
    V1 = st.slider("V1 (Pollution release 1)", 0.0, 5.0, 2.0, 0.1)
    S1 = st.slider("S1 (Pollution supply 1)", 0.0, 1.0, 0.9, 0.01)
    U2 = st.slider("U2 (Pollution usage 2)", 0.0, 5.0, 0.3, 0.01)
    V2 = st.slider("V2 (Pollution release 2)", 0.0, 5.0, 3.0, 0.1)
    S2 = st.slider("S2 (Pollution supply 2)", 0.0, 1.0, 0.95, 0.01)
    alpha1 = st.slider("α1 (Exponent 1)", 2, 10, 5, 1)
    alpha2 = st.slider("α2 (Exponent 2)", 2, 10, 5, 1)
    delta = st.slider("δ (Dispersion factor)", 0.01, 1.0, 0.9, 0.01)
    Z = st.slider("Z (Interaction coefficient)", 0.01, 2.0, 0.6, 0.01)

    # Generate the phase portrait
    st.write("### Phase Portrait")
    fig = generate_phase_portrait(U1, V1, S1, U2, V2, S2, alpha1, alpha2, delta, Z)
    st.pyplot(fig)
