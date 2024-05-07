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

    etiqueta_carga_Periodo = ctk.CTkLabel(ventana11, text='Tipo de gráfico', text_color='white')
    etiqueta_carga_Periodo.grid(row=3, column=4, padx=10, pady=10)

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
        # Periodo de la particula
    periodo = ctk.CTkEntry(ventana11)
    periodo.grid(row=2, column=5, padx=10, pady=10)
        # Posición Campo Magnético
    posición_CM_X = ctk.CTkEntry(ventana11, placeholder_text='X')
    posición_CM_X.grid(row=3, column=1, padx=10, pady=10)
    posición_CM_Y = ctk.CTkEntry(ventana11, placeholder_text='Y')
    posición_CM_Y.grid(row=3, column=2, padx=10, pady=10)
    posición_CM_Z = ctk.CTkEntry(ventana11, placeholder_text='Z')
    posición_CM_Z.grid(row=3, column=3, padx=10, pady=10)
        #Tipo de diagrama
    def seleccionar_opcion():
        opcion_seleccionada = combobox.get()
        etiqueta_resultado.configure(text="Opción: " + opcion_seleccionada)
        if opcion_seleccionada == "Diagrama en vista de pájaro":
            grafico_pajaro()
        elif opcion_seleccionada == "Diagrama 3D":
            grafico_3D()
    
    combobox = ctk.CTkComboBox(ventana11, values=["", 'Diagrama en vista de pájaro', 'Diagrama 3D'])
    combobox.grid(row=3, column=5, padx=10, pady=10)
    

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
        posición_partícula = np.array([2, 5, 0])  # Initial position (x, y, z)
        posicion_del_campo = np.array([2, 2, 0])
        carga_part = float(carga_partícula.get())  # Charge of the particle

        # Velocity vector (relative to particle position)
        vector_velocidad = np.array([
            float(velocidad_IX.get()),
            float(velocidad_IY.get()),
            float(velocidad_IZ.get()),
        ])

        # Magnetic field (assumed constant)
        intensidad_campoM = np.array([
            float(intensidad_CM_X.get()),
            float(intensidad_CM_Y.get()),
            float(intensidad_CM_Z.get()),
        ])

        # Calculate force using Lorentz equation
        vector_fuerza2 = carga_part * np.cross(vector_velocidad, intensidad_campoM)

        # Project force vector onto 2D plane for visualization
        vector_fuerza = vector_fuerza2[:2]  # Extract x and y components

        # Scaling factor for arrows
        escala_flecha = 0.05

        a = intensidad_campoM[2]

        # Plot limits (adjust as needed)
        fig, ax = plt.subplots()

        # Set labels and title
        ax.set_title('Vista de pájaro')
        # Plot particle position
        ax.plot(posición_partícula[0], posición_partícula[1], marker='o', color='green', markersize=10, label='Velocidad')
        ax.plot(posición_partícula[0], posición_partícula[1], marker='o', color='red', markersize=10, label='Fuerza Mg')
        ax.plot(posición_partícula[0], posición_partícula[1], marker='o', color='blue', markersize=10, label='Partícula')

        # Establecer ancho de la cabeza de la flecha manualmente
        head_width = 7  # Ajustar el valor como desees

        posición_partícula_xy = posición_partícula[:2]  # Extract x and y components
        force_tail = posición_partícula_xy
        force_head = force_tail + vector_fuerza
        start_coords = force_tail[0], force_tail[1]
        end_coords = force_head[0], force_head[1]
        ax.annotate("Fuerza", xy=end_coords, xytext=start_coords, size=escala_flecha, 
            arrowprops=dict(facecolor='red', shrink=0.05, linewidth=0.5, headwidth=head_width))

        # Plot velocity vector (modificado)
        velocity_tail = posición_partícula
        velocity_head = velocity_tail + vector_velocidad
        start_coords = velocity_tail[0], velocity_tail[1]
        end_coords = velocity_head[0], velocity_head[1]
        ax.annotate("Velocidad", xy=end_coords, xytext=start_coords, size=escala_flecha, 
            arrowprops=dict(facecolor='green', shrink=0.05, linewidth=0.5, headwidth=head_width))
        # Define magnetic field marker
        magnetic_field_marker = 'o' if a >= 1 else 'x'

        ax.plot(posicion_del_campo[0], posicion_del_campo[1],  marker=magnetic_field_marker, color='purple', markersize=10, label='Campo magnético')
        ax.plot(posicion_del_campo[0]*4, posicion_del_campo[1],  marker=magnetic_field_marker, color='purple', markersize=10)
        ax.plot(posicion_del_campo[0], posicion_del_campo[1]*4,  marker=magnetic_field_marker, color='purple', markersize=10)
        ax.plot(posicion_del_campo[0]*4, posicion_del_campo[1]*4,  marker=magnetic_field_marker, color='purple', markersize=10)

        ax.plot(posicion_del_campo[0], posicion_del_campo[1]*7,  marker=magnetic_field_marker, color='purple', markersize=10)
        ax.plot(posicion_del_campo[0]*7, posicion_del_campo[1],  marker=magnetic_field_marker, color='purple', markersize=10)
        ax.plot(posicion_del_campo[0]*4, posicion_del_campo[1]*7,  marker=magnetic_field_marker, color='purple', markersize=10)
        ax.plot(posicion_del_campo[0]*7, posicion_del_campo[1]*4,  marker=magnetic_field_marker, color='purple', markersize=10)
        ax.plot(posicion_del_campo[0]*7, posicion_del_campo[1]*7,  marker=magnetic_field_marker, color='purple', markersize=10)

        ax.legend(loc='upper right')

        # Create the FigureCanvasTkAgg widget
        canvas = FigureCanvasTkAgg(fig, master=ventana11)
        canvas.draw()

        # Place the canvas in the window
        canvas.get_tk_widget().grid(column=1, row=6, columnspan=3, rowspan=3, padx=10, pady=10)

    def grafico_3D():
        # Extracción de valores de las entradas
        posición_partícula = np.array([2, 5, 10])  # Posición inicial (x, y, z)
        carga_part = float(carga_partícula.get())  # Charge of the particle

        # Velocity vector (relative to particle position)
        vector_velocidad = np.array([
            float(velocidad_IX.get()),
            float(velocidad_IY.get()),
            float(velocidad_IZ.get()),
        ])

        # Magnetic field (assumed constant)
        intensidad_campoM = np.array([
            float(intensidad_CM_X.get()),
            float(intensidad_CM_Y.get()),
            float(intensidad_CM_Z.get()),
        ])

        # Calculate force using Lorentz equation
        vector_fuerza = carga_part * np.cross(vector_velocidad, intensidad_campoM)

        # Scaling factor for arrows
        escala_flecha = 0.5

        # Plot limits (adjust as needed)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Set labels and title
        ax.set_title('Vista tridimensional')

        ax.plot3D(posición_partícula[0], posición_partícula[1], posición_partícula[2], marker='o', color='green', markersize=10, label='Velocidad')
        ax.plot3D(posición_partícula[0], posición_partícula[1], posición_partícula[2], marker='o', color='red', markersize=10, label='Fuerza Mg')
        ax.plot3D(posición_partícula[0], posición_partícula[1], posición_partícula[2], marker='o', color='blue', markersize=10, label='Partícula')

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
        
        # Create the FigureCanvasTkAgg widget
        canvas = FigureCanvasTkAgg(fig, master=ventana11)
        canvas.draw()

        # Place the canvas in the window
        canvas.get_tk_widget().grid(column=1, row=6, columnspan=3, rowspan=3, padx=10, pady=10)

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
    Crear_gráfico = ctk.CTkButton(ventana11, text="Graficar", command=seleccionar_opcion)
    Crear_gráfico.grid(row=5, column=1)

    def cerrar_ventana():
        ventana11.destroy()

    btn_cerrar = ctk.CTkButton(ventana11, text="Cerrar ventana", fg_color='red', border_color='grey', font=("Helvetica", 10, "bold"), command=cerrar_ventana, corner_radius=20)
    btn_cerrar.grid(column=2, row=5, padx=10, pady=10, sticky='s')

    ventana11.mainloop()