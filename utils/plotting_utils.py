import matplotlib.pyplot as plt
import numpy as np
from utils.math_utils import solve_equilibrium, jacobian_matrix

def generate_phase_portrait(U1, V1, S1, U2, V2, S2, alpha1, alpha2, delta, Z):
    """
    Generate the phase portrait with nullclines, equilibrium points, and phase vectors.

    Parameters:
    - U1, V1, S1, U2, V2, S2, alpha1, alpha2, delta, Z: System parameters
    """
    # Define the nullclines
    def fx(x1):
        return (1/(delta*Z)) * (-U1 + S1*x1 - V1*(x1**alpha1/(1+x1**alpha1)) + delta*x1)

    def gx(x2):
        return (1/delta) * (-U2 + S2*x2 - V2*(x2**alpha2/ (1+x2**alpha2)) + Z*x2)

    # Derivatives for the vector field
    def dx1_dt(x1, x2):
        return -U1 - S1 * x1 + V1 * (x1 ** alpha1 / (1 + x1 ** alpha1)) + delta * (Z * x2 - x1)

    def dx2_dt(x1, x2):
        return -U2 - S2 * x2 + V2 * (x2 ** alpha2 / (1 + x2 ** alpha2)) + delta * (x1 - Z * x2)

    # Grid for quiver plot
    grid_points = 20
    x1_vals, x2_vals = np.meshgrid(np.linspace(0, 3, grid_points), np.linspace(0, 3, grid_points))

    # Compute derivatives for the vector field
    dx1_dt_vals = dx1_dt(x1_vals, x2_vals)
    dx2_dt_vals = dx2_dt(x1_vals, x2_vals)

    # Compute magnitude of vectors for normalization and color mapping
    magnitude = np.sqrt(dx1_dt_vals**2 + dx2_dt_vals**2)
    magnitude[magnitude == 0] = 1  # Avoid division by zero

    dx1_dt_normalized = dx1_dt_vals / magnitude
    dx2_dt_normalized = dx2_dt_vals / magnitude

    # Equilibrium points
    equilibrium_points = [solve_equilibrium(U1, V1, S1, U2, V2, S2, alpha1, alpha2, delta, Z)]

    # Plotting phase portrait
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot the nullclines
    x_values = np.linspace(0, 5, 1000)
    ax.plot(x_values, fx(x_values), label="Nullcline: fx(x1) = 0", color="green")
    ax.plot(gx(x_values), x_values, label="Nullcline: gx(x2) = 0", color="red")

    # Add quiver plot (vector field)
    quiver = ax.quiver(x1_vals, x2_vals, dx1_dt_normalized, dx2_dt_normalized,
                       magnitude,
                       scale=20,          # Adjusted scale for shorter arrows
                       cmap="viridis",    # Color map to represent magnitude
                       width=0.003,
                       headwidth=3,
                       alpha=0.6)         # Added transparency

    # Add colorbar for vector magnitude
    plt.colorbar(quiver, ax=ax, label="Vector Magnitude")

    # Plot equilibrium points with stability analysis
    for eq in equilibrium_points:
        if np.isnan(eq[0]) or np.isnan(eq[1]):
            continue
        jacobian = jacobian_matrix(eq[0], eq[1], U1, V1, S1, U2, V2, S2, alpha1, alpha2, delta, Z)
        eigenvalues = np.linalg.eigvals(jacobian)
        if np.all(eigenvalues.real < 0):
            stability = "Stable"
            color = "green"
            marker = "o"
        elif np.any(eigenvalues.real > 0) and np.any(eigenvalues.real < 0):
            stability = "Saddle"
            color = "yellow"
            marker = "D"
        else:
            stability = "Unstable"
            color = "red"
            marker = "X"
        ax.scatter(eq[0], eq[1], color=color, marker=marker, label=f"{stability} Point")
        ax.text(eq[0], eq[1], f"{stability}", fontsize=10, ha="center", va="center", color="black")

    # Add labels and legend
    ax.set_title("Phase Portrait with Stability Analysis")
    ax.set_xlabel("X1")
    ax.set_ylabel("X2")
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.axvline(0, color="black", linestyle="--", linewidth=1)
    ax.legend()
    ax.grid(True)

    return fig
