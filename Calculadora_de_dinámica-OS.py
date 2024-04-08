import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import Intro
import Una_masa
import Dos_masas
import Calculadora
import Trabajo_vertical
import Trabajo_plano
import Trabajo_inclinado
import Trabajo_circular
import Ondas_armónicas
import Nuclear

Intro.animacion_inicial()

# Crear la ventana del menu de la calculadora
ventana1 = ctk.CTk()
ventana1.title("Menu calculadora de Dinámica")
ventana1.geometry('710x300+400+200')
ventana1.configure(fg_color="black")
ctk.set_default_color_theme("dark-blue")

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

def nuclear():
    Nuclear.calculo_nuclear()

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
boton_calculadora_nuclear = ctk.CTkButton(ventana1, text="Calculadora nuclear", command=nuclear, font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora_nuclear.grid(column=3, row=4, columnspan=2, padx=10, pady=10)

def cerrar_ventana():
    ventana1.destroy()

btn_cerrar = ctk.CTkButton(ventana1, text="Cerrar ventana", font=("Helvetica", 10, "bold"), command=cerrar_ventana, corner_radius=20)
btn_cerrar.grid(column=2, row=5, columnspan=3, padx=10, pady=10, sticky='s')

# Mantiene la ventana simpre abierta hasta que el usuario la cierra
ventana1.mainloop()