import tkinter as tk
from tkinter import messagebox

import re

def validar_nombre(pantalla):
    nombre = pantalla.get()
    if re.match(r'^[a-zA-Z]+(?: [a-zA-Z]+)?$', nombre):
        return True
    else:
        messagebox.showerror("Error", "El nombre solo debe contener letras y máximo un espacio entre nombres")
        return False

def validar_apellido(pantalla):
    apellido = pantalla.get()
    if re.match(r'^[a-zA-Z]+(?: [a-zA-Z]+)?$', apellido):
        return True
    else:
        messagebox.showerror("Error", "El apellido solo debe contener letras y máximo un espacio entre nombres")
        return False

def validar_correo(pantalla):
    correo = pantalla.get()
    if "@" in correo and all(char.isalnum() or char == "@" or char == "." for char in correo):
        return True
    else:
        messagebox.showerror("Error", "El correo debe contener solo letras, números, el símbolo '@' y el punto '.'")
        return False

def validar_edad(pantalla):
    if pantalla.get().isdigit():
        return True
    else:
        messagebox.showerror("Error", "La edad debe ser un número")
        return False

def validar_fecha_nacimiento(pantalla):
    fecha = pantalla.get().split('/')
    if len(fecha) == 3 and all(part.isdigit() for part in fecha):
        dia, mes, anio = map(int, fecha)
        if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= anio <= 2100:
            return True
    messagebox.showerror("Error", "La fecha de nacimiento debe seguir el formato DD/MM/YYYY y ser válida")
    return False

def validar_todo():
    return (validar_nombre(nombre_usuario) and validar_apellido(apellido_usuario) and
            validar_correo(correo_usuario) and validar_edad(edad_usuario) and
            validar_fecha_nacimiento(fecha_nacimiento_usuario))

def salir():
    respuesta = messagebox.askyesno("Salir", "¿Estás seguro que quieres salir?")
    if respuesta:
        ventana.quit()

# Crear ventana
ventana = tk.Tk()
ventana.title("Formulario de Registro")

# Nombre
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=5, pady=5)
nombre_usuario = tk.Entry(ventana)
nombre_usuario.grid(row=0, column=1, padx=5, pady=5)

# Apellido
apellido_label = tk.Label(ventana, text="Apellido:")
apellido_label.grid(row=1, column=0, padx=5, pady=5)
apellido_usuario = tk.Entry(ventana)
apellido_usuario.grid(row=1, column=1, padx=5, pady=5)

# Correo
correo_label = tk.Label(ventana, text="Correo:")
correo_label.grid(row=2, column=0, padx=5, pady=5)
correo_usuario = tk.Entry(ventana)
correo_usuario.grid(row=2, column=1, padx=5, pady=5)

# Edad
edad_label = tk.Label(ventana, text="Edad:")
edad_label.grid(row=3, column=0, padx=5, pady=5)
edad_usuario = tk.Entry(ventana)
edad_usuario.grid(row=3, column=1, padx=5, pady=5)

# Fecha de Nacimiento
fecha_nacimiento_label = tk.Label(ventana, text="Fecha de Nacimiento:")
fecha_nacimiento_label.grid(row=4, column=0, padx=5, pady=5)
fecha_nacimiento_usuario = tk.Entry(ventana)
fecha_nacimiento_usuario.grid(row=4, column=1, padx=5, pady=5)

# Botón de enviar
enviar_boton = tk.Button(ventana, text="Guardar", command=lambda: messagebox.showinfo("Validación", "Información enviada correctamente") if validar_todo() else None)
enviar_boton.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Botón de salir
salir_boton = tk.Button(ventana, text="Salir", command=salir)
salir_boton.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()