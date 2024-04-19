from cgitb import text
import tkinter as tk
import customtkinter as ctk
import os

def electromagnetismo():

    ventana11 = ctk.CTk()
    ventana11.setup(width=1.0, height=1.0)
    ventana11.attributes("-fullscreen", True)
    ventana11.title("Ventana de pantalla completa con barra lateral")
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

    ventana11.mainloop()