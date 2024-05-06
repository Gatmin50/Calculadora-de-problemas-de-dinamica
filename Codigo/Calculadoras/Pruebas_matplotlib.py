import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Extracción de valores de las entradas
posición_partícula = np.array([2, 5, 10])  # Posición inicial (x, y, z)
posicion_del_campo = np.array([2, 2, 2])
carga_part = 0.1  # Charge of the particle

# Velocity vector (relative to particle position)
vector_velocidad = np.array([7, 0, 0])

# Magnetic field (assumed constant)
intensidad_campoM = np.array([0, 0, 4])

# Calculate force using Lorentz equation
vector_fuerza = carga_part * np.cross(vector_velocidad, intensidad_campoM)

# Scaling factor for arrows
escala_flecha = 0.5

# Plot limits (adjust as needed)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set labels and title
ax.set_title('Vista de pájaro')

ax.plot3D(posición_partícula[0], posición_partícula[1], posición_partícula[2], marker='o', color='green', markersize=10, label='Velocidad')
ax.plot3D(posición_partícula[0], posición_partícula[1], posición_partícula[2], marker='o', color='red', markersize=10, label='Fuerza Mg')
ax.plot3D(posición_partícula[0], posición_partícula[1], posición_partícula[2], marker='o', color='blue', markersize=10, label='Partícula')

# Establecer ancho de la cabeza de la flecha manualmente
head_width = 7  # Ajustar el valor como desees

ax.quiver3D(posición_partícula[0], posición_partícula[1], posición_partícula[2],
            vector_fuerza[0], vector_fuerza[1], vector_fuerza[2],
            length=escala_flecha, color='red')

# Plot velocity vector (modificado)s
ax.quiver3D(posición_partícula[0], posición_partícula[1], posición_partícula[2],
            vector_velocidad[0], vector_velocidad[1], vector_velocidad[2],
            length=escala_flecha, color='green')

# Cálculo de posiciones de la línea
posicion_inicial = np.array([2, 2, 0])  # Posición actual del punto
longitud_linea = 20  # Ajusta este valor para la longitud de la línea
posicion_final = np.array([posicion_inicial[0], posicion_inicial[1], posicion_inicial[2] + longitud_linea])

if intensidad_campoM[2] >= 1:
    # Dibujo de la línea
    ax.plot3D([posicion_inicial[0], posicion_final[0]], [posicion_inicial[1], posicion_final[1]], [posicion_inicial[2], posicion_final[2]],
        color='purple', label='Campo magnético \n dirección +Z')
    ax.plot3D([posicion_inicial[0]*4, posicion_final[0]*4], [posicion_inicial[1], posicion_final[1]], [posicion_inicial[2], posicion_final[2]],
        color='purple')
    ax.plot3D([posicion_inicial[0], posicion_final[0]], [posicion_inicial[1]*4, posicion_final[1]*4], [posicion_inicial[2], posicion_final[2]],
        color='purple')
    ax.plot3D([posicion_inicial[0]*4, posicion_final[0]*4], [posicion_inicial[1]*4, posicion_final[1]*4], [posicion_inicial[2], posicion_final[2]],
        color='purple')
else:
    # Dibujo de la línea
    ax.plot3D([posicion_inicial[0], posicion_final[0]], [posicion_inicial[1], posicion_final[1]], [posicion_inicial[2], posicion_final[2]],
        color='blue', label='Campo magnético \n dirección -Z')
    ax.plot3D([posicion_inicial[0]*4, posicion_final[0]*4], [posicion_inicial[1], posicion_final[1]], [posicion_inicial[2], posicion_final[2]],
        color='blue')
    ax.plot3D([posicion_inicial[0], posicion_final[0]], [posicion_inicial[1]*4, posicion_final[1]*4], [posicion_inicial[2], posicion_final[2]],
        color='blue')
    ax.plot3D([posicion_inicial[0]*4, posicion_final[0]*4], [posicion_inicial[1]*4, posicion_final[1]*4], [posicion_inicial[2], posicion_final[2]],
        color='blue')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend(loc='upper right')

plt.show()