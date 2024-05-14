from cgitb import text
import tkinter as tk
import customtkinter as ctk
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

def electromagnetismo():

    ventana11 = ctk.CTk()
    ventana11.title("Menu calculadora de Electromagnetismo")
    screen_width = ventana11.winfo_screenwidth()
    screen_height = ventana11.winfo_screenheight()
    ventana11.geometry(f"{screen_width}x{screen_height}")
    ventana11.configure(fg_color="black")
    directorio = 'C:/calculadora_de_dinamica/'
    ruta_local = os.path.join(directorio, 'Interacción_electromagnética.ico')
    ventana11.iconbitmap(ruta_local)

    # Etiquetas
    etiqueta_masa_partícula = ctk.CTkLabel(ventana11, text='Masa de la partícula (?)', text_color='white')
    etiqueta_masa_partícula.grid(row=0, column=0, padx=10, pady=10)
    etiqueta_carga_partícula = ctk.CTkLabel(ventana11, text='Carga de la partícula (?)', text_color='white')
    etiqueta_carga_partícula.grid(row=0, column=2, padx=10, pady=10)
    etiqueta_intensidad_campo_magnético = ctk.CTkLabel(ventana11, text='Intensidad del \n Campo magnético (T)', text_color='white')
    etiqueta_intensidad_campo_magnético.grid(row=0, column=4, padx=10, pady=10)
    etiqueta_posición_inicial_partícula = ctk.CTkLabel(ventana11, text='Posición inicial \n de la Partícula', text_color='white')
    etiqueta_posición_inicial_partícula.grid(row=1, column=0, padx=10, pady=10)
    etiqueta_velocidad_inicial = ctk.CTkLabel(ventana11, text='Velocidad inicial (m/s)', text_color='white')
    etiqueta_velocidad_inicial.grid(row=1, column=4, padx=10, pady=10)
    etiqueta_posición_campo_magnético = ctk.CTkLabel(ventana11, text='Posición del campo magnético', text_color='white')
    etiqueta_posición_campo_magnético.grid(row=2, column=0, padx=10, pady=10)

        # Etiqueta de Resultado 
    etiqueta_resultado = ctk.CTkLabel(ventana11, text='', text_color='white')
    etiqueta_resultado.grid(row=6, column=4, columnspan=2, padx=10, pady=10)
        # Etiquetas de almacenamiento de resultados
    etiqueta_resultado1 = ctk.CTkLabel(ventana11, text='', text_color='white')
    etiqueta_resultado1.grid(row=0, column=6, padx=10, pady=10)
    etiqueta_resultado2 = ctk.CTkLabel(ventana11, text='', text_color='white')
    etiqueta_resultado2.grid(row=1, column=6, padx=10, pady=10)
    etiqueta_resultado3 = ctk.CTkLabel(ventana11, text='', text_color='white')
    etiqueta_resultado3.grid(row=2, column=6, padx=10, pady=10)
    etiqueta_resultado4 = ctk.CTkLabel(ventana11, text='', text_color='white')
    etiqueta_resultado4.grid(row=3, column=6, padx=10, pady=10)
    etiqueta_resultado5 = ctk.CTkLabel(ventana11, text='', text_color='white')
    etiqueta_resultado5.grid(row=4, column=6, padx=10, pady=10)
    etiqueta_resultado6 = ctk.CTkLabel(ventana11, text='', text_color='white')
    etiqueta_resultado6.grid(row=5, column=6, padx=10, pady=10)
    etiqueta_resultado7 = ctk.CTkLabel(ventana11, text='', text_color='white')
    etiqueta_resultado7.grid(row=6, column=6, padx=10, pady=10)
    etiqueta_resultado8 = ctk.CTkLabel(ventana11, text='', text_color='white')
    etiqueta_resultado8.grid(row=7, column=6, padx=10, pady=10)
    etiqueta_resultado9 = ctk.CTkLabel(ventana11, text='', text_color='white')
    etiqueta_resultado9.grid(row=8, column=6, padx=10, pady=10)

    # Entadas de datos
    masa_partícula = ctk.CTkEntry(ventana11)
    masa_partícula.grid(row=0, column=1, padx=10, pady=10)
    carga_partícula = ctk.CTkEntry(ventana11)
    carga_partícula.grid(row=0, column=3, padx=10, pady=10)
    intensidad_CM = ctk.CTkEntry(ventana11)
    intensidad_CM.grid(row=0, column=5, padx=10, pady=10)
        # Posición Inicial Particula
    posición_P_X = ctk.CTkEntry(ventana11, placeholder_text='X')
    posición_P_X.grid(row=1, column=1, padx=10, pady=10)
    posición_P_Y = ctk.CTkEntry(ventana11, placeholder_text='Y')
    posición_P_Y.grid(row=1, column=2, padx=10, pady=10)
    posición_P_Z = ctk.CTkEntry(ventana11, placeholder_text='Z')
    posición_P_Z.grid(row=1, column=3, padx=10, pady=10)
        # Entadas de datos
    velocidad_IP = ctk.CTkEntry(ventana11)
    velocidad_IP.grid(row=1, column=5, padx=10, pady=10)
        # Posición Campo Magnético
    posición_CM_X = ctk.CTkEntry(ventana11, placeholder_text='X')
    posición_CM_X.grid(row=2, column=1, padx=10, pady=10)
    posición_CM_Y = ctk.CTkEntry(ventana11, placeholder_text='Y')
    posición_CM_Y.grid(row=2, column=2, padx=10, pady=10)
    posición_CM_Z = ctk.CTkEntry(ventana11, placeholder_text='Z')
    posición_CM_Z.grid(row=2, column=3, padx=10, pady=10)

    # Definir parámetros
    masa = masa_partícula.get()
    carga = carga_partícula.get()
    posicion_campo_magnetico = np.array([posición_CM_X.get(), posición_CM_Y.get(), posición_CM_Z.get()])
    campo_magnetico = np.array([0.0, intensidad_CM.get(), 0.0])
    posicion_inicial = np.array([posición_P_X.get(), posición_P_Y.get(), posición_P_Z.get()])
    velocidad_inicial = np.array([50.0, 80.0, 0.0])
    tiempo_final = 10.0
    paso_temporal = 0.001

    # Definir funciones
    def distancia(posicion1, posicion2):
        return np.linalg.norm(posicion1 - posicion2)

    def fuerza(posicion):
        r_cm = posicion - posicion_campo_magnetico
        fuerza_magnetica = np.cross(velocidad_inicial, campo_magnetico) * carga
        # Calcular la fuerza magnÃ©tica en funciÃ³n de la distancia
        fuerza_magnetica = fuerza_magnetica / np.linalg.norm(r_cm)**2
        return fuerza_magnetica

    def aceleracion(posicion):
        r_cm = posicion - posicion_campo_magnetico
        a = fuerza(posicion) / masa
        return a

    def gráfico():
        
        def simular_movimiento():
            posiciones = []
            velocidades = []

            posicion = posicion_inicial
            velocidad = velocidad_inicial
            tiempo = 0.0

            while tiempo < tiempo_final:
                a = aceleracion(posicion)
                v_nueva = velocidad + a * paso_temporal
                p_nueva = posicion + v_nueva * paso_temporal

                # Evitar divisiÃ³n por cero en el cÃ¡lculo de la fuerza magnÃ©tica
                if np.linalg.norm(posicion - posicion_campo_magnetico) > 0:
                    posiciones.ventana11end(p_nueva)
                    velocidades.ventana11end(v_nueva)
                else:
                    print("Error: La partÃ­cula estÃ¡ demasiado cerca del campo magnÃ©tico.")
                    break

            tiempo += paso_temporal

            posicion = p_nueva
            velocidad = v_nueva

            return np.array(posiciones), np.array(velocidades)

        # Simular el movimiento de la partÃ­cula
        try:
            posiciones, velocidades = simular_movimiento()
        except Exception as e:
            print(f"Error durante la simulaciÃ³n: {e}")
            posiciones = []
            velocidades = []

        # Definir variables para colores
        color_particula = "green" if carga > 0 else "purple"
        color_campo_magnetico = "red" if campo_magnetico[0] > 0 else "blue"

        # Crear lienzo para la visualizaciÃ³n 3D
        lienzo = ctk.CTkFrame(ventana11, width=400, height=300)
        lienzo.grid(row=5, column=0, rowspan=2)

        # Crear marco para controles
        marco_controles = ctk.CTkFrame(ventana11)
        marco_controles.grid(row=5, column=3, padx=10, pady=10)

        # FunciÃ³n para iniciar la simulaciÃ³n
        def iniciar_simulacion():
            global simulando, tiempo_actualizado
            simulando = True
            boton_inicio.configure(state="disabled")
            tiempo_actualizado = 0.0  # Tiempo inicial para la animaciÃ³n
            actualizar_visualizacion_animada()

        iniciar_simulacion()

        # Función para actualizar la visualizaciÃ³n con animaciÃ³n
        def actualizar_visualizacion_animada():
            global simulando, fig, ax, line_particle, line_field, tiempo_actualizado

            if not simulando or not posiciones.any() or not velocidades.any():
                return

            # Actualizar tiempo simulado
            tiempo_actualizado += paso_temporal

            # Calcular la posiciÃ³n de la partÃ­cula en el tiempo actual
            if simulando:
                a = aceleracion(posiciones[-1])
                v_nueva = velocidades[-1] + a * paso_temporal
                p_nueva = posiciones[-1] + v_nueva * paso_temporal
                posiciones = np.ventana11end(posiciones, [p_nueva], axis=0)
                velocidades = np.ventana11end(velocidades, [v_nueva], axis=0)

            # Actualizar datos en el grÃ¡fico
            line_particle.set_data_3d(posiciones[:, 0], posiciones[:, 1], posiciones[:, 2])
            line_field.set_data_3d(puntos_campo[:, 0] + posicion_campo_magnetico[0], puntos_campo[:, 1] + posicion_campo_magnetico[1], puntos_campo[:, 2] + posicion_campo_magnetico[2],)

            # Simular siguiente paso si la simulaciÃ³n estÃ¡ activa
            if simulando:
                ventana11.after(int(paso_temporal * 1000), actualizar_visualizacion_animada)

        # Crear figura y ejes 3D
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')

        # Crear lÃ­neas para la trayectoria de la partÃ­cula y el campo magnÃ©tico
        line_particle, = ax.plot(
            [], [], [], marker="o", markersize=5, markerfacecolor=color_particula, linestyle="-"
        )
        line_field, = ax.plot(
            [], [], [], marker="", linestyle="-", linewidth=2, color=color_campo_magnetico
        )

        # Establecer las etiquetas y el tÃ­tulo
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('SimulaciÃ³n de interacciÃ³n magnÃ©tica')
        ax.view_init(elev=15, azim=45)
        # Agregar leyenda
        ax.legend()

        # Mostrar el grÃ¡fico en el lienzo
        canvas = FigureCanvasTkAgg(fig, master=ventana11)  
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    boton_inicio = ctk.CTkButton(ventana11, text="Iniciar", command=gráfico)
    boton_inicio.grid(row=3, column=0)

    ventana11.mainloop()