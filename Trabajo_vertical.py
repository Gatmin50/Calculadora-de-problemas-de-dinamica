import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import math
import turtle

def Vertical():
    ventana5 = tk.Tk()
    ventana5.title("Trabajo y energia vertical")
    ventana5.geometry('1300x650+100+100')
    ventana5.configure(background='black')
        
    # Etiquetas
    etiqueta = tk.Label(ventana5, text='No se contempla la friccion con el aire', bg="black", fg="gold")
    etiqueta.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        
    etiqueta_masa = tk.Label(ventana5, text='Masa (kg)', bg="black", fg="white")
    etiqueta_masa.grid(row=1, column=0, padx=10, pady=10)
        
    etiqueta_gravedad = tk.Label(ventana5, text='Gravedad (m/s)', bg="black", fg="white")
    etiqueta_gravedad.grid(row=2, column=0, padx=10, pady=10)
        
    etiqueta_velocidad_i = tk.Label(ventana5, text='Velocidad inicial (m/s)', bg="black", fg="white")
    etiqueta_velocidad_i.grid(row=1, column=2, padx=10, pady=10)
        
    etiqueta_altura_i = tk.Label(ventana5, text='Altura inicial (m)', bg="black", fg="white")
    etiqueta_altura_i.grid(row=2, column=2, padx=10, pady=10)

    etiqueta_distancia = tk.Label(ventana5, text='Distancia (m)', bg="black", fg="white")
    etiqueta_distancia.grid(row=3, column=2, padx=10, pady=10)

    etiqueta_Fuerza = tk.Label(ventana5, text='Fuerza (N)', bg="black", fg="white")
    etiqueta_Fuerza.grid(row=3, column=0, padx=10, pady=10)

    etiqueta_Tiempo = tk.Label(ventana5, text='Tiempo (s)', bg="black", fg="white")
    etiqueta_Tiempo.grid(row=1, column=4, padx=10, pady=10)

    etiqueta_Trabajo = tk.Label(ventana5, text='Trabajo (J)', bg="black", fg="white")
    etiqueta_Trabajo.grid(row=2, column=4, padx=10, pady=10)

    etiqueta_Altura = tk.Label(ventana5, text='Altura (m)', bg="black", fg="white")
    etiqueta_Altura.grid(row=3, column=4, padx=10, pady=10)
        
    etiqueta_resultado = tk.Label(ventana5, text='', bg="black", fg="white")
    etiqueta_resultado.grid(row=5, column=5, padx=10, pady=10)
        
    etiqueta_resultado1 = tk.Label(ventana5, text='', bg="black", fg="white")
    etiqueta_resultado1.grid(row=1, column=6, padx=10, pady=10)
    etiqueta_resultado2 = tk.Label(ventana5, text='', bg="black", fg="white")
    etiqueta_resultado2.grid(row=2, column=6, padx=10, pady=10)
    etiqueta_resultado3 = tk.Label(ventana5, text='', bg="black", fg="white")
    etiqueta_resultado3.grid(row=3, column=6, padx=10, pady=10)
    etiqueta_resultado4 = tk.Label(ventana5, text='', bg="black", fg="white")
    etiqueta_resultado4.grid(row=4, column=6, padx=10, pady=10)
    etiqueta_resultado5 = tk.Label(ventana5, text='', bg="black", fg="white")
    etiqueta_resultado5.grid(row=5, column=6, padx=10, pady=10)
    etiqueta_resultado6 = tk.Label(ventana5, text='', bg="black", fg="white")
    etiqueta_resultado6.grid(row=6, column=6, padx=10, pady=10)
    etiqueta_resultado7 = tk.Label(ventana5, text='', bg="black", fg="white")
    etiqueta_resultado7.grid(row=7, column=6, padx=10, pady=10)
    etiqueta_resultado8 = tk.Label(ventana5, text='', bg="black", fg="white")
    etiqueta_resultado8.grid(row=8, column=6, padx=10, pady=10)

    #Entradas de datos
    masa = tk.Entry(ventana5)
    masa.grid(row=1, column=1, padx=10, pady=10)
        
    gravedad = tk.Entry(ventana5)
    gravedad.grid(row=2, column=1, padx=10, pady=10)
        
    velocidad_i = tk.Entry(ventana5)
    velocidad_i.grid(row=1, column=3, padx=10, pady=10)
        
    altura_i = tk.Entry(ventana5)
    altura_i.grid(row=2, column=3, padx=10, pady=10)

    distancia = tk.Entry(ventana5)
    distancia.grid(row=3, column=3, padx=10, pady=10)

    Fuerza = tk.Entry(ventana5)
    Fuerza.grid(row=3, column=1, padx=10, pady=10)
        
    Tiempo = tk.Entry(ventana5)
    Tiempo.grid(row=1, column=5, padx=10, pady=10)

    Trabajo = tk.Entry(ventana5)
    Trabajo.grid(row=2, column=5, padx=10, pady=10)

    Altura = tk.Entry(ventana5)
    Altura.grid(row=3, column=5, padx=10, pady=10)

    # Calculos
    def altura_max():

        try:
            g = float(gravedad.get())
            vi = float(velocidad_i.get())
            hi = float(altura_i.get())
            v2 = vi * vi                
            hmax = ((1/2) * v2) / g
            hf = hmax + hi
            resultado = round(hf, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(m)")
            etiqueta_resultado1.config(text=f"La altura maxima es: {resultado}(m)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def altura_a_velocidad_media():

        try:
            g = float(gravedad.get())
            vi = float(velocidad_i.get())
            hi = float(altura_i.get())
            v2 = vi * vi
            hmax = ((3/8) * v2) / g
            hf = hmax + hi
            resultado = round(hf, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(m)")
            etiqueta_resultado2.config(text=f"La altura a la mitad de \n velocidad es: {resultado}(m)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")
    
    def velocidad_de_impacto():

        try:
            vi = float(velocidad_i.get())
            v_impacto = vi
            resultado = round(v_impacto, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(m/s)")
            etiqueta_resultado3.config(text=f"La velocidad de impacto es: {resultado}(m/s)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def trabajo():

        try:
            f = float(Fuerza.get())
            d = float(distancia.get())
            w = f * d
            resultado = round(w, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado4.config(text=f"El trabajo del cuerpo es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def energia_cinetica():

        try:
            v = float(velocidad_i.get())
            v2 = v * v
            m = float(masa.get())
            Ec = 0.5 * m * v2
            resultado = round(Ec, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado5.config(text=f"La enegia cinetica es: {resultado}(J)")
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
            etiqueta_resultado6.config(text=f"La enegia potencial es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")

    def energia_mecanica_total():

        try:
            v = float(velocidad_i.get())
            v2 = v * v
            m = float(masa.get())
            h = float(Altura.get())
            g = float(gravedad.get())
            Epg = m * g * h
            Ec = 0.5 * m * v2
            Emt = Epg + Ec
            resultado = round(Emt, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(J)")
            etiqueta_resultado7.config(text=f"La enegia mecanica total es: {resultado}(J)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")
        
    def potencia():

        try:
            t = float(Tiempo.get())
            w = float(Trabajo.get())
            p = w / t
            resultado = round(p, 3)
            etiqueta_resultado.config(text=f"El resultado es: {resultado}(W)")
            etiqueta_resultado8.config(text=f"La potencia es: {resultado}(W)")
        except ValueError:
            etiqueta_resultado.config(text=f"Todos los valores deben \n ser unicamente numéricos")


    # Graficos
    def grafico_H_max():
        h = (altura_i.get())
        texto1 = 'A'
        texto2 = 'B'
        texto3 = 'h ='
        texto4 = 'h = ?'
        texto5 = 'X'
        texto6 = 'Y'

        lienzo_turtle = turtle.ScrolledCanvas(ventana5)
        lienzo_turtle.grid(column=1, row=7, columnspan=4, padx=10, pady=10)
        # Crear un objeto Turtle en el lienzo
        t = turtle.RawTurtle(lienzo_turtle)
        t.speed(100)

        t.pensize(5)
        t.pencolor('black')
        t.penup()
        t.setpos(-100, -120)
        t.pendown()

        # Base
        t.forward(200)
        t.left(180)
        t.forward(100)

        # CuerpoA
        t.pensize(3)
        t.right(90)
        t.penup()
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.pendown()
        t.circle(20)
        t.left(90)
        t.penup()
        t.forward(20)

        # Flecha
        t.right(90)
        t.pendown()
        t.pencolor('blue')
        t.forward(40)
        t.left(90)
        t.forward(10)
        t.right(-225)
        t.forward(15)
        t.right(180)
        t.forward(15)
        t.right(225)
        t.forward(20)
        t.right(225)
        t.forward(15)

        # Linea de eje
        t.pencolor('grey')
        t.right(45)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)

        # CuerpoB
        t.pencolor('black')
        t.pendown()
        t.circle(20)
        t.penup()
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(180)

        # Linea de eje
        t.pencolor('grey')
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)

        # cual es cada massa
        t.pencolor('black')
        t.penup()
        x = -110
        y = -120
        t.goto(x, y)
        t.write(texto5, align="center", font=('Arial', 10))

        x = 40
        y = -105
        t.goto(x, y)
        t.write(texto1, align="center", font=('Arial', 10))

        x = 35
        y = -115
        t.goto(x, y)
        t.write(texto3, align="center", font=('Arial', 10))

        x = 60
        y = -115
        t.goto(x, y)
        t.write(h, align="center", font=('Arial', 10))

        x = 40
        y = 90
        t.goto(x, y)
        t.write(texto2, align="center", font=('Arial', 10))

        x = 40
        y = 80
        t.goto(x, y)
        t.write(texto4, align="center", font=('Arial', 10))

        x = -10
        y = 120
        t.goto(x, y)
        t.write(texto6, align="center", font=('Arial', 10))

        # Escoder lapiz
        t.hideturtle()
        
    def grafico_H_a_velocidad_media():
        h = float(altura_i.get())
        texto1 = 'A'
        texto2 = 'B'
        texto3 = 'h ='
        texto4 = 'h = ?'
        texto5 = 'X'
        texto6 = 'Y'

        lienzo_turtle = turtle.ScrolledCanvas(ventana5)
        lienzo_turtle.grid(column=1, row=7, columnspan=4, padx=10, pady=10)
        # Crear un objeto Turtle en el lienzo
        t = turtle.RawTurtle(lienzo_turtle)
        t.speed(100)

        t.pensize(5)
        t.pencolor('black')
        t.penup()
        t.setpos(-100, -120)
        t.pendown()

        # Base
        t.forward(200)
        t.left(180)
        t.forward(100)

        # CuerpoA
        t.pensize(3)
        t.right(90)
        t.penup()
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.pendown()
        t.circle(20)
        t.left(90)
        t.penup()
        t.forward(20)

        # Flecha
        t.right(90)
        t.pendown()
        t.pencolor('blue')
        t.forward(40)
        t.left(90)
        t.forward(10)
        t.right(-225)
        t.forward(15)
        t.right(180)
        t.forward(15)
        t.right(225)
        t.forward(20)
        t.right(225)
        t.forward(15)

        # Linea de eje
        t.pencolor('grey')
        t.right(45)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)

        # CuerpoB
        t.pencolor('black')
        t.pendown()
        t.circle(20)
        t.penup()
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(180)

        # Linea de eje
        t.pencolor('grey')
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)

        # cual es cada massa
        t.pencolor('black')
        t.penup()
        x = -110
        y = -120
        t.goto(x, y)
        t.write(texto5, align="center", font=('Arial', 10))

        x = 40
        y = -105
        t.goto(x, y)
        t.write(texto1, align="center", font=('Arial', 10))

        x = 35
        y = -115
        t.goto(x, y)
        t.write(texto3, align="center", font=('Arial', 10))

        x = 60
        y = -115
        t.goto(x, y)
        t.write(h, align="center", font=('Arial', 10))

        x = 40
        y = 5
        t.goto(x, y)
        t.write(texto2, align="center", font=('Arial', 10))

        x = 40
        y = -5
        t.goto(x, y)
        t.write(texto4, align="center", font=('Arial', 10))

        x = -10
        y = 120
        t.goto(x, y)
        t.write(texto6, align="center", font=('Arial', 10))

        # Escoder lapiz
        t.hideturtle()

    def grafico_v_de_impacto():
        h = float(altura_i.get())
        texto1 = 'A'
        texto2 = 'h ='
        texto3 = 'X'
        texto4 = 'Y'
        texto5 = 'B'
        texto6 = 'v = ?'

        lienzo_turtle = turtle.ScrolledCanvas(ventana5)
        lienzo_turtle.grid(column=1, row=7, columnspan=4, padx=10, pady=10)
        # Crear un objeto Turtle en el lienzo
        t = turtle.RawTurtle(lienzo_turtle)
        t.speed(100)

        t.pensize(5)
        t.pencolor('black')
        t.penup()
        t.setpos(-200, -120)
        t.pendown()

        # Base
        t.forward(200)
        t.left(180)
        t.forward(100)

        # CuerpoA
        t.pensize(3)
        t.right(90)
        t.penup()
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.pendown()
        t.circle(20)
        t.left(90)
        t.penup()
        t.forward(20)

        # Flecha
        t.right(90)
        t.pendown()
        t.pencolor('blue')
        t.forward(40)
        t.left(90)
        t.forward(10)
        t.right(-225)
        t.forward(15)
        t.right(180)
        t.forward(15)
        t.right(225)
        t.forward(20)
        t.right(225)
        t.forward(15)

        # Linea de eje
        t.pencolor('grey')
        t.right(45)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)

        # cual es cada massa
        t.pencolor('black')
        t.penup()
        x = -210
        y = -120
        t.goto(x, y)
        t.write(texto3, align="center", font=('Arial', 10))

        x = -60
        y = -105
        t.goto(x, y)
        t.write(texto1, align="center", font=('Arial', 10))

        x = -65
        y = -115
        t.goto(x, y)
        t.write(texto2, align="center", font=('Arial', 10))

        x = -40
        y = -115
        t.goto(x, y)
        t.write(h, align="center", font=('Arial', 10))

        x = -110
        y = 120
        t.goto(x, y)
        t.write(texto4, align="center", font=('Arial', 10))

        # Segunda parte
        t.pensize(5)
        t.pencolor('black')
        t.penup()
        t.setpos(50, -120)
        t.pendown()

        # Base
        t.right(90)
        t.forward(200)
        t.left(180)
        t.forward(100)

        # Line de ejes
        t.pencolor('grey')
        t.pensize(3)
        t.right(90)
        t.penup()
        t.forward(60)
        t.right(90)
        t.forward(20)
        t.left(90)

        # CuerpoB
        t.pencolor('black')
        t.pendown()
        t.circle(20)
        t.penup()
        t.left(90)
        t.forward(20)
        t.left(90)

        # flecha caida
        t.pendown()
        t.pencolor('red')
        t.forward(40)
        t.left(90)
        t.forward(10)
        t.right(-225)
        t.forward(15)
        t.right(180)
        t.forward(15)
        t.right(225)
        t.forward(20)
        t.right(225)
        t.forward(15)
        t.left(-225)
        t.penup()
        t.forward(45)

        # Linea de eje
        t.pencolor('grey')
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)

        # cual es cada massa
        t.pencolor('black')
        t.penup()
        x = 190
        y = -65
        t.goto(x, y)
        t.write(texto5, align="center", font=('Arial', 10))

        x = 140
        y = 120
        t.goto(x, y)
        t.write(texto4, align="center", font=('Arial', 10))

        x = 45
        y = -120
        t.goto(x, y)
        t.write(texto3, align="center", font=('Arial', 10))

        x = 190
        y = -75
        t.goto(x, y)
        t.write(texto6, align="center", font=('Arial', 10))

        # Esconder el lapiz
        t.hideturtle()


    #Botones
    Calcular_H_max = tk.Button(ventana5, text="h max", command=lambda:(altura_max(), grafico_H_max()), bg="white", fg="black")
    Calcular_H_max.grid(row=4, column=0, padx=10, pady=10)
    Calcular_h_a_velocidad_media = tk.Button(ventana5, text="h a la mitad de \n velocidad", command=lambda: (altura_a_velocidad_media(), grafico_H_a_velocidad_media()), bg="white", fg="black")
    Calcular_h_a_velocidad_media.grid(row=4, column=1, padx=10, pady=10)
    Calcular_v_impact = tk.Button(ventana5, text="v de impacto", command=lambda: (velocidad_de_impacto(), grafico_v_de_impacto()), bg="white", fg="black")
    Calcular_v_impact.grid(row=4, column=2, padx=10, pady=10)
    Calcular_w = tk.Button(ventana5, text="Calcular W", command=trabajo, bg="white", fg="black")
    Calcular_w.grid(row=4, column=3, padx=10, pady=10) 
    Calcular_p = tk.Button(ventana5, text="Calcular P", command=potencia, bg="white", fg="black")
    Calcular_p.grid(row=4, column=4, padx=10, pady=10)  
    Calcular_Ec = tk.Button(ventana5, text="Calcular Ec", command=energia_cinetica, bg="white", fg="black")
    Calcular_Ec.grid(row=5, column=0, padx=10, pady=10)
    Calcular_Epg = tk.Button(ventana5, text="Calcular Epg", command=energia_potencial_gravitatoria, bg="white", fg="black")
    Calcular_Epg.grid(row=5, column=1, padx=10, pady=10)
    Calcular_Emt = tk.Button(ventana5, text="Calcular Emt", command=energia_mecanica_total, bg="white", fg="black")
    Calcular_Emt.grid(row=5, column=2, padx=10, pady=10)
        
    #Resetear los datos laterales
    def reset_datos():
        etiqueta_resultado1.config(text=f"")
        etiqueta_resultado2.config(text=f"")
        etiqueta_resultado3.config(text=f"")
        etiqueta_resultado4.config(text=f"")
        etiqueta_resultado5.config(text=f"")
        etiqueta_resultado6.config(text=f"")
        etiqueta_resultado7.config(text=f"")
        etiqueta_resultado8.config(text=f"")
    btn_cerrar = tk.Button(ventana5, text="Borrar datos laterales", font=("Helvetica", 10, "bold"), command=reset_datos, bg="white", fg="green")
    btn_cerrar.grid(column=3, row=6, padx=10, pady=10)

    # Cerrar la ventana
    def cerrar_ventana5():
        ventana5.destroy()
    btn_cerrar = tk.Button(ventana5, text="      Cerrar ventana      ", font=("Helvetica", 10, "bold"), command=cerrar_ventana5, bg="red", fg="black")
    btn_cerrar.grid(column=2, row=6, columnspan=1, padx=10, pady=10)