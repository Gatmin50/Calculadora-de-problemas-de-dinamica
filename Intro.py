import turtle as t
import time

def animacion_inicial():
    ventanag = t.Screen()
    ventanag.setup(width=1.0, height=1.0)
    ventanag.bgcolor("white")

    # velocidad del lapiz
    t.speed(10)

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

    t.penup()
    t.setpos(-550,0)
    t.pendown()
    t.pensize(3)
    t.right(30)
    t.pencolor('#306998')

    def curve_one():
        for i in range (90):
            t.left(1)
            t.fd (1)

    def curve_two():
        for i in range (90):
            t.right (1)
            t.fd(1)

    def curve_three (d):
        curve_one()
        t.fd(d)
        curve_one()

    def halt_logo():
        t.fd (50)
        curve_one()
        t.fd (90)
        curve_three (80)
        t.fd (40)
        t.left (90)
        t.fd(80)
        t.right (90)
        t.fd (10)
        t.right (90)
        t.fd (120)
        curve_three (90)
        t.fd (30)
        t.left (90)
        t.fd (50)
        curve_two()
        t.fd (40)

    def point_pos(x,y):
        t.penup()
        t.goto(x,y)
        t.dot (40, 'white')
        t.pendown()

    t.begin_fill()
    t.fillcolor("#306998")
    halt_logo()
    t.end_fill()

    t.penup()
    t.goto(-530,-10)
    t.pendown()
    t.fillcolor("#ffda3b")
    t.pencolor("#ffda3b")
    t.begin_fill()
    t.setheading(180)
    halt_logo()
    t.end_fill()

    point_pos(-600,150)
    point_pos(-488, -160)
    t.hideturtle()

    time.sleep(5)
    ventanag.bye()
