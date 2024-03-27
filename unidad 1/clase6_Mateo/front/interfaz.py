import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
import re

def validar_marca(event):
    contenido = entrada_marca.get()
    if not re.match("^[a-zA-Z ]+$", contenido):
        etiquetaMarca.config(text="Error: Solo se permiten letras y espacios en la marca.")
    else:
        etiquetaMarca.config(text="")

def validar_color(event):
    contenido = entrada_color.get()
    if not re.match("^[a-zA-Z ]+$", contenido):
        etiquetaColor.config(text="Error: Solo se permiten letras y espacios en el color.")
    else:
        etiquetaColor.config(text="")

def validar_tipo(event):
    contenido = entrada_tipo.get()
    if not re.match("^[a-zA-Z ]+$", contenido):
        etiquetaTipo.config(text="Error: Solo se permiten letras y espacios en el tipo.")
    else:
        etiquetaTipo.config(text="")

def validar_material(event):
    contenido = entrada_material.get()
    if not re.match("^[a-zA-Z ]+$", contenido):
        etiquetaMaterial.config(text="Error: Solo se permiten letras y espacios en el material.")
    else:
        etiquetaMaterial.config(text="")

def validar_todo():
    contenido_nombre = entrada_marca.get()
    contenido_apellido = entrada_color.get()
    contenido_correo = entrada_tipo.get()
    contenido_fecha = entrada_material.get()

    if (re.match("^[a-zA-Z ]+$", contenido_marca) and
        re.match("^[a-zA-Z ]+$", contenido_color) and
        re.match("^[a-zA-Z ]+$", contenido_tipo) and
        re.match("^[a-zA-Z ]+$", contenido_material)):
        return True
    else:
        return False

def guardar():
    if validar_todo():
        messagebox.showerror("Valido","completado correctamente.")
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Validación de entrada")

# Crear etiquetas y entradas
etiqueta_marca = tk.Label(ventana, text="Marca:")
etiqueta_marca.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Crear etiqueta para mostrar error nombre
etiquetaMarca = tk.Label(ventana, fg="red")
etiquetaMarca.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

entrada_marca = tk.Entry(ventana)
entrada_marca.grid(row=0, column=1, padx=10, pady=5)
entrada_marca.bind("<KeyRelease>", validar_marca)

# Crear etiquetas y entradas
etiqueta_color = tk.Label(ventana, text="Color:")
etiqueta_color.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Crear etiqueta para mostrar error nombre
etiquetaColor = tk.Label(ventana, fg="red")
etiquetaColor.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

entrada_color = tk.Entry(ventana)
entrada_color.grid(row=0, column=1, padx=10, pady=5)
entrada_color.bind("<KeyRelease>", validar_color)

# Crear etiquetas y entradas
etiqueta_tipo = tk.Label(ventana, text="Tipo:")
etiqueta_tipo.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Crear etiqueta para mostrar error nombre
etiquetaTipo = tk.Label(ventana, fg="red")
etiquetaTipo.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

entrada_tipo = tk.Entry(ventana)
entrada_tipo.grid(row=0, column=1, padx=10, pady=5)
entrada_tipo.bind("<KeyRelease>", validar_tipo)

# Crear etiquetas y entradas
etiqueta_material = tk.Label(ventana, text="Material:")
etiqueta_material.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Crear etiqueta para mostrar error nombre
etiquetaMaterial = tk.Label(ventana, fg="red")
etiquetaMaterial.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

entrada_material = tk.Entry(ventana)
entrada_material.grid(row=0, column=1, padx=10, pady=5)
entrada_material.bind("<KeyRelease>", validar_material)

# Botón de guardar
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar)
boton_guardar.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()