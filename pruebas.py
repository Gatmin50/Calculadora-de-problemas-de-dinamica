import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
import tkinter as tk

def graficar_sinusoidal():
    # Limpiar la figura existente
    plt.clf()

    # Obtener los valores de los controles deslizantes
    longitud_de_onda = np.pi / (longitud_de_onda_slider.get() / 2)
    amplitud = amplitud_slider.get()
    desfase_inicial = desfase_inicial_slider.get()

    # Crear el gráfico con tamaño personalizado
    fig, ax = plt.subplots(figsize=(8, 6))  # Ancho: 8 pulgadas, Alto: 6 pulgadas
    x = np.linspace(0, 10, 1000)
    y = amplitud * np.sin(longitud_de_onda * x + desfase_inicial)
    ax.plot(x, y, label='Ecuación Sinusoidal')

    # Añadir las flechas para la amplitud y la longitud de onda
    ax.plot([(2 * np.pi / longitud_de_onda) / 4, (2 * np.pi / longitud_de_onda) / 4], [0, amplitud], 'r--', label='Amplitud')
    ax.plot([(2 * np.pi / longitud_de_onda) / 4, ((2 * np.pi / longitud_de_onda) / 4) + longitud_de_onda_slider.get()], [amplitud, amplitud], label='Longitud de onda')

    # Añadir etiquetas a los ejes
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()

    # Crear el canvas de matplotlib y añadirlo a la ventana de tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Resto del código sin cambios

# Crear la ventana de tkinter
ventana = tk.Tk()
ventana.geometry('800x600')

# Crear los controles deslizantes
longitud_de_onda_slider = tk.Scale(ventana, from_=0.1, to=10, resolution=0.1, orient='horizontal', label='Longitud de onda')
longitud_de_onda_slider.pack()
amplitud_slider = tk.Scale(ventana, from_=0.1, to=5, resolution=0.1, orient='horizontal', label='Amplitud')
amplitud_slider.pack()
desfase_inicial_slider = tk.Scale(ventana, from_=0, to=2 * np.pi, resolution=0.1, orient='horizontal', label='Desfase inicial')
desfase_inicial_slider.pack()

# Crear el botón que al presionarlo mostrará el gráfico
boton = ctk.CTkButton(master=ventana,
                    text='Graficar',
                    command=graficar_sinusoidal)
boton.pack()

ventana.mainloop()
