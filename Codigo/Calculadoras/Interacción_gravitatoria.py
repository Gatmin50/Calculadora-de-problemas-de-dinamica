from cgitb import text
import tkinter as tk
import customtkinter as ctk
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import markers, patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


def gravitación():

    ventana13 = ctk.CTk()
    ventana13.title("Menu calculadora de Garvitación")
    ventana13.configure(fg_color="black")

    os_name = os.name
    if os_name == 'nt':
        screen_width = ventana13.winfo_screenwidth()
        screen_height = ventana13.winfo_screenheight()
        x_offset = 0
        y_offset = 0
        ventana13.geometry(f"{screen_width}x{screen_height}+{x_offset}+{y_offset}")
        directorio = 'C:/calculadora_de_dinamica/'
        ruta_local = os.path.join(directorio, 'Interacción_electromagnética.ico')
        ventana13.iconbitmap(ruta_local)
    elif os_name == 'posix':
        screen_width = ventana13.winfo_screenwidth()
        screen_height = ventana13.winfo_screenheight()
        ventana13.geometry(f"{screen_width}x{screen_height}")



    ventana13.mainloop()