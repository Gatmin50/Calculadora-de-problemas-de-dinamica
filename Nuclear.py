import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
import tkinter as tk

def calculadora_nuclear():

    ventana10 = ctk.CTk()
    ventana10.title("Calculadora ondas armonicas")
    ventana10.geometry('1400x650+400+200')
    ventana10.configure(fg_color="black")

    def graficar():
        # Definir los parámetros de la desintegración
        N0 = 3  # Número inicial de núcleos
        lambda_ = 0.1  # Constante de desintegración
        t_half = np.log(2) / lambda_  # Tiempo de semivida
        t = np.linspace(0, 5*t_half, 1000)  # Tiempo

        # Calcular el número de núcleos en función del tiempo
        N = N0 * np.exp(-lambda_ * t)

        # Crear el gráfico
        fig, ax = plt.subplots()
        ax.plot(t, N, label='Desintegración nuclear')

        # Añadir las líneas de semivida hasta el punto de intersección
        ax.plot([0, t_half], [N0/2, N0/2], 'r--')
        ax.plot([t_half, t_half], [0, N0/2], 'r--')

        # Marcar el punto de intersección con una 'x'
        ax.plot(t_half, N0/2, 'rx', markersize=5    , label='Semivida')

        # Añadir etiquetas a los ejes
        ax.set_xlabel('Tiempo (s)')
        ax.set_ylabel('Número de núcleos')

        ax.legend()

        # Crear el canvas de matplotlib y añadirlo a la ventana de tkinter
        canvas = FigureCanvasTkAgg(fig, master=ventana10)
        canvas.draw()
        canvas.get_tk_widget().pack()

    # Crear el botón que al presionarlo mostrará el gráfico
    boton = ctk.CTkButton(master=ventana10, text='Graficar', command=graficar)
    boton.pack()

    # Iniciar el bucle principal de tkinter
    ventana10.mainloop()