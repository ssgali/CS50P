import numpy as np
from scipy.optimize import minimize

# Define the objective function f(x, y)
def f(x):
    return x[0]**2 + 4*x[1]**2 - 2*x[0] + 8*x[1]

# Define the constraint function g(x, y)
def constraint(x):
    return x[0] + 2*x[1] - 7

# Define the Lagrangian function L(x, y, λ)
def lagrangian(x):
    return f(x) - lambda_val * constraint(x)

# Define the gradient of the Lagrangian function
def lagrangian_gradient(x):
    grad_f = np.array([2*x[0] - 2, 8*x[1] + 8])
    grad_g = np.array([1, 2])
    return grad_f - lambda_val * grad_g

# Solve using the Lagrange Multipliers Method
# Initialize the Lagrange multiplier
lambda_val = 0.0

# Use minimize function from scipy.optimize to solve the optimization problem
result = minimize(lagrangian, [0, 0], jac=lagrangian_gradient, constraints={'type': 'eq', 'fun': constraint})

# Extract the solution
x_min = result.x
min_value = result.fun

print("Minimum value of f(x, y):", min_value)
print("Achieved at point (x, y):", x_min)