import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# Define mean and covariance
mu = np.array([0, 4])
sigma = np.array([[1, 0], [0, 1]])

# Create grid and multivariate normal distribution
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))
rv = multivariate_normal(mu, sigma)
Z = rv.pdf(pos)

# Set up the figure and 3D axis
fig = plt.figure(figsize=(12, 5))

# 3D Surface Plot
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('Probability Density')
ax1.set_title('3D Surface Plot')

# 2D Contour Plot
ax2 = fig.add_subplot(1, 2, 2)
contour = ax2.contourf(X, Y, Z, cmap='viridis')
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_title('2D Contour Plot')
fig.colorbar(contour, ax=ax2, shrink=0.8)

plt.suptitle('Multivariate Gaussian (Normal examples)')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
