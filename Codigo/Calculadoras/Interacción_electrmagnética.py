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
    #directorio = 'C:/calculadora_de_dinamica/'
    #ruta_local = os.path.join(directorio, 'Interacción_electromagnética.ico')
    #ventana11.iconbitmap(ruta_local)

    # Etiquetas
    etiqueta_intensidad_campo_magnético = ctk.CTkLabel(ventana11, text='Intensidad del \n Campo magnético (T)', text_color='white')
    etiqueta_intensidad_campo_magnético.grid(row=0, column=0, padx=10, pady=10)

    etiqueta_masa_partícula = ctk.CTkLabel(ventana11, text='Masa de la partícula (Kg)', text_color='white')
    etiqueta_masa_partícula.grid(row=0, column=4, padx=10, pady=10)
    etiqueta_posición_inicial_partícula = ctk.CTkLabel(ventana11, text='Posición inicial \n de la Partícula', text_color='white')
    etiqueta_posición_inicial_partícula.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_carga_partícula = ctk.CTkLabel(ventana11, text='Carga de la partícula (C)', text_color='white')
    etiqueta_carga_partícula.grid(row=1, column=4, padx=10, pady=10)
    etiqueta_velocidad_inicial = ctk.CTkLabel(ventana11, text='Velocidad inicial (m/s)', text_color='white')
    etiqueta_velocidad_inicial.grid(row=2, column=0, padx=10, pady=10)

    etiqueta_carga_Periodo = ctk.CTkLabel(ventana11, text='Periodo (s)', text_color='white')
    etiqueta_carga_Periodo.grid(row=2, column=4, padx=10, pady=10)
    etiqueta_posición_campo_magnético = ctk.CTkLabel(ventana11, text='Posición del campo magnético', text_color='white')
    etiqueta_posición_campo_magnético.grid(row=3, column=0, padx=10, pady=10)

        # Etiqueta de Resultado 
    etiqueta_resultado = ctk.CTkLabel(ventana11, text='', text_color='white')
    etiqueta_resultado.grid(row=4, column=4, columnspan=2, padx=10, pady=10)
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
        #Intensidad del campo magnético
    intensidad_CM_X = ctk.CTkEntry(ventana11, placeholder_text='X')
    intensidad_CM_X.grid(row=0, column=1, padx=10, pady=10)
    intensidad_CM_Y = ctk.CTkEntry(ventana11, placeholder_text='Y')
    intensidad_CM_Y.grid(row=0, column=2, padx=10, pady=10)
    intensidad_CM_Z = ctk.CTkEntry(ventana11, placeholder_text='Z')
    intensidad_CM_Z.grid(row=0, column=3, padx=10, pady=10)
        # Masa de la partícula
    masa_partícula = 0
    def seleccionar_opcion(event):
        opcion_seleccionada = combobox.get()
        etiqueta_resultado.configure(text="Opción: " + opcion_seleccionada)
        if opcion_seleccionada == "Protón":
            masa_partícula = 1.6726 * 10^(-27)
        elif opcion_seleccionada == "Electrón":
            masa_partícula = 9.11 * 10^(-31)
        elif opcion_seleccionada == "Positrón":
            masa_partícula = 9.11 * 10^(-31)
        elif opcion_seleccionada == "Pion⁻":
            masa_partícula = 2.2809 * 10^(-28)
        elif opcion_seleccionada == "Pion⁺":
            masa_partícula = 2.2809 * 10^(-28)
        elif opcion_seleccionada == "Muón":
            masa_partícula = 1.867 * 10^(-28)
        elif opcion_seleccionada == "Tauón":
            masa_partícula = 3.167 * 10^(-27)
        elif opcion_seleccionada == "Quark up":
            masa_partícula = 2.3 * 10^(-24)
        elif opcion_seleccionada == "Quark down":
            masa_partícula = 4.8 * 10^(-24)
        elif opcion_seleccionada == "Quark charm":
            masa_partícula = 1.3 * 10^(-23)
        elif opcion_seleccionada == "Quark strange":
            masa_partícula = 1.5 * 10^(-23)
        elif opcion_seleccionada == "Quark top":
            masa_partícula = 173 * 10^(-25)
        elif opcion_seleccionada == "Quark bottom":
            masa_partícula = 4.2 * 10^(-24)
        elif opcion_seleccionada == "Bosón W":
            masa_partícula = 8.69 * 10^(-25)
        elif opcion_seleccionada == "Bosón Z":
            masa_partícula = 9.47 * 10^(-25)
        elif opcion_seleccionada == "Bosón de Higgs / Partícula de dios":
            masa_partícula = 1.25 * 10^(-22)

    combobox = ctk.CTkComboBox(ventana11, values=["", 'Protón', 'Electrón', 'Positrón', 'Pion⁻',
                                                'Pion⁺', 'Muón', 'Tauón', 'Quark up', 
                                                'Quark down', 'Quark charm', 'Quark strange', 
                                                'Quark top', 'Quark bottom', 'Bosón W',
                                                'Bosón Z', 'Bosón de Higgs / Partícula de dios'], command=seleccionar_opcion)
    combobox.grid(row=0, column=5, padx=10, pady=10)

        # Posición Inicial Particula
    posición_P_X = ctk.CTkEntry(ventana11, placeholder_text='X')
    posición_P_X.grid(row=1, column=1, padx=10, pady=10)
    posición_P_Y = ctk.CTkEntry(ventana11, placeholder_text='Y')
    posición_P_Y.grid(row=1, column=2, padx=10, pady=10)
    posición_P_Z = ctk.CTkEntry(ventana11, placeholder_text='Z')
    posición_P_Z.grid(row=1, column=3, padx=10, pady=10)
        # Carga de la particula
    carga_partícula = ctk.CTkEntry(ventana11)
    carga_partícula.grid(row=1, column=5, padx=10, pady=10)
        # Entadas de datos
    velocidad_IX = ctk.CTkEntry(ventana11, placeholder_text='X')
    velocidad_IX.grid(row=2, column=1, padx=10, pady=10)
    velocidad_IY = ctk.CTkEntry(ventana11, placeholder_text='Y')
    velocidad_IY.grid(row=2, column=2, padx=10, pady=10)
    velocidad_IZ = ctk.CTkEntry(ventana11, placeholder_text='Z')
    velocidad_IZ.grid(row=2, column=3, padx=10, pady=10)
        # Posición Campo Magnético
    posición_CM_X = ctk.CTkEntry(ventana11, placeholder_text='X')
    posición_CM_X.grid(row=3, column=1, padx=10, pady=10)
    posición_CM_Y = ctk.CTkEntry(ventana11, placeholder_text='Y')
    posición_CM_Y.grid(row=3, column=2, padx=10, pady=10)
    posición_CM_Z = ctk.CTkEntry(ventana11, placeholder_text='Z')
    posición_CM_Z.grid(row=3, column=3, padx=10, pady=10)
        # Periodo de la particula
    periodo = ctk.CTkEntry(ventana11)
    periodo.grid(row=2, column=5, padx=10, pady=10)

    def calcular_fuerza():
        try:
            # Extracción de valores de las entradas
            carga_part = np.abs(float(carga_partícula.get()))
            velocidad_inicial = np.array([
                float(velocidad_IX.get()),
                float(velocidad_IY.get()),
                float(velocidad_IZ.get())
            ])
            campo_magnetico = np.array([
                float(intensidad_CM_X.get()),
                float(intensidad_CM_Y.get()),
                float(intensidad_CM_Z.get())
            ])

            # Cálculo de la fuerza de Lorentz
            fuerza = np.cross(carga_part * velocidad_inicial, campo_magnetico)
            magnitud_fuerza = np.linalg.norm(fuerza)
            resultado = round(magnitud_fuerza, 3)
            direccion_fuerza = np.arctan2(fuerza[1], fuerza[0]) * 180 / np.pi
            resultado1 = round(direccion_fuerza, 3)

            # Visualización de resultados
            etiqueta_resultado.configure(text=f"Magnitud de la fuerza: {resultado} N")
            etiqueta_resultado1.configure(text=f"Magnitud de la fuerza: {resultado} N")
            etiqueta_resultado2.configure(text=f"Dirección de la fuerza: {resultado1}°")

        except ValueError:
            etiqueta_resultado.configure(text="Error: Valores no válidos.")
    
    def calcular_radio():
        try:
            # Extracción de valores de las entradas
            masa_part = masa_partícula
            carga_part = np.abs(float(carga_partícula.get()))
            velocidad_inicial = np.array([
                float(velocidad_IX.get()),
                float(velocidad_IY.get()),
                float(velocidad_IZ.get())
            ])
            campo_magnetico = np.array([
                float(intensidad_CM_X.get()),
                float(intensidad_CM_Y.get()),
                float(intensidad_CM_Z.get())
            ])

            v = np.linalg.norm(velocidad_inicial)
            B = np.linalg.norm(campo_magnetico)
            r = (masa_part*v)/(carga_part*B)
            resultado = round(r, 3)

            # Visualización de resultados
            etiqueta_resultado.configure(text=f"Magnitud de la fuerza: {resultado} m")
            etiqueta_resultado3.configure(text=f"Magnitud de la fuerza: {resultado} m")

        except ValueError:
            etiqueta_resultado.configure(text="Error: Valores no válidos.")
    
    def calcular_velocidad_angular():
        try:
            # Extracción de valores de las entradas
            masa_part = masa_partícula
            carga_part = np.abs(float(carga_partícula.get()))
            campo_magnetico = np.array([
                float(intensidad_CM_X.get()),
                float(intensidad_CM_Y.get()),
                float(intensidad_CM_Z.get())
            ])

            B = np.linalg.norm(campo_magnetico)
            w = (carga_part/masa_part)*B
            resultado = round(w, 3)

            # Visualización de resultados
            etiqueta_resultado.configure(text=f"Magnitud de la velocidad angular: {resultado} m/s")
            etiqueta_resultado3.configure(text=f"Magnitud de la velocidad angular: {resultado} m/s")

        except ValueError:
            etiqueta_resultado.configure(text="Error: Valores no válidos.")
    
    def calcular_Periodo():
        try:
            # Extracción de valores de las entradas
            masa_part = masa_partícula
            carga_part = np.abs(float(carga_partícula.get()))
            pi = np.pi
            campo_magnetico = np.array([
                float(intensidad_CM_X.get()),
                float(intensidad_CM_Y.get()),
                float(intensidad_CM_Z.get())
            ])

            B = np.linalg.norm(campo_magnetico)
            T = (2*pi*masa_part)/(carga_part*B)
            resultado = round(T, 3)

            # Visualización de resultados
            etiqueta_resultado.configure(text=f"Magnitud del periodo es: {resultado} s")
            etiqueta_resultado3.configure(text=f"Magnitud del periodo es: {resultado} s")

        except ValueError:
            etiqueta_resultado.configure(text="Error: Valores no válidos.")

    def calcular_frecuencia():
        try:
            # Extracción de valores de las entradas
            masa_part = masa_partícula
            carga_part = np.abs(float(carga_partícula.get()))
            T = float(periodo.get())

            pi = np.pi
            campo_magnetico = np.array([
                float(intensidad_CM_X.get()),
                float(intensidad_CM_Y.get()),
                float(intensidad_CM_Z.get())
            ])
            if periodo.get() != ' ':
                B = np.linalg.norm(campo_magnetico)
                f = (carga_part*B)/(2*pi*masa_part)
                resultado = round(f, 3)
            else:
                f = 1/T
                resultado = round(f, 3)

            # Visualización de resultados
            etiqueta_resultado.configure(text=f"Magnitud de la velocidad angular: {resultado} m/s")
            etiqueta_resultado3.configure(text=f"Magnitud de la velocidad angular: {resultado} m/s")

        except ValueError:
            etiqueta_resultado.configure(text="Error: Valores no válidos.")

    def grafico_pajaro():
        # Extracción de valores de las entradas
        #carga_part = np.abs(float(carga_partícula.get()))
        #velocidad_inicial = np.array([
        #    float(velocidad_IX.get()),
        #    float(velocidad_IY.get()),
        #])
        #campo_magnetico = np.array([
        #    float(intensidad_CM_X.get()),
        #    float(intensidad_CM_Y.get()),
        #])

        #fuerza = np.cross(carga_part * velocidad_inicial, campo_magnetico)
        #magnitud_fuerza = np.linalg.norm(fuerza)

        centro1 = [2, -2]  # Coordenadas del centro
        radio1 = 1  # Valor del radio
        centro2 = [2, -7]
        radio2 = 1
        centro3 = [7, -7]
        radio3 = 1
        centro4 = [7, -2]
        radio4 = 1

        # Create the figure and axes
        fig, ax = plt.subplots(figsize=(4, 3))

        plt.title('Vista de pajaro')
        plt.axis('off')
        
        plt.arrow(0, 0, 5, 0, head_width=0.2, head_length=0.5, color='blue')
        plt.arrow(0, 0, 0, -5, head_width=0.2, head_length=0.5, color='red')

        # ax.quiver(0, 0, velocidad_inicial[0], velocidad_inicial[1], scale=magnitud_fuerza/3, headlength=5, headwidth=3, color='green', label='Velocidad inicial')
        # ax.quiver(0, 0, fuerza[0], fuerza[1], scale=magnitud_fuerza, headlength=7, headwidth=3, color='orange', label='Fuerza electromagnética')

        circulo1 = plt.Circle(xy=centro1, radius=radio1, color='black', fill='none', linewidth=0.5)
        ax.add_patch(circulo1)
        plt.plot(2, -2, marker='x', color='white', markersize=15, linewidth=2, alpha=0.7)

        circulo2 = plt.Circle(xy=centro2, radius=radio2, color='black', fill='none', linewidth=0.5)
        ax.add_patch(circulo2)
        plt.plot(2, -7, marker='o', color='white', markersize=15, linewidth=2, alpha=0.7)

        circulo3 = plt.Circle(xy=centro3, radius=radio3, color='black', fill='none', linewidth=0.5)
        ax.add_patch(circulo3)
        plt.plot(7, -7, marker='o', color='white', markersize=15, linewidth=2, alpha=0.7)

        circulo4 = plt.Circle(xy=centro4, radius=radio4, color='black', fill='none', linewidth=0.5)
        ax.add_patch(circulo4)
        plt.plot(7, -2, marker='x', color='white', markersize=15, linewidth=2, alpha=0.7)

        # Create the FigureCanvasTkAgg widget
        canvas = FigureCanvasTkAgg(fig, master=ventana11)
        canvas.draw()

        # Place the canvas in the window
        canvas.get_tk_widget().grid(column=0, row=6, columnspan=3, rowspan=3, padx=10, pady=10)

        # Create a label for the plot
        label_plot = ctk.CTkLabel(ventana11, text="Representación del Campo Magnético")
        label_plot.grid(column=2, row=6, padx=10, pady=10)

    def grafico_3D():
        # Extracción de valores de las entradas
        carga_part = np.abs(float(carga_partícula.get()))
        velocidad_inicial = np.array([
            float(velocidad_IX.get()),
            float(velocidad_IY.get()),
            float(velocidad_IZ.get()),
        ])
        campo_magnetico = np.array([
            float(intensidad_CM_X.get()),
            float(intensidad_CM_Y.get()),
            float(intensidad_CM_Z.get()),
        ])

        fuerza = np.cross(carga_part * velocidad_inicial, campo_magnetico)
        modulo_fuerza = np.linalg.norm(fuerza)

        # Create the figure and axes
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')  # Crea un sub-eje 3D

        plt.title('Vista 3D')
        plt.axis('off')

        longitud_flecha = 3  # Ajusta este valor según sea necesario

        # Calcula las coordenadas del punto final basadas en la longitud y dirección de la flecha
        vi_x_final = velocidad_inicial[0] + longitud_flecha * velocidad_inicial[0] / np.linalg.norm(velocidad_inicial)
        vi_y_final = velocidad_inicial[1] + longitud_flecha * velocidad_inicial[1] / np.linalg.norm(velocidad_inicial)
        vi_z_final = velocidad_inicial[2] + longitud_flecha * velocidad_inicial[2] / np.linalg.norm(velocidad_inicial)

        cm_x_final = campo_magnetico[0] + longitud_flecha * campo_magnetico[0] / np.linalg.norm(campo_magnetico)
        cm_y_final = campo_magnetico[1] + longitud_flecha * campo_magnetico[1] / np.linalg.norm(campo_magnetico)
        cm_z_final = campo_magnetico[2] + longitud_flecha * campo_magnetico[2] / np.linalg.norm(campo_magnetico)

        fuerza_final_x = fuerza[0] + longitud_flecha * modulo_fuerza * fuerza[0] / np.linalg.norm(fuerza)
        fuerza_final_y = fuerza[1] + longitud_flecha * modulo_fuerza * fuerza[1] / np.linalg.norm(fuerza)
        fuerza_final_z = fuerza[2] + longitud_flecha * modulo_fuerza * fuerza[2] / np.linalg.norm(fuerza)

        # Crea flechas con los puntos finales calculados
        ax.quiver(0, 0, 0, vi_x_final, vi_y_final, vi_z_final, head_width=3, color='green', label='Velocidad inicial')
        ax.quiver(0, 0, 0, cm_x_final, cm_y_final, cm_z_final, head_width=3, color='red', label='Campo magnético')
        ax.quiver(0, 0, 0, fuerza_final_x, fuerza_final_y, fuerza_final_z, head_width=5, color='blue', label='Fuerza electromagnética')
        
        # Create the FigureCanvasTkAgg widget
        canvas2 = FigureCanvasTkAgg(fig, master=ventana11)
        canvas2.draw()

        # Place the canvas in the window
        canvas2.get_tk_widget().grid(column=3, row=6, columnspan=3, rowspan=3, padx=10, pady=10)

        # Create a label for the plot
        label_plot1 = ctk.CTkLabel(ventana11, text="Representación del Campo Magnético")
        label_plot1.grid(column=2, row=6, padx=10, pady=10)

    # Botones de calculo
    boton_calcular_fuerza = ctk.CTkButton(ventana11, text="Calcular F", command=calcular_fuerza)
    boton_calcular_fuerza.grid(row=4, column=0)
    boton_calcular_radio = ctk.CTkButton(ventana11, text="Calcular r", command=calcular_radio)
    boton_calcular_radio.grid(row=4, column=1)
    boton_calcular_velocidad_angular = ctk.CTkButton(ventana11, text="Calcular w", command=calcular_velocidad_angular)
    boton_calcular_velocidad_angular.grid(row=4, column=2)
    boton_calcular_periodo = ctk.CTkButton(ventana11, text="Calcular T", command=calcular_Periodo)
    boton_calcular_periodo.grid(row=4, column=3)
    boton_calcular_frecuencia = ctk.CTkButton(ventana11, text="Calcular f", command=calcular_frecuencia)
    boton_calcular_frecuencia.grid(row=4, column=3)
    Crear_gráfico = ctk.CTkButton(ventana11, text="Graficar", command=lambda: (grafico_pajaro(), grafico_3D()))
    Crear_gráfico.grid(row=5, column=1)

    def cerrar_ventana():
        ventana11.destroy()

    btn_cerrar = ctk.CTkButton(ventana11, text="Cerrar ventana", fg_color='red', border_color='grey', font=("Helvetica", 10, "bold"), command=cerrar_ventana, corner_radius=20)
    btn_cerrar.grid(column=2, row=5, padx=10, pady=10, sticky='s')

    ventana11.mainloop()