import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import math
import turtle

def mini_calculadora():

    # Crear la ventana del menu de la calculadora
    ventana3 = tk.Tk()
    ventana3.title("Calculadora")
    ventana3.geometry('340x280+400+200')
    ventana3.configure(background='black')

    def add_character(character):
        entry_text = entry.get()
        entry_text += character
        entry.delete(0, tk.END)
        entry.insert(0, entry_text)

    def delete_all():
        entry.delete(0, tk.END)

    def delete_last():
        entry_text = entry.get()
        entry_text = entry_text[:-1]
        entry.delete(0, tk.END)
        entry.insert(0, entry_text)

    def perform_operacion():
        try:
            expression = entry.get()
            result = eval(expression)  # Evalúa la expresión ingresada
            entry.delete(0, tk.END)
            entry.insert(0, str(result))  # Muestra el resultado en el cuadro de texto
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")  # Manejo de error si la expresión no es válida

    entry = tk.Entry(ventana3, width=40)
    entry.grid(column=0, row=0, columnspan=5, padx=10, pady=10)

    btn_1 = tk.Button(ventana3, text=" 1 ", font=("Helvetica", 10, "bold"), command=lambda: add_character("1"), bg="white", fg="black")
    btn_1.grid(column=0, row=3, columnspan=1, padx=10, pady=10)

    btn_2 = tk.Button(ventana3, text=" 2 ", font=("Helvetica", 10, "bold"), command=lambda: add_character("2"), bg="white", fg="black")
    btn_2.grid(column=1, row=3, columnspan=1, padx=10, pady=10)

    btn_3 = tk.Button(ventana3, text=" 3 ", font=("Helvetica", 10, "bold"), command=lambda: add_character("3"), bg="white", fg="black")
    btn_3.grid(column=2, row=3, columnspan=1, padx=10, pady=10)

    btn_4 = tk.Button(ventana3, text=" 4 ", font=("Helvetica", 10, "bold"), command=lambda: add_character("4"), bg="white", fg="black")
    btn_4.grid(column=0, row=2, columnspan=1, padx=10, pady=10)

    btn_5 = tk.Button(ventana3, text=" 5 ", font=("Helvetica", 10, "bold"), command=lambda: add_character("5"), bg="white", fg="black")
    btn_5.grid(column=1, row=2, columnspan=1, padx=10, pady=10)

    btn_6 = tk.Button(ventana3, text=" 6 ", font=("Helvetica", 10, "bold"), command=lambda: add_character("6"), bg="white", fg="black")
    btn_6.grid(column=2, row=2, columnspan=1, padx=10, pady=10)

    btn_7 = tk.Button(ventana3, text=" 7 ", font=("Helvetica", 10, "bold"), command=lambda: add_character("7"), bg="white", fg="black")
    btn_7.grid(column=0, row=1, columnspan=1, padx=10, pady=10)

    btn_8 = tk.Button(ventana3, text=" 8 ", font=("Helvetica", 10, "bold"), command=lambda: add_character("8"), bg="white", fg="black")
    btn_8.grid(column=1, row=1, columnspan=1, padx=10, pady=10)

    btn_9 = tk.Button(ventana3, text=" 9 ", font=("Helvetica", 10, "bold"), command=lambda: add_character("9"), bg="white", fg="black")
    btn_9.grid(column=2, row=1, columnspan=1, padx=10, pady=10)

    btn_0 = tk.Button(ventana3, text=" 0 ", font=("Helvetica", 10, "bold"), command=lambda: add_character("0"), bg="white", fg="black")
    btn_0.grid(column=0, row=4, columnspan=1, padx=10, pady=10)

    btn_10 = tk.Button(ventana3, text=" - ", font=("Helvetica", 10, "bold"), command=lambda: add_character("-"), bg="white", fg="black")
    btn_10.grid(column=4, row=3, columnspan=1, padx=10, pady=10)

    btn_11 = tk.Button(ventana3, text=" + ", font=("Helvetica", 10, "bold"), command=lambda: add_character("+"), bg="white", fg="black")
    btn_11.grid(column=3, row=3, columnspan=1, padx=10, pady=10)

    btn_12 = tk.Button(ventana3, text=" X ", font=("Helvetica", 10, "bold"), command=lambda: add_character("*"), bg="white", fg="black")
    btn_12.grid(column=3, row=2, columnspan=1, padx=10, pady=10)

    btn_13 = tk.Button(ventana3, text=" / ", font=("Helvetica", 10, "bold"), command=lambda: add_character("/"), bg="white", fg="black")
    btn_13.grid(column=4, row=2, columnspan=1, padx=10, pady=10)

    btn_14 = tk.Button(ventana3, text=" = ", font=("Helvetica", 10, "bold"), command=perform_operacion, bg="gold", fg="black")
    btn_14.grid(column=4, row=4, columnspan=1, padx=10, pady=10)

    btn_15 = tk.Button(ventana3, text=" · ", font=("Helvetica", 10, "bold"), command=lambda: add_character("."), bg="white", fg="black")
    btn_15.grid(column=1, row=4, columnspan=1, padx=10, pady=10)

    btn_16 = tk.Button(ventana3, text=" Ac ", font=("Helvetica", 10, "bold"), command=delete_all, bg="blue", fg="white")
    btn_16.grid(column=4, row=1, columnspan=1, padx=10, pady=10)

    btn_17 = tk.Button(ventana3, text=" Del ", font=("Helvetica", 10, "bold"), command=delete_last, bg="blue", fg="white")
    btn_17.grid(column=3, row=1, columnspan=1, padx=10, pady=10)

    btn_18 = tk.Button(ventana3, text=" ( ", font=("Helvetica", 10, "bold"), command=lambda: add_character("("), bg="white", fg="black")
    btn_18.grid(column=2, row=4, columnspan=1, padx=10, pady=10)

    btn_19 = tk.Button(ventana3, text=" ) ", font=("Helvetica", 10, "bold"), command=lambda: add_character(")"), bg="white", fg="black")
    btn_19.grid(column=3, row=4, columnspan=1, padx=10, pady=10)

    # Boton de cierre de ventana
    def cerrar_ventana():
        ventana3.destroy()

    btn_cerrar = tk.Button(ventana3, text="    OFF    ", font=("Helvetica", 10, "bold"), command=cerrar_ventana, bg="red", fg="black")
    btn_cerrar.grid(column=2, row=5,columnspan=2, padx=10, pady=10)

    # Mantiene la ventana simpre abierta hasta que el usuario la cierra
    ventana3.mainloop()