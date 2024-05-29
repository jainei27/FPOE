import tkinter as tk

class Usuario():
    
    def __init__(self, frame):
        self.frame = frame
        self.id = tk.StringVar(frame)
        self.marca = tk.StringVar(frame)
        self.color = tk.StringVar(frame)
        self.tipo = tk.StringVar(frame)
        self.material = tk.StringVar(frame)