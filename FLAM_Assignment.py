import numpy as np
import pandas as pd
from scipy.optimize import least_squares
import matplotlib.pyplot as plt

csv_path = r"C:\Users\AVINASH A\Downloads\xy_data.csv"
data = pd.read_csv(csv_path)

x_values = data.iloc[:, 0].to_numpy()
y_values = data.iloc[:, 1].to_numpy()
n = len(x_values)
t_values = np.linspace(6, 60, n)

def equation(params, t):
    theta, M, X = params
    exp_term = np.exp(M * t)
    s = np.sin(0.3 * t)
    x_pred = t * np.cos(theta) - exp_term * s * np.sin(theta) + X
    y_pred = 42 + t * np.sin(theta) + exp_term * s * np.cos(theta)
    return x_pred, y_pred

def error(params, t, x, y):
    xp, yp = equation(params, t)
    return np.concatenate([xp - x, yp - y])

deg_to_rad = np.pi / 180
bounds_lower = [0, -0.05, 0]
bounds_upper = [50 * deg_to_rad, 0.05, 100]
initial_guess = [0.7, 0.0, 10]

fit = least_squares(error, initial_guess, args=(t_values, x_values, y_values), bounds=(bounds_lower, bounds_upper))
theta, M, X = fit.x

x_fit, y_fit = equation(fit.x, t_values)
L1 = np.sum(np.abs(x_fit - x_values) + np.abs(y_fit - y_values))

print()
print("Estimated values:")
print("Theta (radians):", round(theta, 6))
print("Theta (degrees):", round(theta * 180 / np.pi, 3))
print("M:", round(M, 6))
print("X:", round(X, 6))
print("L1 Distance:", round(L1, 6))
print()

plt.figure(figsize=(8, 5))
plt.scatter(x_values, y_values, s=20, label="Observed")
plt.plot(x_fit, y_fit, color='red', label="Predicted")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Fitted Curve")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

latex = (
    f"\\left( t\\cos({theta:.6f}) - e^{{{M:.6f}t}}\\sin(0.3t)\\sin({theta:.6f}) + {X:.6f}, "
    f"42 + t\\sin({theta:.6f}) + e^{{{M:.6f}t}}\\sin(0.3t)\\cos({theta:.6f}) \\right)"
)

print("LaTeX Equation:")
print(latex)

pd.DataFrame({
    "theta_rad": [theta],
    "theta_deg": [theta * 180 / np.pi],
    "M": [M],
    "X": [X],
    "L1_distance": [L1]
}).to_csv("fitted_params.csv", index=False)
