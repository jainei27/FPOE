import tkinter as tk
from Front.Controlador.validaciones import Validaciones
from Front.Controlador.peticiones import Peticiones
from .tabla import Tabla
from Front.modelos.modelo import Usuario
from tkinter import messagebox

class Interfaz():

    def __init__(self):
        titulos = ['Identificador', 'Marca', 'Color', 'Tipo', 'Material']
        columnas = ['id', 'Marca', 'Color', 'Tipo', 'Material']
        data = []
        self.frame = tk.Tk()
        self.peticiones = Peticiones(self.frame)
        self.tabla = Tabla(self.frame, titulos, columnas, data)

    def limpiar_entradas(self):
        self.txtMarca.delete(0, tk.END)
        self.txtColor.delete(0, tk.END)
        self.txtTipo.delete(0, tk.END)
        self.txtMaterial.delete(0, tk.END)
        self.txtId.delete(0, tk.END)

    def acción_guardar_boton(self, marca, color, tipo, material, error_marca, error_color, error_tipo, error_material):
        marca_msg = Validaciones.Advertencia1(marca)
        color_msg = Validaciones.Advertencia2(color)
        tipo_msg = Validaciones.Advertencia3(tipo)
        material_msg = Validaciones.Advertencia4(material)

        if marca_msg or  color_msg or  tipo_msg or  material_msg:
            error_marca.config(text= marca_msg or "")
            error_color.conifg(text= color_msg or "")
            error_tipo.donfig(text= tipo_msg or "")
            error_material.config(text= material_msg or "")
            messagebox.showwarning("Error", "Por favor, complete todos los campos correctamente")

        else:
            self.comunicacion.guardar(marca, color, tipo, material)
            error_marca.config(text="")
            error_color.config(text="")
            error_tipo.config(text="")
            error_material.config(text="")
            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Los datos han sido guardados correctamente.")

    def actualizar_boton(self, id, marca, color, tipo, material):
        if id == '':
            self.peticiones.guardar(marca, color, tipo, material)
        else:
            self.peticiones.actualizar(id, marca, color, tipo, material)

    def accion_consultar_boton(self, lblMarcaConsulta, lblColorConsulta, lblTipoConsulta, lblMaterialConsulta, id):
        resultado = self.peticiones.consultar(id)
        lblMarcaConsulta.config(text= resultado.get('marca'))
        lblColorConsulta.config(text= resultado.get('color'))
        lblTipoConsulta.config(text= resultado.get('tipo'))
        lblMaterialConsulta.config(text= resultado.get('material'))
        

    def accion_consultar_todo(self, marca, color, tipo, material):
        resultado = self.peticiones.consultar_todo(marca, color, tipo, material)
        data = []
        print(resultado)
        print(type(resultado))
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('marca'), elemento.get('color'), elemento.get('tipo'), elemento.get('material')))
        self.tabla.refrescar(data)

    def mostrar_interfaz(self):
        
        usuario = Usuario(self.frame)

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                txtId.delete(0, tk.END)
                txtId.insert(0, str(valores[0]))
                txtMarca.delete(0, tk.END)
                txtMarca.insert(0, str(valores[1]))
                txtColor.delete(0, tk.END)
                txtColor.insert(0, str(valores[2]))
                txtTipo.delete(0, tk.END)
                txtTipo.insert(0, str(valores[3]))
                txtMaterial.delete(0, tk.END)
                txtMaterial.insert(0, str(valores[4]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.peticiones.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        lblId = tk.Label(self.frame, text= "ID: ")
        lblMarca = tk.Label(self.frame, text='Marca:')
        lblColor = tk.Label(self.frame, text='Color:')
        lblTipo = tk.Label(self.frame, text='Tipo:')
        lblMaterial = tk.Label(self.frame, text='Material:')
        lblMarcaConsulta = tk.Label(self.frame, text='')
        lblColorConsulta = tk.Label(self.frame, text='')
        lblTipoConsulta = tk.Label(self.frame, text='')
        lblMaterialConsulta = tk.Label(self.frame, text='')
        error_marca = tk.Label(self.frame, text='')
        error_color = tk.Label(self.frame, text='')
        error_tipo = tk.Label(self.frame, text='')
        error_material = tk.Label(self.frame, text='')

        txtId = tk.Entry(self.frame, width=20, textvariable=usuario.id)

        txtMarca = tk.Entry(self.frame, width=20, textvariable=usuario.marca)
        txtMarca.lblAdvertencia1 = tk.Label(self.frame, text='Solo se permiten letras', fg="red")
        txtMarca.lblAdvertencia1.grid(row=4, column=1, sticky="w")
        txtMarca.lblAdvertencia1.grid_remove()

        txtColor = tk.Entry(self.frame, width=20, textvariable=usuario.color)
        txtColor.lblAdvertencia2 = tk.Label(self.frame, text='Solo se permiten letras', fg="red")
        txtColor.lblAdvertencia2.grid(row=6, column=1, sticky="w")
        txtColor.lblAdvertencia2.grid_remove()

        txtTipo = tk.Entry(self.frame, width=20, textvariable=usuario.tipo) 
        txtTipo.lblAdvertencia3 = tk.Label(self.frame, text='Solo se permiten letras', fg="red")
        txtTipo.lblAdvertencia3.grid(row=8, column=1, sticky="w")
        txtTipo.lblAdvertencia3.grid_remove()

        txtMaterial = tk.Entry(self.frame, width=20, textvariable=usuario.material)
        txtMaterial.lblAdvertencia4 = tk.Label(self.frame, text='Solo se permiten letras', fg="red")
        txtMaterial.lblAdvertencia4.grid(row=10, column=1, sticky="w")
        txtMaterial.lblAdvertencia4.grid_remove()
                
        txtMarca.bind('<KeyRelease>', Validaciones.Advertencia1)
        txtColor.bind('<KeyRelease>', Validaciones.Advertencia2)
        txtTipo.bind('<KeyRelease>', Validaciones.Advertencia3)
        txtMaterial.bind('<KeyRelease>', Validaciones.Advertencia4)

        boton_actualizar = tk.Button(self.frame, text='Actualizar', command=lambda: self.limpiar_y_actualizar_y_consultar(self.txtId.get(), self.txtMarca.get(), self.txtColor.get(), self.txtTipo.get(), self.txtMaterial.get()))

        boton_guardar = tk.Button(self.frame, text="Guardar", command=lambda: self.guardar_y_limpiar_y_consultar(self.txtMarca.get(), self.txtColor.get(), self.txtTipo.get(), self.txtMaterial.get(), error_marca, error_color, error_tipo, error_material))

        boton_consultar1 = tk.Button(self.frame, text="consultar1", command=lambda: self.accion_consultar_boton(lblMarcaConsulta, lblColorConsulta, lblTipoConsulta, lblMaterialConsulta, self.txtId.get()))

        boton_consultar_todos = tk.Button(self.frame, text="consultar todos", command=lambda: self.accion_consultar_todo(self.txtMarca.get(), self.txtColor.get(), self.txtTipo.get(), self.txtMaterial.get()))

        boton_limpiar = tk.Button(self.frame, text="Limpiar", command=lambda: self.limpiar_entradas())

        self.frame.title("Ventana Principal")
        self.frame.geometry("1000x1000")
        lblId.pack()
        txtId.pack()
        lblMarca.pack()
        txtMarca.pack()
        lblColor.pack()
        txtColor.pack()
        lblTipo.pack()
        txtTipo.pack()
        lblMaterial.pack()
        txtMaterial.pack()
        boton_actualizar.pack()
        boton_consultar1.pack()
        boton_consultar_todos.pack()
        boton_limpiar.pack()
        boton_guardar.pack()
        self.tabla.tabla.pack()

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        self.frame.mainloop()

    def limpiar_y_actualizar_y_consultar(self, Id, marca, color, tipo, material):
        self.limpiar_entradas()
        self.actualizar_boton(Id,marca, color, tipo, material)
        self.accion_consultar_todo(marca, color, tipo, material)
    
    def guardar_y_limpiar_y_consultar(self, marca, color, tipo, material, error_marca, error_color, error_tipo, error_material):
        self.accion_guardar_boton(marca, color, tipo, material, error_marca, error_color, error_tipo, error_material)

        self.limpiar_entradas()
        
        self.accion_consultar_todo(marca, color, tipo, material)