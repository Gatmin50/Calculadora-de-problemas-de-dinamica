import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import os
import platform
import requests
import shutil
import Intro
import Calculadoras.Una_masa as Una_masa
import Calculadoras.Dos_masas as Dos_masas
import Calculadoras.Calculadora as Calculadora
import Calculadoras.Trabajo_vertical as Trabajo_vertical
import Calculadoras.Trabajo_plano as Trabajo_plano
import Calculadoras.Trabajo_inclinado as Trabajo_inclinado
import Calculadoras.Trabajo_circular as Trabajo_circular
import Calculadoras.Ondas_armónicas as Ondas_armónicas
import Calculadoras.Nuclear as Nuclear
import Calculadoras.Interacción_electrmagnética as Interaccion_Electromagnetica

# Using os.name
os_name = os.name
if os_name == 'nt':
    print("Windows OS detected")
    # URL del archivo de imagen en GitHub
    url = 'https://raw.githubusercontent.com/Gatmin50/Calculadora-de-problemas-de-dinamica/main/Icono.ico'

    # Directorio donde deseas guardar el archivo descargado
    directorio = 'C:/calculadora_de_dinamica/'
    ruta_local = os.path.join(directorio, 'Icono.ico')

    # Verificar si el directorio existe y, si no, crearlo
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    # Verificar si el archivo ya existe antes de descargarlo
    if not os.path.exists(ruta_local):
        try:
            # Descargar la imagen desde GitHub
            response = requests.get(url, stream=True)
            response.raise_for_status()
        
            # Guardar la imagen en la ruta local
            with open(ruta_local, 'wb') as file:
                shutil.copyfileobj(response.raw, file)
        except Exception as e:
            print(f"Error al descargar el archivo: {e}")
        else:
            print(f"El archivo ya existe en {ruta_local}")
elif os_name == 'posix':
    print("Linux or macOS OS detected")
else:
    print(f"Unknown OS: {os_name}")

# Using platform module (optional)
system = platform.system()
release = platform.release()
version = platform.version()

print(f"System: {system}")
print(f"Release: {release}")
print(f"Version: {version}")

#Intro.animacion_inicial()

# Crear la ventana del menu de la calculadora
ventana1 = ctk.CTk()
ventana1.title("Menu calculadora de Dinámica")
ventana1.configure(fg_color="black")
ctk.set_default_color_theme("dark-blue")
# Obtener el tamaño de la pantalla
screen_width = ventana1.winfo_screenwidth()
screen_height = ventana1.winfo_screenheight()
# Establecer el tamaño de la ventana para que ocupe toda la pantalla
ventana1.geometry(f"{screen_width}x{screen_height}")
ventana1.iconbitmap(ruta_local)

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

def Electromagnetismo():
    Interaccion_Electromagnetica.electromagnetismo()

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
    boton_calculadora_nuclear.grid(column=2, row=3, columnspan=2, padx=10, pady=10)
    boton_calculadora_elctromagnética.grid(column=4, row=3, columnspan=2, padx=10, pady=10)
    ventana1.geometry('710x300+400+200')

btn_back = ctk.CTkButton(ventana1, text="Atras", font=("Helvetica", 10, "bold"), command=cerrar_ventana4)
btn_back.grid_remove()

def traspaso1():
    boton_calculadora_plano_inclinado.grid_remove()
    boton_calculadora_plano_inclinado_con_dos_cuerpos.grid_remove()
    boton_calculadora.grid_remove()
    boton_calculadora_te.grid_remove()
    btn_cerrar.grid_remove()
    boton_calculadora_ondas_armonicas.grid_remove()
    boton_calculadora_nuclear.grid_remove()
    boton_calculadora_elctromagnética.grid_remove()
    ventana1.title("Menu calculadora de Trabajo y Energía")
    combobox.grid(row=0, column=1, padx=10, pady=10)
    etiqueta_resultado.grid(row=1, column=1, padx=10, pady=10)
    etiqueta_seleccion.grid(row=0, column=0, padx=10, pady=10)
    btn_back.grid(column=0, row=2, columnspan=2, padx=10, pady=10)
    ventana1.geometry('390x150')

# Crear los botones de las calculadoras
boton_calculadora_plano_inclinado = ctk.CTkButton(ventana1, text="Calculadora de plano inclinado", command=programa_plano_inclinado , font=("Helvetica", 15, "bold"), corner_radius=20)
boton_calculadora_plano_inclinado.grid(column=0, row=0, padx=10, pady=10)
boton_calculadora_plano_inclinado_con_dos_cuerpos = ctk.CTkButton(ventana1, text="Calculadora de plano inclinado \n con dos cuerpos unidos", command=programa_plano_inclinado_con_dos_cuerpos , font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora_plano_inclinado_con_dos_cuerpos.grid(column=3, row=0, padx=10, pady=10)
boton_calculadora = ctk.CTkButton(ventana1, text="Calculadora", command=mini_calculadora , font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora.grid(column=0, row=1, padx=10, pady=10)
boton_calculadora_te = ctk.CTkButton(ventana1, text="Problemas de trabajo y energia", command=traspaso1 , font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora_te.grid(column=2, row=1, padx=10, pady=10)
boton_calculadora_ondas_armonicas = ctk.CTkButton(ventana1, text="Calculadora de \n ondas armonicas", command=Ondas, font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora_ondas_armonicas.grid(column=0, row=3, padx=10, pady=10)
boton_calculadora_nuclear = ctk.CTkButton(ventana1, text="Calculadora nuclear", command=nuclear, font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora_nuclear.grid(column=2, row=3, padx=10, pady=10)
boton_calculadora_elctromagnética = ctk.CTkButton(ventana1, text="Calculadora Electromagnética", command=Electromagnetismo, font=("Helvetica", 15, "bold"),corner_radius=20)
boton_calculadora_elctromagnética.grid(column=4, row=3, padx=10, pady=10)

def cerrar_ventana():
    ventana1.destroy()

btn_cerrar = ctk.CTkButton(ventana1, text="Cerrar ventana", font=("Helvetica", 10, "bold"), command=cerrar_ventana, corner_radius=20)
btn_cerrar.grid(column=2, row=5, columnspan=3, padx=10, pady=10, sticky='s')

# Mantiene la ventana simpre abierta hasta que el usuario la cierra
ventana1.mainloop()
