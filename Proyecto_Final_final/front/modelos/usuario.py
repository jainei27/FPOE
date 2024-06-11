import tkinter as tk

class Usuario():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = tk.StringVar(ventanaPrincipal)
        self.nombre = tk.StringVar(ventanaPrincipal)
        self.apellido = tk.StringVar(ventanaPrincipal)
        self.cedula = tk.StringVar(ventanaPrincipal)
        self.telefono =tk.StringVar(ventanaPrincipal)
        self.correo =tk.StringVar(ventanaPrincipal)



        self.nombre_del_servicio = tk.StringVar(ventanaPrincipal)
        self.cedula_servicio = tk.StringVar(ventanaPrincipal)
        self.descripcion = tk.StringVar(ventanaPrincipal)
        self.valor =tk.StringVar(ventanaPrincipal)