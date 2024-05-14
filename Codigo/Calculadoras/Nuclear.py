import customtkinter as ctk
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

def calculo_nuclear():
    ventana10 = ctk.CTk()
    ventana10.title("Calculadora ondas armonicas")
    ventana10.geometry('1400x650+400+200')
    ventana10.configure(fg_color="black")
    directorio = 'C:/calculadora_de_dinamica/'
    ruta_local = os.path.join(directorio, 'Plano_inclinado.ico')
    ventana10.iconbitmap(ruta_local)

    # Constantes
    RADIO_ATOMO = 1e-15
    DENSIDAD_NUCLEO = 1.5e18
    CONSTANTE_PLANCK = 6.6e-34

    # Etiquetas
    N0 = ctk.CTkLabel(ventana10, text='N0', text_color='white')
    N0.grid(row=0, column=0, padx=10, pady=10)
    N = ctk.CTkLabel(ventana10, text='N', text_color='white')
    N.grid(row=0, column=2, padx=10, pady=10)
    t_media = ctk.CTkLabel(ventana10, text='Vida media', text_color='white')
    t_media.grid(row=0, column=4, padx=10, pady=10)
    masa_inicial = ctk.CTkLabel(ventana10, text='Masa inicial', text_color='white')
    masa_inicial.grid(row=1, column=0, padx=10, pady=10)
    masa_final1 = ctk.CTkLabel(ventana10, text='Masa final 1', text_color='white')
    masa_final1.grid(row=1, column=2, padx=10, pady=10)
    masa_final2 = ctk.CTkLabel(ventana10, text='Masa final 2', text_color='white')
    masa_final2.grid(row=1, column=4, padx=10, pady=10)
    masa_helio = ctk.CTkLabel(ventana10, text='Masa Helio', text_color='white')
    masa_helio.grid(row=2, column=0, padx=10, pady=10)
    masa_deuterio = ctk.CTkLabel(ventana10, text='Masa Deuterio', text_color='white')
    masa_deuterio.grid(row=2, column=2, padx=10, pady=10)
    masa_tritio = ctk.CTkLabel(ventana10, text='Masa Tritio', text_color='white')
    masa_tritio.grid(row=2, column=4, padx=10, pady=10)
    lambda_ = ctk.CTkLabel(ventana10, text='Landa', text_color='white')
    lambda_.grid(row=3, column=0, padx=10, pady=10)
    
    etiqueta_resultado = ctk.CTkLabel(ventana10, text='', text_color='white')
    etiqueta_resultado.grid(row=6, column=4, columnspan=2, padx=10, pady=10)
    
    etiqueta_resultado1 = ctk.CTkLabel(ventana10, text='', text_color='white')
    etiqueta_resultado1.grid(row=0, column=6, padx=10, pady=10)
    etiqueta_resultado2 = ctk.CTkLabel(ventana10, text='', text_color='white')
    etiqueta_resultado2.grid(row=1, column=6, padx=10, pady=10)
    etiqueta_resultado3 = ctk.CTkLabel(ventana10, text='', text_color='white')
    etiqueta_resultado3.grid(row=2, column=6, padx=10, pady=10)
    etiqueta_resultado4 = ctk.CTkLabel(ventana10, text='', text_color='white')
    etiqueta_resultado4.grid(row=3, column=6, padx=10, pady=10)
    etiqueta_resultado5 = ctk.CTkLabel(ventana10, text='', text_color='white')
    etiqueta_resultado5.grid(row=4, column=6, padx=10, pady=10)
    etiqueta_resultado6 = ctk.CTkLabel(ventana10, text='', text_color='white')
    etiqueta_resultado6.grid(row=5, column=6, padx=10, pady=10)
    etiqueta_resultado7 = ctk.CTkLabel(ventana10, text='', text_color='white')
    etiqueta_resultado7.grid(row=6, column=6, padx=10, pady=10)
    etiqueta_resultado8 = ctk.CTkLabel(ventana10, text='', text_color='white')
    etiqueta_resultado8.grid(row=7, column=6, padx=10, pady=10)
    etiqueta_resultado9 = ctk.CTkLabel(ventana10, text='', text_color='white')
    etiqueta_resultado9.grid(row=8, column=6, padx=10, pady=10)

    # Entradas de datos

    N0 = ctk.CTkEntry(ventana10)
    N0.grid(row=0, column=1, padx=10, pady=10)
    N = ctk.CTkEntry(ventana10)
    N.grid(row=0, column=3, padx=10, pady=10)
    t_media = ctk.CTkEntry(ventana10)
    t_media.grid(row=0, column=5, padx=10, pady=10)
    masa_inicial = ctk.CTkEntry(ventana10)
    masa_inicial.grid(row=1, column=1, padx=10, pady=10)
    masa_final1 = ctk.CTkEntry(ventana10)
    masa_final1.grid(row=1, column=3, padx=10, pady=10)
    masa_final2 = ctk.CTkEntry(ventana10)
    masa_final2.grid(row=1, column=5, padx=10, pady=10)
    masa_helio = ctk.CTkEntry(ventana10)
    masa_helio.grid(row=2, column=1, padx=10, pady=10)
    masa_deuterio = ctk.CTkEntry(ventana10)
    masa_deuterio.grid(row=2, column=3, padx=10, pady=10)
    masa_tritio = ctk.CTkEntry(ventana10)
    masa_tritio.grid(row=2, column=5, padx=10, pady=10)
    lambda_ = ctk.CTkEntry(ventana10)
    lambda_.grid(row=3, column=1, padx=10, pady=10)

    # Funciones

    def calcular_vida_media():
        try:
            t_media = -(math.log(N.get()/N0.get()))
            resultado = round(t_media, 3)
            etiqueta_resultado.configure(text=f"El resultado es {resultado}(s⁻¹)")
            etiqueta_resultado1.configure(text=f"La vida media es \n {resultado}(s⁻¹)")

        except ZeroDivisionError:
            t_media = "N0 debe ser mayor que N"

    def calcular_lambda():
        try:
            lambda_ = 1 / t_media.get()
            resultado = round(lambda_, 3)
            etiqueta_resultado.configure(text=f"El resultado es {resultado}(s⁻¹)")
            etiqueta_resultado2.configure(text=f"La vida media es \n {resultado}(s⁻¹)")

        except ZeroDivisionError:
            lambda_ = "La vida media no puede ser 0"

    def calcular_actividad():
        try:
            A = N.get() * lambda_.get()
            resultado = round(A, 3)
            etiqueta_resultado.configure(text=f"El resultado es {resultado}(s⁻¹)")
            etiqueta_resultado3.configure(text=f"La vida media es \n {resultado}(s⁻¹)")
        
        except TypeError:
            A = "N o lambda no son números válidos"

    def calcular_actividad():
        try:
            energia_fission = (masa_inicial.get() - masa_final1.get() - masa_final2.get()) * 931.5
            resultado = round(energia_fission, 3)
            etiqueta_resultado.configure(text=f"El resultado es {resultado}(J)")
            etiqueta_resultado4.configure(text=f"La vida media es \n {resultado}(J)")
        
        except TypeError:
            energia_fission = "Las masas no son números válidos"

    def calcular_energia_fusion():
        try:
            energia_fusion = (float(masa_deuterio.get()) + float(masa_tritio.get()) - float(masa_helio.get())) * 931.5
        
        except TypeError:
            energia_fusion = "Las masas no son números válidos"

    def graficar():
        # Definir los parámetros de la desintegración
        n01 = float(N0.get())  # Número inicial de núcleos
        lambda_1 = float(lambda_.get())  # Constante de desintegración
        t_half = np.log(2) / lambda_1  # Tiempo de semivida
        t = np.linspace(0, 5*t_half, 1000)  # Tiempo

        # Calcular el número de núcleos en función del tiempo
        N = n01 * np.exp(-lambda_1 * t)

        # Crear el gráfico
        fig, ax = plt.subplots(figsize=(8, 3.3))
        ax.plot(t, N, label='Desintegración nuclear')

        # Añadir las líneas de semivida hasta el punto de intersección
        ax.plot([0, t_half], [n01/2, n01/2], 'r--')
        ax.plot([t_half, t_half], [0, n01/2], 'r--')

        # Marcar el punto de intersección con una 'x'
        ax.plot(t_half, n01/2, 'rx', markersize=5    , label='Semivida')

        # Añadir etiquetas a los ejes
        ax.set_xlabel('Tiempo (s)')
        ax.set_ylabel('Número de núcleos')

        ax.legend('Leyenda')

        # Crear el canvas de matplotlib y añadirlo a la ventana de tkinter
        canvas = FigureCanvasTkAgg(fig, master=ventana10)
        canvas.draw()
        canvas.get_tk_widget().grid(row=6, column=1, padx=10, pady=10, rowspan=5, columnspan=5)

	# Botones
    btn_vida_meia = ctk.CTkButton(ventana10, text="Calcular T1/2", font=("Helvetica", 10, "bold"), command=calcular_vida_media)
    btn_vida_meia.grid(column=0, row=4, padx=10, pady=10)
    btn_landa = ctk.CTkButton(ventana10, text="Calcular λ", font=("Helvetica", 10, "bold"), command=calcular_lambda)
    btn_landa.grid(column=1, row=4, padx=10, pady=10)
    btn_actividad = ctk.CTkButton(ventana10, text="Calcular A", font=("Helvetica", 10, "bold"), command=calcular_actividad)
    btn_actividad.grid(column=2, row=4, padx=10, pady=10)
    btn_número_de_onda = ctk.CTkButton(ventana10, text="Calcular A", font=("Helvetica", 10, "bold"), command=calcular_actividad)
    btn_número_de_onda.grid(column=3, row=4, padx=10, pady=10)
    btn_energia_de_fusion = ctk.CTkButton(ventana10, text="Calcular Ef", font=("Helvetica", 10, "bold"), command=calcular_energia_fusion)
    btn_energia_de_fusion.grid(column=4, row=4, padx=10, pady=10)
    # Crear el botón que al presionarlo mostrará el gráfico
    boton = ctk.CTkButton(master=ventana10, text='Graficar', command=graficar)
    boton.grid(column=5, row=4, padx=10, pady=10)

    def cerrar_ventana():
        ventana10.destroy()

    btn_cerrar = ctk.CTkButton(ventana10, text="Cerrar ventana", font=("Helvetica", 10, "bold"), command=cerrar_ventana, corner_radius=20)
    btn_cerrar.grid(column=4, row=5, padx=10, pady=10)

    # Iniciar el bucle principal de tkinter
    ventana10.mainloop()
