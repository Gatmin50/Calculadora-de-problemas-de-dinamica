import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define variables
centro = [0, 0]  # Center of the circle (x, y coordinates)
radio = 3

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate angles for circle outline
theta = np.linspace(0, 2*np.pi, 20)  # 20 points for smooth outline

# Calculate X, Y, and Z coordinates for outline points
x = radio * np.cos(theta) + centro[0]
y = radio * np.sin(theta) + centro[1]
z = np.zeros_like(x)  # Set all Z values to 0 for a flat circle

# Plot the circle outline in 3D
ax.plot(x, y, z, color='purple', linewidth=2)
marca1 = ax.plot3D(centro[0], centro[1] - radio, 0, marker='>', color='purple', markersize=10, label='Campo Mg')
marca2 = ax.plot3D(centro[0], centro[1] + radio, 0, marker='<', color='purple', markersize=10)

ax.plot3D(centro[0], centro[0], 0, marker='^', color='blue', markersize=10)
ax.plot3D([centro[0], centro[0]], [centro[0], centro[1]], [-20, 20],
        color='blue', label='Hilo')

# Set plot limits and labels
ax.set_xlim(-radio-1, radio+1)
ax.set_ylim(-radio-1, radio+1)
ax.set_zlim(-20, 20)  # Set Z limits for a thin circle
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Círculo 3D')

plt.show()