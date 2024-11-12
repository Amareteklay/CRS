import numpy as np
from scipy.optimize import fsolve

def jacobian_matrix(x1, x2, U1, V1, S1, U2, V2, S2, alpha1, alpha2, delta, Z):
    # Compute the Jacobian matrix elements with error handling
    dfx_dx1 = (S1 - V1 * alpha1 * (x1 ** (alpha1 - 1)) / ((1 + x1 ** alpha1) ** 2)) / (delta * Z) + 1
    dfx_dx2 = -1
    dgx_dx1 = -1
    dgx_dx2 = (S2 - V2 * alpha2 * (x2 ** (alpha2 - 1)) / ((1 + x2 ** alpha2) ** 2)) / delta + Z
    return np.array([[dfx_dx1, dfx_dx2], [dgx_dx1, dgx_dx2]])

def solve_equilibrium(U1, V1, S1, U2, V2, S2, alpha1, alpha2, delta, Z):
    def equations(p):
        x1, x2 = p
        fx = (1 / (delta * Z)) * (-U1 + S1 * x1 - V1 * (x1 ** alpha1 / (1 + x1 ** alpha1)) + delta * x1)
        gx = (1 / delta) * (-U2 + S2 * x2 - V2 * (x2 ** alpha2 / (1 + x2 ** alpha2)) + Z * x2)
        return fx, gx

    solution = fsolve(equations, [0.5, 0.5])
    return solution if all(np.isfinite(solution)) else [np.nan, np.nan]
