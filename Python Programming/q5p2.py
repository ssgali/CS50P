import numpy as np
from scipy.optimize import minimize_scalar

# Define the objective function: distance between the point (0, 3) and the parabola y = x^2
def distance(x):
    return np.sqrt((x - 0)**2 + (x**2 - 3)**2)

# Define the constraint function: parabola y = x^2
def parabola_constraint(x):
    return x**2 - 3

# Define the Lagrangian function
def lagrangian(x):
    return distance(x) - lambda_val * parabola_constraint(x)

# Solve using the Lagrange Multipliers Method
# Initialize the Lagrange multiplier
lambda_val = 0.0

# Use minimize_scalar function from scipy.optimize to solve the optimization problem
result = minimize_scalar(lagrangian)

# Extract the solution
x_min = result.x
y_min = x_min**2
min_distance = result.fun

print("Minimum distance:", min_distance)
print("Achieved at point (x, y):", (x_min, y_min))
