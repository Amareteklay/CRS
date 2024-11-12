import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from utils.math_utils import jacobian_matrix, solve_equilibrium
from utils.plotting_utils import generate_phase_portrait
import streamlit as st

def pollution_phase_portrait(U1, V1, S1, U2, V2, S2, alpha1, alpha2, delta, Z):
    """
    Display phase portrait for Pollution Models with user-defined parameters.
    """
    st.write("Explore cascading regime shifts in pollution systems.")

    # Generate Phase Portrait
    st.write("### Phase Portrait")
    fig = generate_phase_portrait(U1, V1, S1, U2, V2, S2, alpha1, alpha2, delta, Z)
    st.pyplot(fig)
