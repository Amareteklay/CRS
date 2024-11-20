import streamlit as st
from utils.plotting_utils import generate_phase_portrait

def pollution_model_page():
    st.title("Pollution Models")
    st.write("Explore dynamics of Pollution Models under various conditions.")

    # Sub-Level Navigation
    tab1, tab2, tab3 = st.tabs(["Without Dispersion", "With Dispersion", "With Control"])

    with tab1:
        st.subheader("Pollution Dynamics Without Dispersion")

        # Create columns: Left for sliders, Right for figure
        left_col, right_col = st.columns([1, 3])  # Adjust the width ratio as needed

        with left_col:
            with st.expander("Adjust Parameters"):
                # Sliders for parameters
                U1 = st.slider("U1", 0.0, 5.0, 0.34, 0.01)
                V1 = st.slider("V1", 0.0, 5.0, 0.8, 0.1)
                S1 = st.slider("S1", 0.0, 1.0, 0.62, 0.01)
                U2 = st.slider("U2", 0.0, 5.0, 0.21, 0.01)
                V2 = st.slider("V2", 0.0, 5.0, 1.6, 0.1)
                S2 = st.slider("S2", 0.0, 1.0, 0.83, 0.01)
                alpha1 = st.slider("alpha1", 2.0, 10.0, 5.0, 1.0)
                alpha2 = st.slider("alpha2", 2.0, 10.0, 5.0, 1.0)
                delta = st.slider("delta", 0.0, 2.0, 0.15, 0.01)
                Z = st.slider("Z", 0.0, 2.0, 0.33, 0.01)

        with right_col:
            # Generate and display the figure
            fig = generate_phase_portrait(U1, V1, S1, U2, V2, S2, alpha1, alpha2, delta, Z)
            st.pyplot(fig)

    with tab2:
        st.subheader("Pollution Dynamics With Dispersion")

        # Create columns for sliders and figure
        left_col, right_col = st.columns([1, 3])

        with left_col:
            # Add sliders specific to this case
            st.write("Parameters specific to Dispersion.")

        with right_col:
            st.write("Figure for Dispersion Dynamics.")
            # Add plot generation code

    with tab3:
        st.subheader("Pollution Dynamics With Control")

        # Create columns for sliders and figure
        left_col, right_col = st.columns([1, 3])

        with left_col:
            # Add sliders specific to control mechanisms
            st.write("Parameters specific to Control.")

        with right_col:
            st.write("Figure for Control Dynamics.")
            # Add plot generation code
