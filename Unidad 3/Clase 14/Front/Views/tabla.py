from tkinter import ttk
import tkinter as tk

class Tabla():
    
    def __init__(self, frame, titulos, columnas, data):
        self.tabla = ttk.Treeview(frame, columns= columnas, show ='headings')
        for posicion in range(0, len(columnas)):
            self.tabla.heading(columnas[posicion], text=titulos[posicion])
        for elemento in data:
            self.tabla.insert(parent='', index=0, values=elemento)

    def refrescar(self, data):
        self.tabla.delete(*self.tabla.get_children())
        for elemento in data:
            self.tabla.insert(parent='', index=tk.END, values=elemento)