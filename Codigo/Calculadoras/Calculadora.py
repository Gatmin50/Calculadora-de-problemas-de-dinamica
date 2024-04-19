import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import math
import turtle
import os

def mini_calculadora():

    # Crear la ventana del menu de la calculadora
    ventana3 = ctk.CTk()
    ventana3.title("Calculadora")
    ventana3.geometry('810x280+400+200')
    ventana3.configure(bg_color='black')
    directorio = 'C:/calculadora_de_dinamica/'
    ruta_local = os.path.join(directorio, 'Calculadora.ico')
    ventana3.iconbitmap(ruta_local)

    def add_character(character):
        entry_text = entry.get()
        entry_text += character
        entry.delete(0, ctk.END)
        entry.insert(0, entry_text)

    def delete_all():
        entry.delete(0, tk.END)

    def delete_last():
        entry_text = entry.get()
        entry_text = entry_text[:-1]
        entry.delete(0, ctk.END)
        entry.insert(0, entry_text)

    def perform_operacion():
        try:
            expression = entry.get()
            result = eval(expression)  # Evalúa la expresión ingresada
            entry.delete(0, ctk.END)
            entry.insert(0, str(result))  # Muestra el resultado en el cuadro de texto
        except:
            entry.delete(0, ctk.END)
            entry.insert(0, "Error")  # Manejo de error si la expresión no es válida

    entry = ctk.CTkEntry(ventana3, width=40)
    entry.grid(column=0, row=0, columnspan=5, padx=10, pady=10)

    btn_1 = ctk.CTkButton(ventana3, text=" 1 ", command=lambda: add_character("1"), text_color="white")
    btn_1.grid(column=0, row=3, columnspan=1, padx=10, pady=10)

    btn_2 = ctk.CTkButton(ventana3, text=" 2 ", command=lambda: add_character("2"), text_color="white")
    btn_2.grid(column=1, row=3, columnspan=1, padx=10, pady=10)

    btn_3 = ctk.CTkButton(ventana3, text=" 3 ", command=lambda: add_character("3"), text_color="white")
    btn_3.grid(column=2, row=3, columnspan=1, padx=10, pady=10)

    btn_4 = ctk.CTkButton(ventana3, text=" 4 ", command=lambda: add_character("4"), text_color="white")
    btn_4.grid(column=0, row=2, columnspan=1, padx=10, pady=10)

    btn_5 = ctk.CTkButton(ventana3, text=" 5 ", command=lambda: add_character("5"), text_color="white")
    btn_5.grid(column=1, row=2, columnspan=1, padx=10, pady=10)

    btn_6 = ctk.CTkButton(ventana3, text=" 6 ", command=lambda: add_character("6"), text_color="white")
    btn_6.grid(column=2, row=2, columnspan=1, padx=10, pady=10)

    btn_7 = ctk.CTkButton(ventana3, text=" 7 ", command=lambda: add_character("7"), text_color="white")
    btn_7.grid(column=0, row=1, columnspan=1, padx=10, pady=10)

    btn_8 = ctk.CTkButton(ventana3, text=" 8 ", command=lambda: add_character("8"), text_color="white")
    btn_8.grid(column=1, row=1, columnspan=1, padx=10, pady=10)

    btn_9 = ctk.CTkButton(ventana3, text=" 9 ", command=lambda: add_character("9"), text_color="white")
    btn_9.grid(column=2, row=1, columnspan=1, padx=10, pady=10)

    btn_0 = ctk.CTkButton(ventana3, text=" 0 ", command=lambda: add_character("0"), text_color="white")
    btn_0.grid(column=0, row=4, columnspan=1, padx=10, pady=10)

    btn_10 = ctk.CTkButton(ventana3, text=" - ", command=lambda: add_character("-"), text_color="white")
    btn_10.grid(column=4, row=3, columnspan=1, padx=10, pady=10)

    btn_11 = ctk.CTkButton(ventana3, text=" + ", command=lambda: add_character("+"), text_color="white")
    btn_11.grid(column=3, row=3, columnspan=1, padx=10, pady=10)

    btn_12 = ctk.CTkButton(ventana3, text=" X ", command=lambda: add_character("*"), text_color="white")
    btn_12.grid(column=3, row=2, columnspan=1, padx=10, pady=10)

    btn_13 = ctk.CTkButton(ventana3, text=" / ", command=lambda: add_character("/"), text_color="white")
    btn_13.grid(column=4, row=2, columnspan=1, padx=10, pady=10)

    btn_14 = ctk.CTkButton(ventana3, text=" = ", command=perform_operacion, text_color="white")
    btn_14.grid(column=4, row=4, columnspan=1, padx=10, pady=10)

    btn_15 = ctk.CTkButton(ventana3, text=" · ", command=lambda: add_character("."), text_color="white")
    btn_15.grid(column=1, row=4, columnspan=1, padx=10, pady=10)

    btn_16 = ctk.CTkButton(ventana3, text=" Ac ", command=delete_all, text_color="white")
    btn_16.grid(column=4, row=1, columnspan=1, padx=10, pady=10)

    btn_17 = ctk.CTkButton(ventana3, text=" Del ", command=delete_last, text_color="white")
    btn_17.grid(column=3, row=1, columnspan=1, padx=10, pady=10)

    btn_18 = ctk.CTkButton(ventana3, text=" ( ", command=lambda: add_character("("), text_color="white")
    btn_18.grid(column=2, row=4, columnspan=1, padx=10, pady=10)

    btn_19 = ctk.CTkButton(ventana3, text=" ) ", command=lambda: add_character(")"), text_color="white")
    btn_19.grid(column=3, row=4, columnspan=1, padx=10, pady=10)

    # Boton de cierre de ventana
    def cerrar_ventana():
        ventana3.destroy()

    btn_cerrar = ctk.CTkButton(ventana3, text="    OFF    ", font=("Helvetica", 10, "bold"), command=cerrar_ventana, text_color="white")
    btn_cerrar.grid(column=2, row=5,columnspan=2, padx=10, pady=10)

    # Mantiene la ventana simpre abierta hasta que el usuario la cierra
    ventana3.mainloop()
