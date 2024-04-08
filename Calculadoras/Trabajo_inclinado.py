import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import math
import turtle

def Inclinado():
    ventana7 = tk.Tk()
    ventana7.title("Trabajo y energia inclinado")
    ventana7.geometry('1300x650+100+100')
    ventana7.configure(background='black')

    # Etiquetas
    etiqueta = tk.Label(ventana7, text='No se contempla la friccion con el aire', bg="black", fg="gold")
    etiqueta.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        
    etiqueta_masa = tk.Label(ventana7, text='Masa (kg)', bg="black", fg="white")
    etiqueta_masa.grid(row=1, column=0, padx=10, pady=10)
        
    etiqueta_gravedad = tk.Label(ventana7, text='Gravedad (m/s)', bg="black", fg="white")
    etiqueta_gravedad.grid(row=2, column=0, padx=10, pady=10)

    etiqueta_velocidad = tk.Label(ventana7, text='velocidad (m/s)', bg="black", fg="white")
    etiqueta_velocidad.grid(row=3, column=0, padx=10, pady=10)

    etiqueta_distancia = tk.Label(ventana7, text='Distancia (m)', bg="black", fg="white")
    etiqueta_distancia.grid(row=1, column=2, padx=10, pady=10)

    etiqueta_Fuerza = tk.Label(ventana7, text='Fuerza (N)', bg="black", fg="white")
    etiqueta_Fuerza.grid(row=2, column=2, padx=10, pady=10)

    etiqueta_Tiempo = tk.Label(ventana7, text='Tiempo (s)', bg="black", fg="white")
    etiqueta_Tiempo.grid(row=3, column=2, padx=10, pady=10)

    etiqueta_Trabajo = tk.Label(ventana7, text='Trabajo (J)', bg="black", fg="white")
    etiqueta_Trabajo.grid(row=1, column=4, padx=10, pady=10)

    etiqueta_Altura = tk.Label(ventana7, text='Altura (m)', bg="black", fg="white")
    etiqueta_Altura.grid(row=2, column=4, padx=10, pady=10)

    etiqueta_inclinacion_del_plano = tk.Label(ventana7, text='Inclinacion del \n plano', bg="black", fg="white")
    etiqueta_inclinacion_del_plano.grid(row=3, column=4, padx=10, pady=10)
        
    etiqueta_resultado = tk.Label(ventana7, text='', bg="black", fg="white")
    etiqueta_resultado.grid(row=5, column=4, columnspan=2, padx=10, pady=10)
        
    etiqueta_resultado1 = tk.Label(ventana7, text='', bg="black", fg="white")
    etiqueta_resultado1.grid(row=4, column=6, padx=10, pady=10)
    etiqueta_resultado2 = tk.Label(ventana7, text='', bg="black", fg="white")
    etiqueta_resultado2.grid(row=5, column=6, padx=10, pady=10)
    etiqueta_resultado3 = tk.Label(ventana7, text='', bg="black", fg="white")
    etiqueta_resultado3.grid(row=6, column=6, padx=10, pady=10)
    etiqueta_resultado4 = tk.Label(ventana7, text='', bg="black", fg="white")
    etiqueta_resultado4.grid(row=7, column=6, padx=10, pady=10)
    etiqueta_resultado5 = tk.Label(ventana7, text='', bg="black", fg="white")
    etiqueta_resultado5.grid(row=8, column=6, padx=10, pady=10)

    #Entradas de datos
    masa = tk.Entry(ventana7)
    masa.grid(row=1, column=1, padx=10, pady=10)
        
    gravedad = tk.Entry(ventana7)
    gravedad.grid(row=2, column=1, padx=10, pady=10)

    velocidad = tk.Entry(ventana7)
    velocidad.grid(row=3, column=1, padx=10, pady=10)

    distancia = tk.Entry(ventana7)
    distancia.grid(row=1, column=3, padx=10, pady=10)

    Fuerza = tk.Entry(ventana7)
    Fuerza.grid(row=2, column=3, padx=10, pady=10)
        
    Tiempo = tk.Entry(ventana7)
    Tiempo.grid(row=3, column=3, padx=10, pady=10)

    Trabajo = tk.Entry(ventana7)
    Trabajo.grid(row=1, column=5, padx=10, pady=10)

    Altura = tk.Entry(ventana7)
    Altura.grid(row=2, column=5, padx=10, pady=10)

    inclinacion_del_plano = tk.Entry(ventana7)
    inclinacion_del_plano.grid(row=3, column=5, padx=10, pady=10)

    def trabajo():

        try:
            f = float(Fuerza.get())
            d = float(distancia.get())
            i = float(inclinacion_del_plano.get())
            w = f * d * math.radians(math.cos(i))
            resultado = round(w, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado1.config(text=f"El trabajo del cuerpo es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def energia_cinetica():

        try:
            v = float(velocidad.get())
            v2 = v * v
            m = float(masa.get())
            Ec = 0.5 * m * v2
            resultado = round(Ec, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado2.config(text=f"La enegia cinetica es: {resultado}(J)")
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
            etiqueta_resultado3.config(text=f"La enegia potencial es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def energia_mecanica_total():

        try:
            v = float(velocidad.get())
            v2 = v * v
            m = float(masa.get())
            h = float(Altura.get())
            g = float(gravedad.get())
            Epg = m * g * h
            Ec = 0.5 * m * v2
            Emt = Epg + Ec
            resultado = round(Emt, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado4.config(text=f"La enegia mecanica total es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")
        
    def potencia():

        try:
            t = float(Tiempo.get())
            w = float(Trabajo.get())
            p = w / t
            resultado = round(p, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(W)")
            etiqueta_resultado5.config(text=f"La potencia es: {resultado}(W)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def grafico_triangulo():
        lienzo_turtle = turtle.ScrolledCanvas(ventana7)
        lienzo_turtle.grid(column=1, row=6, columnspan=4, padx=10, pady=10)
        # Crear un objeto Turtle en el lienzo
        t = turtle.RawTurtle(lienzo_turtle)

        a3 = float(inclinacion_del_plano.get())
        # Pide los ángulos de los dos ángulos desconocidos
        a2 = - a3 - 90

        cc = math.cos(math.radians(a3)) * 300
        co = math.cos(math.radians(a2)) * 300

        # Configura la tortuga
        t.speed(100)

        # Definir el tamaño de la línea y el color
        t.pensize(7)
        t.pencolor('black')

        t.penup()
        t.setpos(-50, -100)
        t.pendown()

        # Dibuja el triángulo rectángulo
        t.left(a3)
        t.forward(50)
        t.forward(250)
        t.left(a2)
        t.backward(co)

        # Angulo de 90º
        t.pensize(3)
        t.pencolor('red')

        t.left(90)
        t.backward(30)
        t.left(90)
        t.forward(30)
        t.left(90)
        t.backward(30)

        # Dibuja el triángulo rectángulo
        t.pensize(7)
        t.pencolor('black')
        t.left(90)
        t.forward(30)
        t.left(90)
        t.backward(cc)
        t.left(a3)
        t.forward(260)
        t.left(90)

        # Cuerpo
        t.penup()
        t.forward(30)
        t.right(90)
        t.forward(30)
        t.pensize(5)
        t.pencolor('grey')
        t.pendown()
        t.left(90)
        t.circle(30)
        t.left(90)
        t.penup()
        t.forward(30)

        # Flecha de la fuerza
        t.pendown()
        t.pencolor('lightgreen')
        t.forward(50)
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
    Calcular_w = tk.Button(ventana7, text="Calcular W", command=lambda:(trabajo(), grafico_triangulo()), bg="white", fg="black")
    Calcular_w.grid(row=4, column=0, padx=10, pady=10) 
    Calcular_p = tk.Button(ventana7, text="Calcular P", command=potencia, bg="white", fg="black")
    Calcular_p.grid(row=4, column=1, padx=10, pady=10)  
    Calcular_Ec = tk.Button(ventana7, text="Calcular Ec", command=energia_cinetica, bg="white", fg="black")
    Calcular_Ec.grid(row=4, column=2, padx=10, pady=10)
    Calcular_Epg = tk.Button(ventana7, text="Calcular Epg", command=energia_potencial_gravitatoria, bg="white", fg="black")
    Calcular_Epg.grid(row=4, column=3, padx=10, pady=10)
    Calcular_Emt = tk.Button(ventana7, text="Calcular Emt", command=energia_mecanica_total, bg="white", fg="black")
    Calcular_Emt.grid(row=4, column=4, padx=10, pady=10)

    #Resetear los datos laterales
    def reset_datos():
        etiqueta_resultado1.config(text=f"")
        etiqueta_resultado2.config(text=f"")
        etiqueta_resultado3.config(text=f"")
        etiqueta_resultado4.config(text=f"")
        etiqueta_resultado5.config(text=f"")
    btn_cerrar = tk.Button(ventana7, text="Borrar datos laterales", font=("Helvetica", 10, "bold"), command=reset_datos, bg="white", fg="green")
    btn_cerrar.grid(column=3, row=5, padx=10, pady=10)

    # Cerrar la ventana
    def cerrar_ventana7():
        ventana7.destroy()
    btn_cerrar = tk.Button(ventana7, text="      Cerrar ventana      ", font=("Helvetica", 10, "bold"), command=cerrar_ventana7, bg="red", fg="black")
    btn_cerrar.grid(column=2, row=5, columnspan=1, padx=10, pady=10)
