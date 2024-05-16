import tkinter as tk
from tkinter import messagebox
from controllers.controlador import Controlador

class Vista:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("250x300+200+100")
        self.ventana.title("Interfaz Simple")
        self.ventana.resizable(0, 0)
        self.ventana.configure(bg="gray")
        
        self.controlador = Controlador()
        
        # Configuración de las entradas y etiquetas
        self.setup_entrada("nombre", self.validar_caracteres_nombre)
        self.setup_entrada("edad", self.validar_caracteres_edad)
        self.setup_entrada("altura", self.validar_caracteres_altura)
        self.setup_entrada("raza", self.validar_caracteres_raza)

        # Botón de validación
        self.button_validar = tk.Button(self.ventana, text="Validar", command=self.validar_datos)
        self.button_validar.pack()

    def setup_entrada(self, campo, validation_method):
        label = tk.Label(self.ventana, text=f"{campo.capitalize()}:")
        label.pack()
        entry = tk.Entry(self.ventana)
        entry.pack()
        label_error = tk.Label(self.ventana, text="", fg="red",bg="gray")
        label_error.pack()
        entry.bind("<KeyRelease>", validation_method)
        setattr(self, f"entry_{campo}", entry)
        setattr(self, f"label_error_{campo}", label_error)

    def validar_datos(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        altura = self.entry_altura.get()
        raza = self.entry_raza.get()

        resultado = self.controlador.validar_datos(nombre, edad, altura, raza)
        if resultado:
            messagebox.showinfo("Validación", "La información es válida.")
            resultado1 = self.controlador.enviar_datos(nombre, edad, altura, raza)
            resultado1
        else:
            messagebox.showerror("Validación", "La información no es válida.")

    def validar_caracteres_nombre(self, event):
        self.validar_caracteres_generico(self.entry_nombre, self.label_error_nombre)

    def validar_caracteres_edad(self, event):
        self.validar_caracteres_generico(self.entry_edad, self.label_error_edad)

    def validar_caracteres_altura(self, event):
        self.validar_caracteres_generico(self.entry_altura, self.label_error_altura)

    def validar_caracteres_raza(self, event):
        self.validar_caracteres_generico(self.entry_raza, self.label_error_raza)

    def validar_caracteres_generico(self, widget, label_error):
        texto = widget.get()
        if not self.controlador.validar_caracteres(texto):
            label_error.config(text="Solo caracteres válidos")
        else:
            label_error.config(text="")
