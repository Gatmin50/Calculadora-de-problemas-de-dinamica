import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import math
import turtle

def Circular():
    ventana8 = tk.Tk()
    ventana8.title("Trabajo y energia circular")
    ventana8.geometry('1300x650+100+100')
    ventana8.configure(background='black')

    # Etiquetas
    etiqueta = tk.Label(ventana8, text='No se contempla la friccion con el aire', bg="black", fg="gold")
    etiqueta.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        
    etiqueta_masa = tk.Label(ventana8, text='Masa (kg)', bg="black", fg="white")
    etiqueta_masa.grid(row=1, column=0, padx=10, pady=10)
        
    etiqueta_gravedad = tk.Label(ventana8, text='Gravedad (m/s)', bg="black", fg="white")
    etiqueta_gravedad.grid(row=2, column=0, padx=10, pady=10)

    etiqueta_velocidad_angular = tk.Label(ventana8, text='velocidad angular (rad/s)', bg="black", fg="white")
    etiqueta_velocidad_angular.grid(row=3, column=0, padx=10, pady=10)

    etiqueta_Radio = tk.Label(ventana8, text='Radio (m)', bg="black", fg="white")
    etiqueta_Radio.grid(row=1, column=2, padx=10, pady=10)

    etiqueta_Fuerza = tk.Label(ventana8, text='Fuerza (N)', bg="black", fg="white")
    etiqueta_Fuerza.grid(row=2, column=2, padx=10, pady=10)

    etiqueta_Tiempo = tk.Label(ventana8, text='Tiempo (s)', bg="black", fg="white")
    etiqueta_Tiempo.grid(row=3, column=2, padx=10, pady=10)

    etiqueta_Trabajo = tk.Label(ventana8, text='Trabajo (J)', bg="black", fg="white")
    etiqueta_Trabajo.grid(row=1, column=4, padx=10, pady=10)

    etiqueta_Altura = tk.Label(ventana8, text='Altura (m)', bg="black", fg="white")
    etiqueta_Altura.grid(row=2, column=4, padx=10, pady=10)
        
    etiqueta_resultado = tk.Label(ventana8, text='', bg="black", fg="white")
    etiqueta_resultado.grid(row=5, column=4, columnspan=2, padx=10, pady=10)
        
    etiqueta_resultado1 = tk.Label(ventana8, text='', bg="black", fg="white")
    etiqueta_resultado1.grid(row=1, column=6, padx=10, pady=10)
    etiqueta_resultado2 = tk.Label(ventana8, text='', bg="black", fg="white")
    etiqueta_resultado2.grid(row=2, column=6, padx=10, pady=10)
    etiqueta_resultado3 = tk.Label(ventana8, text='', bg="black", fg="white")
    etiqueta_resultado3.grid(row=3, column=6, padx=10, pady=10)
    etiqueta_resultado4 = tk.Label(ventana8, text='', bg="black", fg="white")
    etiqueta_resultado4.grid(row=4, column=6, padx=10, pady=10)
    etiqueta_resultado5 = tk.Label(ventana8, text='', bg="black", fg="white")
    etiqueta_resultado5.grid(row=5, column=6, padx=10, pady=10)
    etiqueta_resultado6 = tk.Label(ventana8, text='', bg="black", fg="white")
    etiqueta_resultado6.grid(row=6, column=6, padx=10, pady=10)

    #Entradas de datos
    masa = tk.Entry(ventana8)
    masa.grid(row=1, column=1, padx=10, pady=10)
        
    gravedad = tk.Entry(ventana8)
    gravedad.grid(row=2, column=1, padx=10, pady=10)

    velocidad_angular = tk.Entry(ventana8)
    velocidad_angular.grid(row=3, column=1, padx=10, pady=10)

    Radio = tk.Entry(ventana8)
    Radio.grid(row=1, column=3, padx=10, pady=10)

    Fuerza = tk.Entry(ventana8)
    Fuerza.grid(row=2, column=3, padx=10, pady=10)
        
    Tiempo = tk.Entry(ventana8)
    Tiempo.grid(row=3, column=3, padx=10, pady=10)

    Trabajo = tk.Entry(ventana8)
    Trabajo.grid(row=1, column=5, padx=10, pady=10)

    Altura = tk.Entry(ventana8)
    Altura.grid(row=2, column=5, padx=10, pady=10)

    def seleccionar_opcion():
        opcion_seleccionada = combobox.get()
        etiqueta_resultado.config(text="Opción: " + opcion_seleccionada)

        if opcion_seleccionada == "Vuelta completa":
            trabajo_uv()
        elif opcion_seleccionada == "1/4 de vuelta":
            trabajo_uq()
        elif opcion_seleccionada == "Media vuelta":
            trabajo_sv()
        elif opcion_seleccionada == "3/4 de vuelta":
            trabajo_tq()

    opciones = ["Vuelta completa", "1/4 de vuelta", "Media vuelta", "3/4 de vuelta"]
    combobox = ttk.Combobox(ventana8, values=opciones)
    combobox.grid(row=3, column=5, padx=10, pady=10)
    etiqueta_seleccion = tk.Label(ventana8, text="Cantidad de giro:", bg="black", fg="white")
    etiqueta_seleccion.grid(row=3, column=4, padx=10, pady=10)

    def trabajo_uq():

        try:
            f = float(Fuerza.get())
            R = float(Radio.get())
            pi = math.pi
            d = (pi * R)/2
            w = f * d * math.radians(math.cos(pi/2))
            resultado = round(w, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado1.config(text=f"El trabajo del cuerpo es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")
        
    def trabajo_uv():

        try:
            f = float(Fuerza.get())
            R = float(Radio.get())
            pi = math.pi
            d = (pi * R)/2
            w = f * d * math.radians(math.cos(pi * 2))
            resultado = round(w, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado1.config(text=f"El trabajo del cuerpo es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")
        
    def trabajo_tq():

        try:
            f = float(Fuerza.get())
            R = float(Radio.get())
            pi = math.pi
            d = (pi * R)/2
            w = f * d * math.radians(math.cos((3 * pi)/2))
            resultado = round(w, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado1.config(text=f"El trabajo del cuerpo es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def trabajo_sv():

        try:
            f = float(Fuerza.get())
            R = float(Radio.get())
            pi = math.pi
            d = (pi * R)/2
            w = f * d * math.radians(math.cos(pi))
            resultado = round(w, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado1.config(text=f"El trabajo del cuerpo es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")
        
    def potencia():

        try:
            t = float(Tiempo.get())
            w = float(Trabajo.get())
            p = w / t
            resultado = round(p, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(W)")
            etiqueta_resultado2.config(text=f"La potencia es: {resultado}(W)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def momento_de_Inercia():

        try:
            m = float(masa.get())
            R = float(Radio.get())
            R2 = R * R
            I = (1/4) * m * R2
            resultado = round(I, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(Kg·m^2)")
            etiqueta_resultado3.config(text=f"El trabajo del cuerpo es: {resultado}(Kg·m^2)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def energia_cinetica():

        try:
            w = float(velocidad_angular.get())
            w2 = w * w
            m = float(masa.get())
            R = float(Radio.get())
            R2 = R * R
            I = (1/4) * m * R2
            Ec = 0.5 * I * w2
            resultado = round(Ec, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado4.config(text=f"La enegia cinetica es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")
        
    def energia_potencial_gravitatoria():

        try:
            h = float(Altura.get())
            m = float(masa.get())
            g = float(gravedad.get())
            Epg = m * g * h
            resultado = round(Epg, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado5.config(text=f"La enegia potencial es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def energia_mecanica_total():
        try:
            w = float(velocidad_angular.get())
            w2 = w * w
            m = float(masa.get())
            h = float(Altura.get())
            g = float(gravedad.get())
            R = float(Radio.get())
            R2 = R * R
            I = (1/4) * m * R2
            Epg = m * g * h
            Ec = 0.5 * I * w2
            Emt = Epg + Ec
            resultado = round(Emt, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado6.config(text=f"La enegia mecanica total es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def grafico_Circular():
        lienzo_turtle = turtle.ScrolledCanvas(ventana8)
        lienzo_turtle.grid(column=1, row=6, columnspan=4, padx=10, pady=10)

        # Crear un objeto Turtle en el lienzo
        t = turtle.RawTurtle(lienzo_turtle)
    
        t.speed(100)
        t.pencolor('grey')
        t.pensize(5)

        # centro
        t.forward(10)
        t.left(180)
        t.forward(20)
        t.left(180)
        t.forward(10)
        t.left(90)
        t.forward(10)
        t.left(180)
        t.forward(20)
        t.left(180)
        t.forward(10)
        t.right(90)

        # creacion del circulo grande
        t.penup()
        t.forward(200)
        t.left(90)
        t.pendown()
        t.circle(200)

        # masa
        t.pencolor('black')
        t.pensize(4)
        t.circle(40)
        t.penup()
        t.left(90)
        t.forward(40)

        # flechas de fuerzas
        t.pendown()
        t.pencolor('lightgreen')
        t.forward(60)
        t.left(90)
        t.forward(15)
        t.left(180)
        t.left(45)
        t.forward(20)
        t.left(180)
        t.forward(20)
        t.left(180)
        t.right(45)
        t.forward(30)
        t.left(180)
        t.right(45)
        t.forward(20)
        t.left(180)
        t.forward(20)
        t.left(180)
        t.right(45)
        t.left(90)
        t.forward(15)
        t.left(90)
        t.penup()
        t.forward(60)
        t.left(90)
        t.pendown()
        t.pencolor('gold')
        t.left(180)
        t.forward(60)
        t.left(90)
        t.forward(15)
        t.left(180)
        t.left(45)
        t.forward(20)
        t.left(180)
        t.forward(20)
        t.left(180)
        t.right(45)
        t.forward(30)
        t.left(180)
        t.right(45)
        t.forward(20)

        # Esconder el lapiz
        t.hideturtle()

    #Botones
    Calcular_w = tk.Button(ventana8, text="Calcular W", command=lambda:(seleccionar_opcion(), grafico_Circular()), bg="white", fg="black")
    Calcular_w.grid(row=4, column=0, padx=10, pady=10) 
    Calcular_p = tk.Button(ventana8, text="Calcular P", command=potencia, bg="white", fg="black")
    Calcular_p.grid(row=4, column=1, padx=10, pady=10)
    Calcular_I = tk.Button(ventana8, text="Calcular I", command=momento_de_Inercia, bg="white", fg="black")
    Calcular_I.grid(row=4, column=2, padx=10, pady=10)
    Calcular_Ec = tk.Button(ventana8, text="Calcular Ec", command=energia_cinetica, bg="white", fg="black")
    Calcular_Ec.grid(row=4, column=3, padx=10, pady=10)
    Calcular_Epg = tk.Button(ventana8, text="Calcular Epg", command=energia_potencial_gravitatoria, bg="white", fg="black")
    Calcular_Epg.grid(row=4, column=4, padx=10, pady=10)
    Calcular_Emt = tk.Button(ventana8, text="Calcular Emt", command=energia_mecanica_total, bg="white", fg="black")
    Calcular_Emt.grid(row=4, column=5, padx=10, pady=10)

    #Resetear los datos laterales
    def reset_datos():
        etiqueta_resultado1.config(text=f"")
        etiqueta_resultado2.config(text=f"")
        etiqueta_resultado3.config(text=f"")
        etiqueta_resultado4.config(text=f"")
        etiqueta_resultado5.config(text=f"")
        etiqueta_resultado6.config(text=f"")
    btn_cerrar = tk.Button(ventana8, text="Borrar datos laterales", font=("Helvetica", 10, "bold"), command=reset_datos, bg="white", fg="green")
    btn_cerrar.grid(column=3, row=5, padx=10, pady=10)

    # Cerrar la ventana
    def cerrar_ventana8():
        ventana8.destroy()
    btn_cerrar = tk.Button(ventana8, text="      Cerrar ventana      ", font=("Helvetica", 10, "bold"), command=cerrar_ventana8, bg="red", fg="black")
    btn_cerrar.grid(column=2, row=5, columnspan=1, padx=10, pady=10)
