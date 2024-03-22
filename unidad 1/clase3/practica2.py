import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
import re
from datetime import datetime

def validar_nombre(event):
    contenido = entrada_nombre.get()
    if not re.match("^[a-zA-Z ]+$", contenido):
        etiquetaNombre.config(text="Error: Solo se permiten letras y espacios en el nombre.")
    else:
        etiquetaNombre.config(text="")

def validar_apellido(event):
    contenido = entrada_apellido.get()
    if not re.match("^[a-zA-Z ]+$", contenido):
        etiquetaApellido.config(text="Error: Solo se permiten letras y espacios en el apellido.")
    else:
        etiquetaApellido.config(text="")

def validar_edad(event):
    contenido = entrada_edad.get()
    if not contenido.isdigit():
        etiquetaEdad.config(text="Error: Solo se permiten números en la edad.")
    else:
        etiquetaEdad.config(text="")

def validar_correo(event):
    contenido = entrada_correo.get()
    if not all(c.isalnum() or c == '@' for c in contenido):
        etiquetaCorreo.config(text="Error: Formato de correo no válido.")
    else:
        etiquetaCorreo.config(text="")

def validar_fecha(event):
    contenido = entrada_fecha.get()
    if not all(c.isdigit() or c == '/' for c in contenido):
        etiquetaFecha.config(text="Error: Formato de fecha no válido.")
    else:
        fecha_ingresada = datetime.strptime(contenido, '%d/%m/%Y')
        fecha_actual = datetime.now()
        if fecha_ingresada > fecha_actual:
            etiquetaFecha.config(text="Error: La fecha de nacimiento no puede ser mayor que la fecha actual.")
        else:
            etiquetaFecha.config(text="")

def validar_todo():
    contenido_nombre = entrada_nombre.get()
    contenido_apellido = entrada_apellido.get()
    contenido_correo = entrada_correo.get()
    contenido_fecha = entrada_fecha.get()

    if (re.match("^[a-zA-Z ]+$", contenido_nombre) and
        re.match("^[a-zA-Z ]+$", contenido_apellido) and
        all(c.isalnum() or c == '@' for c in contenido_correo) and
        all(c.isdigit() or c == '/' for c in contenido_fecha)):
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
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Crear etiqueta para mostrar error nombre
etiquetaNombre = tk.Label(ventana, fg="red")
etiquetaNombre.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1, padx=10, pady=5)
entrada_nombre.bind("<KeyRelease>", validar_nombre)

#apellido
etiqueta_apellido = tk.Label(ventana, text="Apellido:")
etiqueta_apellido.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Crear etiqueta para mostrar error apellido
etiquetaApellido = tk.Label(ventana, fg="red")
etiquetaApellido.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

entrada_apellido = tk.Entry(ventana)
entrada_apellido.grid(row=2, column=1, padx=10, pady=5)
entrada_apellido.bind("<KeyRelease>", validar_apellido)

#edad
etiqueta_edad = tk.Label(ventana, text="Edad:")
etiqueta_edad.grid(row=4, column=0, padx=10, pady=5, sticky="w")

entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=4, column=1, padx=10, pady=5)
entrada_edad.bind("<KeyRelease>", validar_edad)

# Crear etiqueta para mostrar error
etiquetaEdad = tk.Label(ventana, fg="red")
etiquetaEdad.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

#correo
etiqueta_correo = tk.Label(ventana, text="Correo electrónico:")
etiqueta_correo.grid(row=6, column=0, padx=10, pady=5, sticky="w")

# Crear etiqueta para mostrar error en el apellido
etiquetaCorreo = tk.Label(ventana, fg="red")
etiquetaCorreo.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

entrada_correo = tk.Entry(ventana)
entrada_correo.grid(row=6, column=1, padx=10, pady=5)
entrada_correo.bind("<KeyRelease>", validar_correo)

#fecha
etiqueta_fecha = tk.Label(ventana, text="Fecha de nacimiento (DD/MM/YYYY):")
etiqueta_fecha.grid(row=8, column=0, padx=10, pady=5, sticky="w")

# Crear etiqueta para mostrar error en la fecha
etiquetaFecha = tk.Label(ventana, fg="red")
etiquetaFecha.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

entrada_fecha = tk.Entry(ventana)
entrada_fecha.grid(row=8, column=1, padx=10, pady=5)
entrada_fecha.bind("<KeyRelease>", validar_fecha)

# Botón de guardar
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar)
boton_guardar.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()