import tkinter as tk
from tkinter import messagebox
import re
import requests

def validar_nombre(mascota):
    contenido = entrada_nombre.get()
    if not re.match("^[a-zA-Z ]+$", contenido):
        etiquetaNombre.config(text="Error: Solo se permiten letras y espacios en el nombre.")
    else:
        etiquetaNombre.config(text="")

def validar_edad(mascota):
    contenido = entrada_edad.get()
    if not re.match("^[0-9.]+$", contenido):
        etiquetaEdad.config(text="Error: Solo se permiten números en la edad.")
    else:
        etiquetaEdad.config(text="")

def validar_altura(mascota):
    contenido = entrada_altura.get()
    if not re.match("^[0-9.]+$", contenido):
        etiquetaAltura.config(text="Error: Solo se permiten números en la altura.")
    else:
        etiquetaAltura.config(text="")

def validar_raza(mascota):
    contenido = entrada_raza.get()
    if not re.match("^[a-zA-Z ]+$", contenido):
        etiquetaRaza.config(text="Error: Solo se permiten letras y espacios en la raza.")
    else:
        etiquetaRaza.config(text="")

def validar_todo():
    contenido_nombre = entrada_nombre.get()
    contenido_edad = entrada_edad.get()
    contenido_altura = entrada_altura.get()
    contenido_raza = entrada_raza.get()

    if (re.match("^[a-zA-Z ]+$", contenido_nombre) and 
        re.match("^[0-9.]+$", contenido_edad) and 
        re.match("^[0-9.]+$", contenido_altura) and
        re.match("^[a-zA-Z ]+$", contenido_raza)):

        return True
    else:
        return False

def guardar():
    if validar_todo():
        messagebox.showinfo("Valido", "Completado correctamente.")
        data = {
            "nombre": entrada_nombre.get(),
            "edad": entrada_edad.get(),
            "altura": entrada_altura.get(),
            "raza": entrada_raza.get()
        }

        try:
            response = requests.post("http://localhost:8000/v1/mascota", data=data)
            print(response.status_code)
            print(response.content)
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud:", e)
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Validación de entrada")

# Nombre
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")

etiquetaNombre = tk.Label(ventana, fg="red")
etiquetaNombre.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1, padx=10, pady=5)
entrada_nombre.bind("<KeyRelease>", validar_nombre)

# Edad
etiqueta_edad = tk.Label(ventana, text="Edad:")
etiqueta_edad.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=2, column=1, padx=10, pady=5)
entrada_edad.bind("<KeyRelease>", validar_edad)

etiquetaEdad = tk.Label(ventana, fg="red")
etiquetaEdad.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Altura
etiqueta_altura = tk.Label(ventana, text="Altura:")
etiqueta_altura.grid(row=4, column=0, padx=10, pady=5, sticky="w")

entrada_altura = tk.Entry(ventana)
entrada_altura.grid(row=4, column=1, padx=10, pady=5)
entrada_altura.bind("<KeyRelease>", validar_altura)

etiquetaAltura = tk.Label(ventana, fg="red")
etiquetaAltura.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Raza
etiqueta_raza = tk.Label(ventana, text="Raza:")
etiqueta_raza.grid(row=6, column=0, padx=10, pady=5, sticky="w")

entrada_raza = tk.Entry(ventana)
entrada_raza.grid(row=6, column=1, padx=10, pady=5)
entrada_raza.bind("<KeyRelease>", validar_raza)

etiquetaRaza = tk.Label(ventana, fg="red")
etiquetaRaza.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Botón de guardar
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar)
boton_guardar.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()
