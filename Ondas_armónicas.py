import customtkinter as ctk
import math
import plotly.graph_objects as go
import numpy as np
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def ondas_armónicas():

    ventana9 = ctk.CTk()
    ventana9.title("Calculadora ondas armonicas")
    ventana9.geometry('1400x700+400+200')
    ventana9.configure(fg_color="black")

    # Etiquetas
    etiqueta_posición_x = ctk.CTkLabel(ventana9, text='Posicion en x (m)', text_color='white')
    etiqueta_posición_x.grid(row=0, column=0, padx=10, pady=10)
    etiqueta_posición_t = ctk.CTkLabel(ventana9, text='Posicion en t (s)', text_color='white')
    etiqueta_posición_t.grid(row=0, column=2, padx=10, pady=10)
    etiqueta_posición_y = ctk.CTkLabel(ventana9, text='Posicion en y (m)', text_color='white')
    etiqueta_posición_y.grid(row=0, column=4, padx=10, pady=10)
    etiqueta_número_de_onda = ctk.CTkLabel(ventana9, text='número de onda (rad/m)', text_color='white')
    etiqueta_número_de_onda.grid(row=1, column=0, padx=10, pady=10)
    etiqueta_frecuencia_angular = ctk.CTkLabel(ventana9, text='fercuencia angular (rad/s)', text_color='white')
    etiqueta_frecuencia_angular.grid(row=1, column=2, padx=10, pady=10)
    etiqueta_amplitud = ctk.CTkLabel(ventana9, text='amplitud (m)', text_color='white')
    etiqueta_amplitud.grid(row=2, column=0, padx=10, pady=10)
    etiqueta_periodo = ctk.CTkLabel(ventana9, text='Periodo (s)', text_color='white')
    etiqueta_periodo.grid(row=2, column=2, padx=10, pady=10)
    etiqueta_longitud_de_onda = ctk.CTkLabel(ventana9, text='Longitud de onda (m)', text_color='white')
    etiqueta_longitud_de_onda.grid(row=2, column=4, padx=10, pady=10)
    etiqueta_velocidad_propagación = ctk.CTkLabel(ventana9, text='velocidad de propagacion (m/s)', text_color='white')
    etiqueta_velocidad_propagación.grid(row=3, column=2, padx=10, pady=10)
    etiqueta_frecuencia = ctk.CTkLabel(ventana9, text='fercuencia (Hz)', text_color='white')
    etiqueta_frecuencia.grid(row=3, column=4, padx=10, pady=10)
        
    etiqueta_resultado = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado.grid(row=6, column=4, columnspan=2, padx=10, pady=10)
        
    etiqueta_resultado1 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado1.grid(row=0, column=6, padx=10, pady=10)
    etiqueta_resultado2 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado2.grid(row=1, column=6, padx=10, pady=10)
    etiqueta_resultado3 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado3.grid(row=2, column=6, padx=10, pady=10)
    etiqueta_resultado4 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado4.grid(row=3, column=6, padx=10, pady=10)
    etiqueta_resultado5 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado5.grid(row=4, column=6, padx=10, pady=10)
    etiqueta_resultado6 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado6.grid(row=5, column=6, padx=10, pady=10)
    etiqueta_resultado7 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado7.grid(row=6, column=6, padx=10, pady=10)
    etiqueta_resultado8 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado8.grid(row=7, column=6, padx=10, pady=10)
    etiqueta_resultado9 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado9.grid(row=8, column=6, padx=10, pady=10)

    # Entradas de datos

    posición_x = ctk.CTkEntry(ventana9)
    posición_x.grid(row=0, column=1, padx=10, pady=10)
    posición_t = ctk.CTkEntry(ventana9)
    posición_t.grid(row=0, column=3, padx=10, pady=10)
    posición_y = ctk.CTkEntry(ventana9)
    posición_y.grid(row=0, column=5, padx=10, pady=10)
    número_de_onda = ctk.CTkEntry(ventana9)
    número_de_onda.grid(row=1, column=1, padx=10, pady=10)
    frecuencia_angular = ctk.CTkEntry(ventana9)
    frecuencia_angular.grid(row=1, column=3, padx=10, pady=10)
    amplitud = ctk.CTkEntry(ventana9)
    amplitud.grid(row=2, column=1, padx=10, pady=10)
    periodo = ctk.CTkEntry(ventana9)
    periodo.grid(row=2, column=3, padx=10, pady=10)
    longitud_de_onda = ctk.CTkEntry(ventana9)
    longitud_de_onda.grid(row=2, column=5, padx=10, pady=10)
    velocidad_propagación = ctk.CTkEntry(ventana9)
    velocidad_propagación.grid(row=3, column=3, padx=10, pady=10)
    frecuencia = ctk.CTkEntry(ventana9)
    frecuencia.grid(row=3, column=5, padx=10, pady=10)
    pi = math.pi

    # despliege de secciones
    combobox = ctk.CTkComboBox(ventana9, values=["", "0", "π/2", "π", "3π/2"])
    combobox.grid(row=1, column=5, padx=10, pady=10)
    etiqueta_seleccion = ctk.CTkLabel(ventana9, text="Selecciona una opcion:", text_color="white")
    etiqueta_seleccion.grid(row=1, column=4, padx=10, pady=10)

    # Calculos

    def calcular_frecuencia_angular():
        if periodo.get() != "":
            try:
                T = float(periodo.get())
                w = (2*pi)/T
                resultado = round(w, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad/s)")
                etiqueta_resultado1.configure(text=f"La frecuencia angular es \n {resultado}(rad/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de T debe ser numérico")

        elif longitud_de_onda.get() != "":
            try:
                c = float(300000000)
                landa = float(longitud_de_onda.get())
                f = c / landa
                w = 2 * pi * f
                resultado = round(w, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad/s)")
                etiqueta_resultado1.configure(text=f"La frecuencia angular es \n {resultado}(rad/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de landa debe ser numérico")

        elif número_de_onda.get() != "" and velocidad_propagación.get() != "":
            try:
                k = float(número_de_onda)
                Vprop = float(velocidad_propagación.get())
                w = k * Vprop
                resultado = round(w, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad/s)")
                etiqueta_resultado1.configure(text=f"La frecuencia angular es \n {resultado}(rad/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de k y Vprop deben ser numéricos")

        elif frecuencia.get() != "":
            try:
                f = float(frecuencia.get())
                w = 2 * pi * f
                resultado = round(w, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad/s)")
                etiqueta_resultado1.configure(text=f"La frecuencia angular es \n {resultado}(rad/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de f debe ser numérico")
        
        elif número_de_onda.get() != "" and longitud_de_onda.get() != "" and periodo.get() != "":
            try:
                landa = float(longitud_de_onda.get())
                T = float(periodo.get())
                k = float(número_de_onda.get())
                w = (k * landa) / T
                resultado = round(w, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad/s)")
                etiqueta_resultado1.configure(text=f"La frecuencia angular es \n {resultado}(rad/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de k, Vprop y T deben ser numéricos")

        else:
            etiqueta_resultado.configure(text=f"Por favor, introduce al menos un valor")


    def calcular_longitud_onda():
        if frecuencia_angular.get() != "":
            try:
                c = float(300000000)
                w = (frecuencia_angular.get())
                landa = c/w
                resultado = round(landa, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado2.configure(text=f"La logitud de onda es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de ω debe ser numérico")
        
        elif número_de_onda.get() != "":
            try:
                k = float(número_de_onda.get())
                landa = (2*pi) / k
                resultado = round(landa, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado2.configure(text=f"La logitud de onda es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de k debe ser numérico")
        
        elif periodo.get() != "" and velocidad_propagación.get() != "":
            try:
                T = float(periodo.get())
                Vprop = float(velocidad_propagación.get())
                landa = Vprop * T
                resultado = round(landa, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado2.configure(text=f"La logitud de onda es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de T y Vprop deben ser numéricos")
        
        elif periodo.get() != "" and frecuencia_angular.get() != "" and número_de_onda.get() != "": 
            try:
                T = float(periodo.get())
                w = float(frecuencia_angular.get())
                k = float(número_de_onda.get())
                landa = (w*T) / k
                resultado = round(landa, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado2.configure(text=f"La logitud de onda es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de T, ω y k deben ser numéricos")
        
        else:
            etiqueta_resultado.configure(text=f"Por favor, introduce al menos un valor")
        
    def calcular_periodo():
        if frecuencia.get() != "":
            try:
                f = float(frecuencia.get())
                T = 1/f
                resultado = round(T, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(s)")
                etiqueta_resultado3.configure(text=f"El periodo es \n {resultado}(s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de f debe ser numérico")
            
        elif frecuencia_angular.get() != "":
            try:
                w = float(frecuencia_angular.get())
                T = (2*pi) / w
                resultado = round(T, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(s)")
                etiqueta_resultado3.configure(text=f"El periodo es \n {resultado}(s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de ω debe ser numérico")
        
        elif número_de_onda.get() != "" and frecuencia_angular.get() != "" and longitud_de_onda.get() != "": 
            try:
                landa = float(longitud_de_onda.get())
                w = float(frecuencia_angular.get())
                k = float(número_de_onda.get())
                T = (k*landa) / w
                resultado = round(T, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(s)")
                etiqueta_resultado3.configure(text=f"El periodo es \n {resultado}(s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de λ, ω y k deben ser numéricos")
        
        elif velocidad_propagación.get() != "" and longitud_de_onda.get() != "": 
            try:
                landa = float(longitud_de_onda.get())
                Vprop = float(velocidad_propagación.get())
                T = landa / Vprop
                resultado = round(T, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(s)")
                etiqueta_resultado3.configure(text=f"El periodo es \n {resultado}(s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de λ y Vprop deben ser numéricos")
        
        else:
            etiqueta_resultado.configure(text=f"Por favor, introduce al menos un valor")
    
    def calcular_número_de_onda():
        if longitud_de_onda.get() != "":
            try:
                landa = float(longitud_de_onda.get())
                k = (2*pi) / landa
                resultado = round(k, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad/m)")
                etiqueta_resultado4.configure(text=f"El número de onda es \n {resultado}(rad/m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de λ debe ser numérico")
        
        elif velocidad_propagación.get() != "" and frecuencia_angular.get() != "": 
            try:
                w = float(frecuencia_angular.get())
                Vprop = float(velocidad_propagación.get())
                k = w / Vprop
                resultado = round(k, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad/m)")
                etiqueta_resultado4.configure(text=f"El número de onda es \n {resultado}(rad/m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de ω y Vprop deben ser numéricos")
        
        elif periodo.get() != "" and frecuencia_angular.get() != "" and longitud_de_onda.get() != "": 
            try:
                landa = float(longitud_de_onda.get())
                w = float(frecuencia_angular.get())
                T = float(periodo.get())
                k = (w*T) / landa
                resultado = round(k, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad/m)")
                etiqueta_resultado4.configure(text=f"El número de onda es \n {resultado}(rad/m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de λ, ω y T deben ser numéricos")
        
        else:
            etiqueta_resultado.configure(text=f"Por favor, introduce al menos un valor")
    
    def calcular_velocidad_de_propagación():
        if frecuencia_angular.get() != "" and número_de_onda.get() != "":
            try:
                w = float(frecuencia_angular.get())
                k = float(número_de_onda.get())
                Vprop = w / k
                resultado = round(Vprop, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
                etiqueta_resultado5.configure(text=f"La velocidad de propagación es \n {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de k y ω deben ser numéricos")
        
        elif periodo.get() != "" and longitud_de_onda.get() != "":
            try:
                landa = float(longitud_de_onda.get())
                T = float(periodo.get())
                Vprop = landa / T
                resultado = round(Vprop, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
                etiqueta_resultado5.configure(text=f"La velocidad de propagación es \n {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de T y λ deben ser numéricos")
        
        else:
            etiqueta_resultado.configure(text=f"Por favor, introduce al menos un valor")
        
    def calcular_frecuencia():
        if frecuencia_angular.get() != "":
            try:
                w = float(frecuencia_angular.get())
                Vprop = w / (2*pi)
                resultado = round(Vprop, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
                etiqueta_resultado6.configure(text=f"La frecuencia es \n {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de ω debe ser numérico")
        
        elif periodo.get() != "":
            try:
                T = float(periodo.get())
                Vprop = (2*pi) / T
                resultado = round(Vprop, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
                etiqueta_resultado6.configure(text=f"La frecuencia es \n {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de T debe ser numérico")
        
        else:
            etiqueta_resultado.configure(text=f"Por favor, introduce al menos un valor")

    def equación_general():
        if check_var.get() == "si" and número_de_onda.get() != "" and check_var2.get() == "no":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                y = A * math.sin(k*x + w*t + fi)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado7.configure(text=f"La posicion en y es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t y φ deben ser numéricos")

        elif check_var.get() == "si" and periodo.get() != "" and check_var2.get() == "no":
            try:
                A = float(amplitud.get())
                landa = float(longitud_de_onda.get())
                T = float(periodo.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                y = A * math.sin((2*pi) * (x/landa + t/T) + fi)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado7.configure(text=f"La posicion en y es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, λ, T, x, t y φ deben ser numéricos")
        
        elif check_var.get() == "no" and número_de_onda.get() != "" and check_var2.get() == "no":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                y = A * math.sin(k*x - w*t + fi)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado7.configure(text=f"La posicion en y es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t y φ deben ser numéricos")

        elif check_var.get() == "no" and periodo.get() != "" and check_var2.get() == "no":
            try:
                A = float(amplitud.get())
                landa = float(longitud_de_onda.get())
                T = float(periodo.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                y = A * math.sin((2*pi) * (x/landa - t/T) + fi)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado7.configure(text=f"La posicion en y es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, λ, T, x, t y φ deben ser numéricos")

        elif check_var.get() == "si" and número_de_onda.get() != "" and check_var2.get() == "si":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                y = A * math.cos(k*x + w*t + fi)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado7.configure(text=f"La posicion en y es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t y φ deben ser numéricos")

        elif check_var.get() == "si" and periodo.get() != "" and check_var2.get() == "si":
            try:
                A = float(amplitud.get())
                landa = float(longitud_de_onda.get())
                T = float(periodo.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                y = A * math.cos((2*pi) * (x/landa + t/T) + fi)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado7.configure(text=f"La posicion en y es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, λ, T, x, t y φ deben ser numéricos")
        
        elif check_var.get() == "no" and número_de_onda.get() != "" and check_var2.get() == "si":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                y = A * math.cos(k*x - w*t + fi)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado7.configure(text=f"La posicion en y es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t y φ deben ser numéricos")

        elif check_var.get() == "no" and periodo.get() != "" and check_var2.get() == "si":
            try:
                A = float(amplitud.get())
                landa = float(longitud_de_onda.get())
                T = float(periodo.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                y = A * math.cos((2*pi) * (x/landa - t/T) + fi)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m)")
                etiqueta_resultado7.configure(text=f"La posicion en y es \n {resultado}(m)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, λ, T, x, t y φ deben ser numéricos")

        else:
            etiqueta_resultado.configure(text=f"Por favor, introduce al menos un valor")
        
    
    def calcular_combobox():
        if check_var.get() == "si" and número_de_onda.get() != "" and check_var2.get() == "no":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                y = float(combobox.get())
                fi = math.arcsen(y/A) - k*x - w*t
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad)")
                etiqueta_resultado8.configure(text=f"El desfase inicial es \n {resultado}(rad)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t e y deben ser numéricos")

        elif check_var.get() == "si" and periodo.get() != "" and check_var2.get() == "no":
            try:
                A = float(amplitud.get())
                landa = float(longitud_de_onda.get())
                T = float(periodo.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                y = float(combobox.get())
                fi = math.arcsen(y/(A*(2*pi))) -(x/landa) - (t/T)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad)")
                etiqueta_resultado8.configure(text=f"El desfase inicial es \n {resultado}(rad)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, λ, T, x, t e y deben ser numéricos")
        
        elif check_var.get() == "no" and número_de_onda.get() != "" and check_var2.get() == "no":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                y = float(combobox.get())
                fi = math.arcsen(y/A) - k*x + w*t
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad)")
                etiqueta_resultado8.configure(text=f"El desfase inicial es \n {resultado}(rad)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t e y deben ser numéricos")

        elif check_var.get() == "no" and periodo.get() != "" and check_var2.get() == "no":
            try:
                A = float(amplitud.get())
                landa = float(longitud_de_onda.get())
                T = float(periodo.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                y = float(combobox.get())
                fi = math.arcsen(y/(A*(2*pi))) -(x/landa) + (t/T)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad)")
                etiqueta_resultado8.configure(text=f"El desfase inicial es \n {resultado}(rad)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, λ, T, x, t e y deben ser numéricos")

        elif check_var.get() == "si" and número_de_onda.get() != "" and check_var2.get() == "si":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                y = float(combobox.get())
                fi =math.arccos(y/A) - k*x - w*t
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad)")
                etiqueta_resultado8.configure(text=f"El desfase inicial es \n {resultado}(rad)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t e y deben ser numéricos")

        elif check_var.get() == "si" and periodo.get() != "" and check_var2.get() == "si":
            try:
                A = float(amplitud.get())
                landa = float(longitud_de_onda.get())
                T = float(periodo.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                y = float(combobox.get())
                fi =math.arccos(y/(A*(2*pi))) -(x/landa) - (t/T)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad)")
                etiqueta_resultado8.configure(text=f"El desfase inicial es \n {resultado}(rad)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, λ, T, x, t e y deben ser numéricos")
        
        elif check_var.get() == "no" and número_de_onda.get() != "" and check_var2.get() == "si":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                y = float(combobox.get())
                fi =math.arccos(y/A) - k*x + w*t
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad)")
                etiqueta_resultado8.configure(text=f"El desfase inicial es \n {resultado}(rad)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t e y deben ser numéricos")

        elif check_var.get() == "no" and periodo.get() != "" and check_var2.get() == "si":
            try:
                A = float(amplitud.get())
                landa = float(longitud_de_onda.get())
                T = float(periodo.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                y = float(combobox.get())
                fi =math.arccos(y/(A*(2*pi))) -(x/landa) + (t/T)
                resultado = round(y, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(rad)")
                etiqueta_resultado8.configure(text=f"El desfase inicial es \n {resultado}(rad)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, λ, T, x, t y y deben ser numéricos")

        else:
            etiqueta_resultado.configure(text=f"Por favor, introduce al menos un valor")

    def velocidad_y():
        if check_var.get() == "no" and número_de_onda.get() != "" and check_var2.get() == "no":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                vy = A * (-w) * math.cos(k*x - w*t + fi)
                resultado = round(vy, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
                etiqueta_resultado9.configure(text=f"La velocidad en y es \n {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t y φ deben ser numéricos")
        
        elif check_var.get() == "si" and número_de_onda.get() != "" and check_var2.get() == "no":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                vy = A * w * math.cos(k*x + w*t + fi)
                resultado = round(vy, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
                etiqueta_resultado9.configure(text=f"La velocidad en y es \n {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t y φ deben ser numéricos")
        
        if check_var.get() == "no" and número_de_onda.get() != "" and check_var2.get() == "si":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                vy = A * w * math.sin(k*x - w*t + fi)
                resultado = round(vy, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
                etiqueta_resultado9.configure(text=f"La velocidad en y es \n {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t y φ deben ser numéricos")
        
        elif check_var.get() == "si" and número_de_onda.get() != "" and check_var2.get() == "si":
            try:
                A = float(amplitud.get())
                k = float(número_de_onda.get())
                w = float(frecuencia_angular.get())
                x = float(posición_x.get())
                t = float(posición_t.get())
                fi = float(combobox.get())
                vy = A * w * (-math.sin(k*x + w*t + fi))
                resultado = round(vy, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
                etiqueta_resultado9.configure(text=f"La velocidad en y es \n {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de A, k, ω, x, t y φ deben ser numéricos")

        else:
            etiqueta_resultado.configure(text=f"Por favor, introduce al menos un valor")


    def crear_gráfico():
        if check_var2.get() == "no" and combobox.get() == "0":
            # Limpiar la figura existente
            plt.clf()

            # Obtener los valores de los controles deslizantes
            longitud_de_onda2 = np.pi / (float(longitud_de_onda.get()) / 2)
            amplitud2 = float(amplitud.get())
            desfase_inicial2 = 0

            # Crear el gráfico con tamaño personalizado
            fig, ax = plt.subplots(figsize=(8, 3.7))  # Ancho: 8 pulgadas, Alto: 6 pulgadas
            x = np.linspace(0, 10, 1000)
            y = amplitud2 * np.sin(longitud_de_onda2 * x + desfase_inicial2)
            ax.plot(x, y, label='Ecuación Sinusoidal')

            # Añadir las flechas para la amplitud y la longitud de onda
            ax.plot([0,10], [0,0], color='black')
            ax.plot([(2 * np.pi / longitud_de_onda2) / 4, (2 * np.pi / longitud_de_onda2) / 4], [0, amplitud2], 'r--', label='Amplitud')
            ax.plot([(2 * np.pi / longitud_de_onda2) / 4, ((2 * np.pi / longitud_de_onda2) / 4) + float(longitud_de_onda.get())], [amplitud2, amplitud2], label='Longitud de onda', color='yellow')

            # Añadir etiquetas a los ejes
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend(loc='upper right')

            # Crear el canvas de matplotlib y añadirlo a la ventana de tkinter
            canvas = FigureCanvasTkAgg(fig, master=ventana9)
            canvas.draw()
            canvas.get_tk_widget().grid(row=6, column=1, padx=10, pady=10, rowspan=5, columnspan=5)

        elif check_var2.get() == "no" and combobox.get() == "π/2":
            # Limpiar la figura existente
            plt.clf()

            # Obtener los valores de los controles deslizantes
            longitud_de_onda2 = np.pi / (float(longitud_de_onda.get()) / 2)
            amplitud2 = float(amplitud.get())
            desfase_inicial2 = np.pi/2

            # Crear el gráfico con tamaño personalizado
            fig, ax = plt.subplots(figsize=(8, 3.7))  # Ancho: 8 pulgadas, Alto: 6 pulgadas
            x = np.linspace(0, 10, 1000)
            y = amplitud2 * np.sin(longitud_de_onda2 * x + desfase_inicial2)
            ax.plot(x, y, label='Ecuación Sinusoidal')

            # Añadir las flechas para la amplitud y la longitud de onda
            ax.plot([0,10], [0,0], color='black')
            ax.plot([0, 0], [0, amplitud2], 'r--', label='Amplitud')
            ax.plot([0, float(longitud_de_onda.get())], [amplitud2, amplitud2], label='Longitud de onda', color='yellow')

            # Añadir etiquetas a los ejes
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend(loc='upper right')

            # Crear el canvas de matplotlib y añadirlo a la ventana de tkinter
            canvas = FigureCanvasTkAgg(fig, master=ventana9)
            canvas.draw()
            canvas.get_tk_widget().grid(row=6, column=1, padx=10, pady=10, rowspan=5, columnspan=5)

        elif check_var2.get() == "no" and combobox.get() == "π":
            # Limpiar la figura existente
            plt.clf()

            # Obtener los valores de los controles deslizantes
            longitud_de_onda2 = np.pi / (float(longitud_de_onda.get()) / 2)
            amplitud2 = float(amplitud.get())
            desfase_inicial2 = np.pi

            # Crear el gráfico con tamaño personalizado
            fig, ax = plt.subplots(figsize=(8, 3.7))  # Ancho: 8 pulgadas, Alto: 6 pulgadas
            x = np.linspace(0, 10, 1000)
            y = amplitud2 * np.sin(longitud_de_onda2 * x + desfase_inicial2)
            ax.plot(x, y, label='Ecuación Sinusoidal')

            # Añadir las flechas para la amplitud y la longitud de onda
            ax.plot([0,10], [0,0], color='black')
            ax.plot([(2 * np.pi / longitud_de_onda2) / 4, (2 * np.pi / longitud_de_onda2) / 4], [0, -amplitud2], 'r--', label='Amplitud')
            ax.plot([(2 * np.pi / longitud_de_onda2) / 4, ((2 * np.pi / longitud_de_onda2) / 4) + float(longitud_de_onda.get())], [-amplitud2, -amplitud2], label='Longitud de onda', color='yellow')

            # Añadir etiquetas a los ejes
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend(loc='upper right')

            # Crear el canvas de matplotlib y añadirlo a la ventana de tkinter
            canvas = FigureCanvasTkAgg(fig, master=ventana9)
            canvas.draw()
            canvas.get_tk_widget().grid(row=6, column=1, padx=10, pady=10, rowspan=5, columnspan=5)

        elif check_var2.get() == "no" and combobox.get() == "3π/2":
            # Limpiar la figura existente
            plt.clf()

            # Obtener los valores de los controles deslizantes
            longitud_de_onda2 = np.pi / (float(longitud_de_onda.get()) / 2)
            amplitud2 = float(amplitud.get())
            desfase_inicial2 = (3*np.pi)/2

            # Crear el gráfico con tamaño personalizado
            fig, ax = plt.subplots(figsize=(8, 3.7))  # Ancho: 8 pulgadas, Alto: 6 pulgadas
            x = np.linspace(0, 10, 1000)
            y = amplitud2 * np.sin(longitud_de_onda2 * x + desfase_inicial2)
            ax.plot(x, y, label='Ecuación Sinusoidal')

            # Añadir las flechas para la amplitud y la longitud de onda
            ax.plot([0,10], [0,0], color='black')
            ax.plot([0, 0], [0, -amplitud2], 'r--', label='Amplitud')
            ax.plot([0, float(longitud_de_onda.get())], [-amplitud2, -amplitud2], label='Longitud de onda', color='yellow')

            # Añadir etiquetas a los ejes
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend(loc='upper right')

            # Crear el canvas de matplotlib y añadirlo a la ventana de tkinter
            canvas = FigureCanvasTkAgg(fig, master=ventana9)
            canvas.draw()
            canvas.get_tk_widget().grid(row=6, column=1, padx=10, pady=10, rowspan=5, columnspan=5)

        elif check_var2.get() == "si" and combobox.get() == "0":
            # Limpiar la figura existente
            plt.clf()

            # Obtener los valores de los controles deslizantes
            longitud_de_onda2 = np.pi / (float(longitud_de_onda.get()) / 2)
            amplitud2 = float(amplitud.get())
            desfase_inicial2 = 0

            # Crear el gráfico con tamaño personalizado
            fig, ax = plt.subplots(figsize=(8, 3.7))  # Ancho: 8 pulgadas, Alto: 6 pulgadas
            x = np.linspace(0, 10, 1000)
            y = amplitud2 * np.cos(longitud_de_onda2 * x + desfase_inicial2)
            ax.plot(x, y, label='Ecuación Sinusoidal')

            # Añadir las flechas para la amplitud y la longitud de onda
            ax.plot([0,10], [0,0], color='black')
            ax.plot([0, 0], [0, amplitud2], 'r--', label='Amplitud')
            ax.plot([0, float(longitud_de_onda.get())], [amplitud2, amplitud2], label='Longitud de onda', color='yellow')

            # Añadir etiquetas a los ejes
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend(loc='upper right')

            # Crear el canvas de matplotlib y añadirlo a la ventana de tkinter
            canvas = FigureCanvasTkAgg(fig, master=ventana9)
            canvas.draw()
            canvas.get_tk_widget().grid(row=6, column=1, padx=10, pady=10, rowspan=5, columnspan=5)

        elif check_var2.get() == "si" and combobox.get() == "π/2":
            # Limpiar la figura existente
            plt.clf()

            # Obtener los valores de los controles deslizantes
            longitud_de_onda2 = np.pi / (float(longitud_de_onda.get()) / 2)
            amplitud2 = float(amplitud.get())
            desfase_inicial2 = np.pi/2

            # Crear el gráfico con tamaño personalizado
            fig, ax = plt.subplots(figsize=(8, 3.7))  # Ancho: 8 pulgadas, Alto: 6 pulgadas
            x = np.linspace(0, 10, 1000)
            y = amplitud2 * np.cos(longitud_de_onda2 * x + desfase_inicial2)
            ax.plot(x, y, label='Ecuación Sinusoidal')

            # Añadir las flechas para la amplitud y la longitud de onda
            ax.plot([0,10], [0,0], color='black')
            ax.plot([(2 * np.pi / longitud_de_onda2) / 4, (2 * np.pi / longitud_de_onda2) / 4], [0, -amplitud2], 'r--', label='Amplitud')
            ax.plot([(2 * np.pi / longitud_de_onda2) / 4, ((2 * np.pi / longitud_de_onda2) / 4) + float(longitud_de_onda.get())], [-amplitud2, -amplitud2], label='Longitud de onda', color='yellow')

            # Añadir etiquetas a los ejes
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend(loc='upper right')

            # Crear el canvas de matplotlib y añadirlo a la ventana de tkinter
            canvas = FigureCanvasTkAgg(fig, master=ventana9)
            canvas.draw()
            canvas.get_tk_widget().grid(row=6, column=1, padx=10, pady=10, rowspan=5, columnspan=5)

        elif check_var2.get() == "si" and combobox.get() == "π":
            # Limpiar la figura existente
            plt.clf()

            # Obtener los valores de los controles deslizantes
            longitud_de_onda2 = np.pi / (float(longitud_de_onda.get()) / 2)
            amplitud2 = float(amplitud.get())
            desfase_inicial2 = np.pi

            # Crear el gráfico con tamaño personalizado
            fig, ax = plt.subplots(figsize=(8, 3.7))  # Ancho: 8 pulgadas, Alto: 6 pulgadas
            x = np.linspace(0, 10, 1000)
            y = amplitud2 * np.cos(longitud_de_onda2 * x + desfase_inicial2)
            ax.plot(x, y, label='Ecuación Sinusoidal')

            # Añadir las flechas para la amplitud y la longitud de onda
            ax.plot([0,10], [0,0], color='black')
            ax.plot([0, 0], [0, -amplitud2], 'r--', label='Amplitud')
            ax.plot([0, float(longitud_de_onda.get())], [-amplitud2, -amplitud2], label='Longitud de onda', color='yellow')

            # Añadir etiquetas a los ejes
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend(loc='upper right')

            # Crear el canvas de matplotlib y añadirlo a la ventana de tkinter
            canvas = FigureCanvasTkAgg(fig, master=ventana9)
            canvas.draw()
            canvas.get_tk_widget().grid(row=6, column=1, padx=10, pady=10, rowspan=5, columnspan=5)

        elif check_var2.get() == "si" and combobox.get() == "3π/2":
            # Limpiar la figura existente
            plt.clf()

            # Obtener los valores de los controles deslizantes
            longitud_de_onda2 = np.pi / (float(longitud_de_onda.get()) / 2)
            amplitud2 = float(amplitud.get())
            desfase_inicial2 = (3*np.pi)/2

            # Crear el gráfico con tamaño personalizado
            fig, ax = plt.subplots(figsize=(8, 3.7))  # Ancho: 8 pulgadas, Alto: 6 pulgadas
            x = np.linspace(0, 10, 1000)
            y = amplitud2 * np.cos(longitud_de_onda2 * x + desfase_inicial2)
            ax.plot(x, y, label='Ecuación Sinusoidal')

            # Añadir las flechas para la amplitud y la longitud de onda
            ax.plot([0,10], [0,0], color='black')
            ax.plot([(2 * np.pi / longitud_de_onda2) / 4, (2 * np.pi / longitud_de_onda2) / 4], [0, amplitud2], 'r--', label='Amplitud')
            ax.plot([(2 * np.pi / longitud_de_onda2) / 4, ((2 * np.pi / longitud_de_onda2) / 4) + float(longitud_de_onda.get())], [amplitud2, amplitud2], label='Longitud de onda', color='yellow')

            # Añadir etiquetas a los ejes
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend(loc='upper right')

            # Crear el canvas de matplotlib y añadirlo a la ventana de tkinter
            canvas = FigureCanvasTkAgg(fig, master=ventana9)
            canvas.draw()
            canvas.get_tk_widget().grid(row=6, column=1, padx=10, pady=10, rowspan=5, columnspan=5)


    #Resetear los datos laterales
    def reset_datos():
        etiqueta_resultado1.configure(text=f"")
        etiqueta_resultado2.configure(text=f"")
        etiqueta_resultado3.configure(text=f"")
        etiqueta_resultado4.configure(text=f"")
        etiqueta_resultado5.configure(text=f"")
        etiqueta_resultado6.configure(text=f"")
    btn_borrar = ctk.CTkButton(ventana9, text="Borrar datos laterales", font=("Helvetica", 10, "bold"), command=reset_datos)
    btn_borrar.grid(column=4, row=5, padx=10, pady=10)

    #Botones
    btn_frecuencia_angular = ctk.CTkButton(ventana9, text="Calcular ω", font=("Helvetica", 10, "bold"), command=calcular_frecuencia_angular)
    btn_frecuencia_angular.grid(column=4, row=4, padx=10, pady=10)
    btn_longitud_de_onda = ctk.CTkButton(ventana9, text="Calcular λ", font=("Helvetica", 10, "bold"), command=calcular_longitud_onda)
    btn_longitud_de_onda.grid(column=5, row=4, padx=10, pady=10)
    btn_Periodo = ctk.CTkButton(ventana9, text="Calcular T", font=("Helvetica", 10, "bold"), command=calcular_periodo)
    btn_Periodo.grid(column=0, row=5, padx=10, pady=10)
    btn_número_de_onda = ctk.CTkButton(ventana9, text="Calcular k", font=("Helvetica", 10, "bold"), command=calcular_número_de_onda)
    btn_número_de_onda.grid(column=1, row=5, padx=10, pady=10)
    btn_velocidad_de_propagación = ctk.CTkButton(ventana9, text="Calcular Vprop", font=("Helvetica", 10, "bold"), command=calcular_velocidad_de_propagación)
    btn_velocidad_de_propagación.grid(column=0, row=4, padx=10, pady=10)
    btn_frecuencia = ctk.CTkButton(ventana9, text="Calcular f", font=("Helvetica", 10, "bold"), command=calcular_frecuencia)
    btn_frecuencia.grid(column=1, row=4, padx=10, pady=10)
    btn_eq_general = ctk.CTkButton(ventana9, text="Calcular y", font=("Helvetica", 10, "bold"), command=equación_general)
    btn_eq_general.grid(column=2, row=4, padx=10, pady=10)
    btn_combobox = ctk.CTkButton(ventana9, text="Calcular φ", font=("Helvetica", 10, "bold"), command=calcular_combobox)
    btn_combobox.grid(column=3, row=4, padx=10, pady=10)
    btn_velocidad_de_obscilación = ctk.CTkButton(ventana9, text="Calcular Vy", font=("Helvetica", 10, "bold"), command=velocidad_y)
    btn_velocidad_de_obscilación.grid(column=2, row=5, padx=10, pady=10)
    btn_crear_grafico = ctk.CTkButton(ventana9, text="Crear gráfico", font=("Helvetica", 10, "bold"), command=crear_gráfico)
    btn_crear_grafico.grid(column=3, row=5, padx=10, pady=10)

    def checkbox_event():
        etiqueta_resultado.configure(text=f"Orintación hacia la izquierda: {check_var.get()}")

    def checkbox_event2():
        etiqueta_resultado.configure(text=f"Equación en coseno: {check_var2.get()}")

    check_var = ctk.StringVar(value="no")
    checkbox = ctk.CTkCheckBox(ventana9, text="Activar onda hacia la izquierda", text_color='white', command=checkbox_event, variable=check_var, onvalue="si", offvalue="no")
    checkbox.grid(column=0, row=3, padx=20, pady=10)

    check_var2 = ctk.StringVar(value="no")
    checkbox2 = ctk.CTkCheckBox(ventana9, text="Activar equación en coseno", text_color='white', command=checkbox_event2, variable=check_var2, onvalue="si", offvalue="no")
    checkbox2.grid(column=1, row=3, padx=20, pady=10)


    def cerrar_ventana():
        ventana9.destroy()

    btn_cerrar = ctk.CTkButton(ventana9, text="Cerrar ventana", font=("Helvetica", 10, "bold"), command=cerrar_ventana, corner_radius=20)
    btn_cerrar.grid(column=5, row=5, padx=10, pady=10)