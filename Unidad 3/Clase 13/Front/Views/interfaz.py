import tkinter as tk
import re
from tkinter import messagebox
from Front.Controlador.validaciones import Validaciones
from Front.Controlador.peticiones import Peticiones

def PeticionIngresarLapicero():
    Peticiones.ingresar_lapicero(txtMarca, txtColor, txtTipo, txtMaterial)
    
def accion_consultar_boton(lblmarca, lblcolor, lbltipo, lblmaterial, entryid):
    resultado = Peticiones.consultar(entryid)
    lblmarca.config(text= resultado.get('marca'))
    lblcolor.config(text= resultado.get('color'))
    lbltipo.config(text= resultado.get('tipo'))
    lblmaterial.config(text= resultado.get('material'))

def accion_consultar_todo(marca, color, tipo, material):
    resultado = Peticiones.consultar_todo(marca, color, tipo, material)
    print(resultado[0].get('marca'))
    print(resultado)            

principal = tk.Tk()
principal.title('Lapicero')  

frame = tk.Frame(principal, padx=10, pady=10)
frame.pack()  

lblTitulo = tk.Label(frame, text='Ingresar Datos')
lblTitulo.grid(row=0, column=0, columnspan=2) 

lblMarca = tk.Label(frame, text='Marca:')
lblMarca.grid(row=1, column=0, padx=5, pady=5)  
lblColor = tk.Label(frame, text='Color:')
lblColor.grid(row=3, column=0, padx=5, pady=5)
lblTipo = tk.Label(frame, text='Tipo:')
lblTipo.grid(row=5, column=0, padx=5, pady=5)
lblMaterial = tk.Label(frame, text='Material:')
lblMaterial.grid(row=7, column=0, padx=5, pady=5)
#crear label para cuando se haga la consulta no se sobre escriba en la interfaz grafica para dentro de 8 días 

txtMarca = tk.Entry(frame, width=20)
txtMarca.grid(row=1, column=1, padx=5, pady=5)  
txtMarca.lblAdvertencia1 = tk.Label(frame, text='Solo se permiten letras', fg="red")
txtMarca.lblAdvertencia1.grid(row=2, column=1, sticky="w")
txtMarca.lblAdvertencia1.grid_remove()

txtColor = tk.Entry(frame, width=20)
txtColor.grid(row=3, column=1, padx=5, pady=5)
txtColor.lblAdvertencia2 = tk.Label(frame, text='Solo se permiten letras', fg="red")
txtColor.lblAdvertencia2.grid(row=4, column=1, sticky="w")
txtColor.lblAdvertencia2.grid_remove()

txtTipo = tk.Entry(frame, width=20)
txtTipo.grid(row=5, column=1, padx=5, pady=5)  
txtTipo.lblAdvertencia3 = tk.Label(frame, text='Solo se permiten letras', fg="red")
txtTipo.lblAdvertencia3.grid(row=6, column=1, sticky="w")
txtTipo.lblAdvertencia3.grid_remove()

txtMaterial = tk.Entry(frame, width=20)
txtMaterial.grid(row=7, column=1, padx=5, pady=5)
txtMaterial.lblAdvertencia4 = tk.Label(frame, text='Solo se permiten letras', fg="red")
txtMaterial.lblAdvertencia4.grid(row=8, column=1, sticky="w")
txtMaterial.lblAdvertencia4.grid_remove()

txtentryid = tk.Entry(frame, width=20)
txtentryid.grid(row=8, column=1, padx=5, pady=5)

def ingresarLapicero():
    marca = txtMarca.get()
    color = txtColor.get()
    tipo = txtTipo.get()
    material = txtMaterial.get()
    messagebox.showinfo("Información de Lapicero", f"Marca: {marca}\nColor: {color}\nTipo: {tipo}\nMaterial: {material}")
    
txtMarca.bind('<KeyRelease>', Validaciones.Advertencia1)
txtColor.bind('<KeyRelease>', Validaciones.Advertencia2)
txtTipo.bind('<KeyRelease>', Validaciones.Advertencia3)
txtMaterial.bind('<KeyRelease>', Validaciones.Advertencia4)

btnIngresar = tk.Button(frame, text='Ingresar', command=PeticionIngresarLapicero)
btnIngresar.grid(row=10, column=1, columnspan=2, pady=10)

boton_consultar1 = tk.Button(frame, text="consultar1", command=lambda: accion_consultar_boton(lblMarca, lblColor, lblTipo, lblMaterial, txtentryid.get()))
boton_consultar1.grid(row=12, column=1, columnspan=2, pady=10)

boton_consultar_todos = tk.Button(frame, text="consultar todos", command=lambda: accion_consultar_todo(txtMarca.get(), txtColor.get(), txtTipo.get(), txtMaterial.get()))
boton_consultar_todos.grid(row=13, column=1, columnspan=2, pady=10)

principal.mainloop()