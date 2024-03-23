import numpy as np
import matplotlib.pyplot as plt

# Trapezoidal membership function
def trapezoidal(x, a, b, c, d):
    return np.maximum(0, np.minimum((x - a) / (b - a), 1, (d - x) / (d - c)))

# Triangular membership function
def triangular(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

# Gaussian membership function
def gaussian(x, mean, std):
    return np.exp(-0.5 * ((x - mean) / std) ** 2)

# Example usage
x = np.linspace(0, 10, 100)

trap = trapezoidal(x, 2, 4, 6, 8)
tri = triangular(x, 3, 5, 7)
gauss = gaussian(x, 5, 1)

plt.plot(x, trap, label='Trapezoidal')
plt.plot(x, tri, label='Triangular')
plt.plot(x, gauss, label='Gaussian')
plt.legend()
plt.xlabel('x')
plt.ylabel('Membership')
plt.show()
