import turtle as t
import time
import os

def animacion_inicial():
    ventanag = t.Screen()
    ventanag.title("Intro")
    ventanag.setup(width=1.0, height=1.0)
    ventanag.bgcolor("white") 

    # velocidad del lapiz
    t.speed(5)

    # Definir el tamaño de la línea y el color del trazo
    t.pensize(7)
    t.pencolor('black')

    t.penup()
    t.setpos(160, -100)
    t.pendown()

    # Dibuja el triángulo rectángulo
    t.fillcolor('#DCD9D9')
    t.begin_fill()
    t.left(180)
    t.forward(180)
    t.penup()
    t.forward(30)
    t.pendown()
    t.forward(190)
    t.right(180)
    t.left(30)
    t.forward(462)
    t.right(180)
    t.left(60)
    t.forward(231)
    t.end_fill()

    t.fillcolor('#E87810')
    t.begin_fill()
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(231)
    t.left(90)
    t.forward(80)
    t.left(180)
    t.forward(40)
    t.right(90)
    t.forward(95.5)
    t.penup()
    t.forward(40)
    t.pendown()
    t.forward(95.5)
    t.end_fill()

    t.fillcolor('#FF9C3E')
    t.begin_fill()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(231)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(95.5)
    t.penup()
    t.forward(40)
    t.pendown()
    t.forward(95.5)
    t.end_fill()

    t.penup()
    t.right(90)
    t.forward(440)
    t.right(180)
    t.left(30)
    t.forward(231)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.pendown()

    t.fillcolor('#FC6C6C')
    t.begin_fill()
    t.left(90)
    t.circle(40, 320)
    t.penup()
    t.circle(40, 40)
    t.pendown()
    t.end_fill()

    t.right(90)
    t.penup()
    t.forward(60)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()
    t.left(45)
    t.forward(20)
    t.left(180)
    t.forward(20)
    t.left(180)
    t.right(45)
    t.right(45)
    t.forward(20)
    t.left(180)
    t.forward(20)
    t.left(180)
    t.left(45)
    t.forward(70)

    t.penup()
    t.right(90)
    t.forward(20)
    t.right(90)
    t.pendown()
    t.forward(30)
    t.left(180)
    t.forward(60)

    t.left(180)
    t.penup()
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.backward(10)
    t.pendown()
    t.forward(10)
    t.left(180)
    t.forward(60)
    
    t.hideturtle()
    time.sleep(2)
    ventanag.bye()
