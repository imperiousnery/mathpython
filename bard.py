import numpy as np
import matplotlib.pyplot as plt

# Define the number of data points
n = 100

# Generate random real and imaginary parts for the non-trivial zeros
x = np.random.rand(n)
y = np.random.rand(n)

# Define the functions F and G
F = lambda x: b0 + b1*x + b2*x**2 + b3*x**3 + b4*x**4
G = lambda y: c0 + c1*y + c2*y**2 + c3*y**3 + c4*y**4

# Fit the coefficients b0, b1, b2, b3, and b4 of F
b0, b1, b2, b3, b4 = np.linalg.lstsq(x.reshape(-1, 1), F(x).reshape(-1, 1))[0]

# Fit the coefficients c0, c1, c2, c3, and c4 of G
c0, c1, c2, c3, c4 = np.linalg.lstsq(y.reshape(-1, 1), G(y).reshape(-1, 1))[0]

# Plot the data points and the fitted functions
plt.plot(x, F(x), 'r', label='F(x)')
plt.plot(y, G(y), 'b', label='G(y)')
plt.scatter(x, y, s=10, c='g', label='Data points')
plt.xlabel('Real part')
plt.ylabel('Imaginary part')
plt.legend()
plt.show()
