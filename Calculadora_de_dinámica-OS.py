import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import math
import turtle
import Intro
import Una_masa
import Dos_masas
import Calculadora
import Trabajo_vertical
import Trabajo_plano
import Trabajo_inclinado
import Trabajo_circular
import Ondas_armónicas

Intro.animacion_inicial()

# Crear la ventana del menu de la calculadora
ctk.set_appearance_mode("system")
ventana1 = ctk.CTk()
ventana1.title("Menu calculadora de Dinámica")
ventana1.geometry('710x300+400+200')
ventana1.configure(fg_color="black")

def programa_plano_inclinado():
    Una_masa.programa_plano_inclinado()

def programa_plano_inclinado_con_dos_cuerpos():
    Dos_masas.programa_plano_inclinado_con_dos_cuerpos()

def mini_calculadora():
    Calculadora.mini_calculadora()

def Vertical():
    Trabajo_vertical.Vertical()

def Plano():
    Trabajo_plano.Plano()

def Inclinado():
    Trabajo_inclinado.Inclinado()
    
def Circular():
    Trabajo_circular.Circular()

def Ondas():
    Ondas_armónicas.ondas_armónicas()

# despliege de secciones
def seleccionar_opcion(event):
    opcion_seleccionada = combobox.get()
    etiqueta_resultado.configure(text="Opción: " + opcion_seleccionada)

    if opcion_seleccionada == "Vertical":
        Vertical()
    elif opcion_seleccionada == "Plano":
        Plano()
    elif opcion_seleccionada == "Inclinado":
        Inclinado()
    elif opcion_seleccionada == "Circular":
        Circular()

combobox = ctk.CTkComboBox(ventana1, values=["", "Vertical", "Plano", "Inclinado", "Circular"], command=seleccionar_opcion)
combobox.grid_remove()
etiqueta_resultado = ctk.CTkLabel(ventana1, text="", text_color="white")
etiqueta_resultado.grid_remove()
etiqueta_seleccion = ctk.CTkLabel(ventana1, text="Selecciona una opcion:", text_color="white")
etiqueta_seleccion.grid_remove()

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

def Plano():
    ventana6 = tk.Tk()
    ventana6.title("Trabajo y energia plano")
    ventana6.geometry('1300x650+100+100')
    ventana6.configure(background='black')

    # Etiquetas
    etiqueta = tk.Label(ventana6, text='No se contempla la friccion', bg="black", fg="gold")
    etiqueta.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        
    etiqueta_masa = tk.Label(ventana6, text='Masa (kg)', bg="black", fg="white")
    etiqueta_masa.grid(row=1, column=0, padx=10, pady=10)
        
    etiqueta_gravedad = tk.Label(ventana6, text='Gravedad (m/s)', bg="black", fg="white")
    etiqueta_gravedad.grid(row=2, column=0, padx=10, pady=10)

    etiqueta_velocidad = tk.Label(ventana6, text='velocidad (m/s)', bg="black", fg="white")
    etiqueta_velocidad.grid(row=3, column=0, padx=10, pady=10)

    etiqueta_distancia = tk.Label(ventana6, text='Distancia (m)', bg="black", fg="white")
    etiqueta_distancia.grid(row=1, column=2, padx=10, pady=10)

    etiqueta_Fuerza = tk.Label(ventana6, text='Fuerza (N)', bg="black", fg="white")
    etiqueta_Fuerza.grid(row=2, column=2, padx=10, pady=10)

    etiqueta_Tiempo = tk.Label(ventana6, text='Tiempo (s)', bg="black", fg="white")
    etiqueta_Tiempo.grid(row=3, column=2, padx=10, pady=10)

    etiqueta_Trabajo = tk.Label(ventana6, text='Trabajo (J)', bg="black", fg="white")
    etiqueta_Trabajo.grid(row=1, column=4, padx=10, pady=10)

    etiqueta_Altura = tk.Label(ventana6, text='Altura (m)', bg="black", fg="white")
    etiqueta_Altura.grid(row=2, column=4, padx=10, pady=10)
        
    etiqueta_resultado = tk.Label(ventana6, text='', bg="black", fg="white")
    etiqueta_resultado.grid(row=3, column=4, columnspan=2, padx=10, pady=10)
        
    etiqueta_resultado1 = tk.Label(ventana6, text='', bg="black", fg="white")
    etiqueta_resultado1.grid(row=1, column=6, padx=10, pady=10)
    etiqueta_resultado2 = tk.Label(ventana6, text='', bg="black", fg="white")
    etiqueta_resultado2.grid(row=2, column=6, padx=10, pady=10)
    etiqueta_resultado3 = tk.Label(ventana6, text='', bg="black", fg="white")
    etiqueta_resultado3.grid(row=3, column=6, padx=10, pady=10)
    etiqueta_resultado4 = tk.Label(ventana6, text='', bg="black", fg="white")
    etiqueta_resultado4.grid(row=4, column=6, padx=10, pady=10)
    etiqueta_resultado5 = tk.Label(ventana6, text='', bg="black", fg="white")
    etiqueta_resultado5.grid(row=5, column=6, padx=10, pady=10)

    #Entradas de datos
    masa = tk.Entry(ventana6)
    masa.grid(row=1, column=1, padx=10, pady=10)
        
    gravedad = tk.Entry(ventana6)
    gravedad.grid(row=2, column=1, padx=10, pady=10)

    velocidad = tk.Entry(ventana6)
    velocidad.grid(row=3, column=1, padx=10, pady=10)

    distancia = tk.Entry(ventana6)
    distancia.grid(row=1, column=3, padx=10, pady=10)

    Fuerza = tk.Entry(ventana6)
    Fuerza.grid(row=2, column=3, padx=10, pady=10)
        
    Tiempo = tk.Entry(ventana6)
    Tiempo.grid(row=3, column=3, padx=10, pady=10)

    Trabajo = tk.Entry(ventana6)
    Trabajo.grid(row=1, column=5, padx=10, pady=10)

    Altura = tk.Entry(ventana6)
    Altura.grid(row=2, column=5, padx=10, pady=10)

    def trabajo():

        try:
            f = float(Fuerza.get())
            d = float(distancia.get())
            w = f * d
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
        
    def grafico_orizontal():
        lienzo_turtle = turtle.ScrolledCanvas(ventana6)
        lienzo_turtle.grid(column=1, row=6, columnspan=4, padx=10, pady=10)
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
        t.forward(180)
        t.right(90)

        # Cuerpo
        t.penup()
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.pensize(4)
        t.pencolor('grey')
        t.pendown()
        t.left(90)
        t.circle(20)
        t.left(90)
        t.penup()
        t.forward(20)
        t.right(180)

        # Flecha de la fuerza
        t.pendown()
        t.pencolor('lightgreen')
        t.forward(40)
        t.left(90)
        t.forward(10)
        t.left(180)
        t.left(45)
        t.forward(15)
        t.left(180)
        t.forward(15)
        t.left(180)
        t.right(45)
        t.forward(20)
        t.left(180)
        t.right(45)
        t.forward(15)

        # Esconder el lapiz
        t.hideturtle()

    #Botones
    Calcular_w = tk.Button(ventana6, text="Calcular W", command=lambda:(trabajo(), grafico_orizontal()), bg="white", fg="black")
    Calcular_w.grid(row=4, column=0, padx=10, pady=10) 
    Calcular_p = tk.Button(ventana6, text="Calcular P", command=potencia, bg="white", fg="black")
    Calcular_p.grid(row=4, column=1, padx=10, pady=10)  
    Calcular_Ec = tk.Button(ventana6, text="Calcular Ec", command=energia_cinetica, bg="white", fg="black")
    Calcular_Ec.grid(row=4, column=2, padx=10, pady=10)
    Calcular_Epg = tk.Button(ventana6, text="Calcular Epg", command=energia_potencial_gravitatoria, bg="white", fg="black")
    Calcular_Epg.grid(row=4, column=3, padx=10, pady=10)
    Calcular_Emt = tk.Button(ventana6, text="Calcular Emt", command=energia_mecanica_total, bg="white", fg="black")
    Calcular_Emt.grid(row=4, column=4, padx=10, pady=10)

    #Resetear los datos laterales
    def reset_datos():
        etiqueta_resultado1.config(text=f"")
        etiqueta_resultado2.config(text=f"")
        etiqueta_resultado3.config(text=f"")
        etiqueta_resultado4.config(text=f"")
        etiqueta_resultado5.config(text=f"")
    btn_cerrar = tk.Button(ventana6, text="Borrar datos laterales", font=("Helvetica", 10, "bold"), command=reset_datos, bg="white", fg="green")
    btn_cerrar.grid(column=3, row=5, padx=10, pady=10)

    # Cerrar la ventana
    def cerrar_ventana6():
        ventana6.destroy()
    btn_cerrar = tk.Button(ventana6, text="      Cerrar ventana      ", font=("Helvetica", 10, "bold"), command=cerrar_ventana6, bg="red", fg="black")
    btn_cerrar.grid(column=2, row=5, columnspan=1, padx=10, pady=10)

    
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

def ondas_armónicas():

    ventana9 = ctk.CTk()
    ventana9.title("Calculadora ondas armonicas")
    ventana9.geometry('1400x650+400+200')
    ventana9.configure(fg_color="black")

    # Etiquetas
        
    etiqueta_periodo = ctk.CTkLabel(ventana9, text='Periodo (s)', text_color='white')
    etiqueta_periodo.grid(row=1, column=0, padx=10, pady=10)
        
    etiqueta_longitud_de_onda = ctk.CTkLabel(ventana9, text='Longitud de onda (m)', text_color='white')
    etiqueta_longitud_de_onda.grid(row=1, column=2, padx=10, pady=10)

    etiqueta_velocidad_propagación = ctk.CTkLabel(ventana9, text='velocidad de propagacion (m/s)', text_color='white')
    etiqueta_velocidad_propagación.grid(row=2, column=0, padx=10, pady=10)

    etiqueta_número_de_onda = ctk.CTkLabel(ventana9, text='número de onda', text_color='white')
    etiqueta_número_de_onda.grid(row=2, column=2, padx=10, pady=10)

    etiqueta_frecuencia = ctk.CTkLabel(ventana9, text='fercuencia (Hz)', text_color='white')
    etiqueta_frecuencia.grid(row=1, column=4, padx=10, pady=10)
        
    etiqueta_resultado = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado.grid(row=5, column=4, columnspan=2, padx=10, pady=10)
        
    etiqueta_resultado1 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado1.grid(row=1, column=6, padx=10, pady=10)
    etiqueta_resultado2 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado2.grid(row=2, column=6, padx=10, pady=10)
    etiqueta_resultado3 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado3.grid(row=3, column=6, padx=10, pady=10)
    etiqueta_resultado4 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado4.grid(row=4, column=6, padx=10, pady=10)
    etiqueta_resultado5 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado5.grid(row=5, column=6, padx=10, pady=10)
    etiqueta_resultado6 = ctk.CTkLabel(ventana9, text='', text_color='white')
    etiqueta_resultado6.grid(row=6, column=6, padx=10, pady=10)

    # Entradas de datos

    periodo = ctk.CTkEntry(ventana9)
    periodo.grid(row=1, column=1, padx=10, pady=10)
    longitud_de_onda = ctk.CTkEntry(ventana9)
    longitud_de_onda.grid(row=1, column=3, padx=10, pady=10)
    velocidad_propagación = ctk.CTkEntry(ventana9)
    velocidad_propagación.grid(row=2, column=1, padx=10, pady=10)
    número_de_onda = ctk.CTkEntry(ventana9)
    número_de_onda.grid(row=2, column=3, padx=10, pady=10)
    frecuencia = ctk.CTkEntry(ventana9)
    frecuencia.grid(row=1, column=5, padx=10, pady=10)
    pi = math.pi

    def calcular_omega():
        if T:
            try:
                T = float(periodo.get())
                w = (2*pi)/T
                resultado = round(w, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de T debe ser numérico")

        elif landa:
            try:
                c = float(300000000)
                landa = float(longitud_de_onda.get())
                f = c / landa
                w = 2 * pi * f
                resultado = round(w, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de landa debe ser numérico")

        elif k and Vprop:
            try:
                k = float(k)
                Vprop = float(velocidad_propagación.get())
                w = k * Vprop
                resultado = round(w, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"Los valores de k y Vprop deben ser numéricos")

        elif f:
            try:
                f = float(frecuencia.get())
                w = 2 * pi * f
                resultado = round(w, 3)
                etiqueta_resultado.configure(text=f"El resultado es {resultado}(m/s)")
            except ValueError:
                etiqueta_resultado.configure(text=f"El valor de f debe ser numérico")
                
        else:
            etiqueta_resultado.configure(text=f"Por favor, introduce al menos un valor")



    def longitud_onda():
        try:
            landa = 'hola'
        
        except ValueError:
            print('hola')
    
    #Resetear los datos laterales
    def reset_datos():
        etiqueta_resultado1.configure(text=f"")
        etiqueta_resultado2.configure(text=f"")
        etiqueta_resultado3.configure(text=f"")
        etiqueta_resultado4.configure(text=f"")
        etiqueta_resultado5.configure(text=f"")
        etiqueta_resultado6.configure(text=f"")
    btn_cerrar = ctk.CTkButton(ventana9, text="Borrar datos laterales", font=("Helvetica", 10, "bold"), command=reset_datos)
    btn_cerrar.grid(column=3, row=5, padx=10, pady=10)

    btn_cerrar = ctk.CTkButton(ventana9, text="Calcular W", font=("Helvetica", 10, "bold"), command=calcular_omega)
    btn_cerrar.grid(column=0, row=3, padx=10, pady=10)

=======
>>>>>>> bb01275ba5329ddf0366be95cd684d2051aa2ee6
def cerrar_ventana4():
    combobox.grid_remove()
    etiqueta_resultado.grid_remove()
    etiqueta_seleccion.grid_remove()
    btn_back.grid_remove()
    ventana1.title("Menu calculadora de Dinámica")
    boton_calculadora_plano_inclinado.grid(column=2, row=2, padx=10, pady=10)
    boton_calculadora_plano_inclinado_con_dos_cuerpos.grid(column=4, row=2, padx=10, pady=10)
    boton_calculadora.grid(column=2, row=4, columnspan=2, padx=10, pady=10)
    boton_calculadora_te.grid(column=3, row=3, columnspan=2, padx=10, pady=10)
    btn_cerrar.grid(column=2, row=5, columnspan=3, padx=10, pady=10)
    boton_calculadora_ondas_armonicas.grid(column=2, row=3, padx=10, pady=10)
    ventana1.geometry('710x300+400+200')

btn_back = ctk.CTkButton(ventana1, text="Atras", font=("Helvetica", 10, "bold"), command=cerrar_ventana4)
btn_back.grid_remove()

def traspaso1():
    boton_calculadora_plano_inclinado.grid_remove()
    boton_calculadora_plano_inclinado_con_dos_cuerpos.grid_remove()
    boton_calculadora.grid_remove()
    boton_calculadora_te.grid_remove()
    btn_cerrar.grid_remove()
    boton_calculadora_ondas_armonicas.grid_remove
    ventana1.title("Menu calculadora de Trabajo y Energía")
    combobox.grid(row=0, column=1, padx=10, pady=10)
    etiqueta_resultado.grid(row=1, column=1, padx=10, pady=10)
    etiqueta_seleccion.grid(row=0, column=0, padx=10, pady=10)
    btn_back.grid(column=0, row=2, columnspan=2, padx=10, pady=10)
    ventana1.geometry('390x150')

# Crear los botones de las calculadoras
boton_calculadora_plano_inclinado = ctk.CTkButton(ventana1, text="Calculadora de plano inclinado", command=programa_plano_inclinado , font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora_plano_inclinado.grid(column=2, row=2, padx=10, pady=10)
boton_calculadora_plano_inclinado_con_dos_cuerpos = ctk.CTkButton(ventana1, text="Calculadora de plano inclinado \n con dos cuerpos unidos", command=programa_plano_inclinado_con_dos_cuerpos , font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora_plano_inclinado_con_dos_cuerpos.grid(column=4, row=2, padx=10, pady=10)
boton_calculadora = ctk.CTkButton(ventana1, text="Calculadora", command=mini_calculadora , font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora.grid(column=2, row=4, columnspan=2, padx=10, pady=10)
boton_calculadora_te = ctk.CTkButton(ventana1, text="Problemas de trabajo y energia", command=traspaso1 , font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora_te.grid(column=3, row=3, columnspan=2, padx=10, pady=10)
boton_calculadora_ondas_armonicas = ctk.CTkButton(ventana1, text="Calculadora de \n ondas armonicas", command=Ondas, font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora_ondas_armonicas.grid(column=2, row=3, padx=10, pady=10)

def cerrar_ventana():
    ventana1.destroy()

btn_cerrar = ctk.CTkButton(ventana1, text="Cerrar ventana", font=("Helvetica", 10, "bold"), command=cerrar_ventana, corner_radius=20)
btn_cerrar.grid(column=2, row=5, columnspan=3, padx=10, pady=10, sticky='s')

# Mantiene la ventana simpre abierta hasta que el usuario la cierra
ventana1.mainloop()