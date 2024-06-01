import tkinter as tk

class Usuario():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.marca = tk.StringVar(ventanaPrincipal)
        self.color = tk.StringVar(ventanaPrincipal)
        self.tipo = tk.StringVar(ventanaPrincipal)
        self.material =tk.StringVar(ventanaPrincipal)

