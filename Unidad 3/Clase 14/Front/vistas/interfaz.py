import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.usuario import Usuario
from controladores.validaciones import Validaciones
from tkinter import messagebox
from .tabla import Tabla

class Interfaz:

    def __init__(self):
        titulos = ['Identificador','Marca' ,'Color' ,'Tipo' ,'Material']
        comlumnas = ['id','marca' ,'color' ,'tipo' ,'material' ]
        data = []
        self.ventanaPrincipal = tk.Tk()
        #self.ventanaPrincipal.resizable(0, 0)
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.ventanaPrincipal.state("zoomed")
        self.tabla = Tabla(self.ventanaPrincipal, titulos, comlumnas, data)
        self.ventanaPrincipal.config(bg="light blue")

    def validar_entrada(self, valor, etiqueta_error):
        mensaje_error = Validaciones.validarLetrasNumeros(valor)
        if mensaje_error:
            etiqueta_error.config(text=mensaje_error)
        else:
            etiqueta_error.config(text="")
    
    def limpiar_entradas(self):
        self.entrymarca.delete(0, tk.END)
        self.entrycolor.delete(0, tk.END)
        self.entrytipo.delete(0, tk.END)
        self.entrymaterial.delete(0, tk.END)
        self.entryId.delete(0, tk.END)

    def accion_guardar_boton(self, marca, color, tipo, material, marca_error, color_error, tipo_error, material_error):
        # Validaciones
        marca_msg = Validaciones.validarLetrasNumeros(marca)
        color_msg = Validaciones.validarLetrasNumeros(color)
        tipo_msg = Validaciones.validarLetrasNumeros(tipo)
        material_msg = Validaciones.validarLetrasNumeros(material)
        
        if marca_msg or color_msg or tipo_msg or material_msg:
            marca_error.config(text=marca_msg or "")
            color_error.config(text=color_msg or "")
            tipo_error.config(text=tipo_msg or "")
            material_error.config(text=material_msg or "")
            # Mostrar un mensaje de error general si algún campo no es válido
            messagebox.showwarning("Error", "Por favor, complete todos los campos correctamente.")
        else:
            self.comunicacion.guardar(marca, color, tipo, material)
            marca_error.config(text="")
            color_error.config(text="")
            tipo_error.config(text="")
            material_error.config(text="")
            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Los datos han sido guardados correctamente.")
        
    
    def actualizar_boton(self, id, marca, color, tipo, material):
        
        if id == '':
            self.comunicacion.guardar( marca, color, tipo, material)
        
        else:
            self.comunicacion.actualizar(id, marca, color, tipo, material)

    def accion_consultar_boton(self, labelConsultamarca, labelConsultacolor, labelConsultatipo, labelConsultamaterial, id):
        resultado = self.comunicacion.consultar(id)
        labelConsultamarca.config(text=resultado.get('marca'))
        labelConsultacolor.config(text=resultado.get('color'))
        labelConsultatipo.config(text=resultado.get('tipo'))
        labelConsultamaterial.config(text=resultado.get('material'))
    
    def accion_consultar_todo(self, marca, color, tipo, material):
        resultado = self.comunicacion.consultar_todo(marca, color, tipo, material)
        data=[]
        print(resultado)
        print(type(resultado))
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('marca'), elemento.get('color'), elemento.get('tipo'), elemento.get('material')))
        self.tabla.refrescar(data)

    def mostrar_interfaz(self):
        usuario = Usuario(self.ventanaPrincipal)
        
        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                self.entryId.delete(0, tk.END)
                self.entryId.insert(0,str(valores[0]))
                self.entrymarca.delete(0, tk.END)
                self.entrymarca.insert(0,str(valores[1]))
                self.entrycolor.delete(0, tk.END)
                self.entrycolor.insert(0,str(valores[2]))             
                self.entrytipo.delete(0, tk.END)
                self.entrytipo.insert(0,str(valores[3]))
                self.entrymaterial.delete(0, tk.END)
                self.entrymaterial.insert(0,str(valores[4]))
                
        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

#Espacios de texto y entardas de texto principales
        labelmarca = tk.Label(self.ventanaPrincipal, text="Marca", bg="light blue", font=("arial", 12))
        self.entrymarca = tk.Entry(self.ventanaPrincipal, textvariable=usuario.marca)
        labelcolor = tk.Label(self.ventanaPrincipal, text="Color", bg="light blue", font=("arial", 12))
        self.entrycolor = tk.Entry(self.ventanaPrincipal, textvariable=usuario.color)
        labeltipo = tk.Label(self.ventanaPrincipal, text="Tipo", bg="light blue", font=("arial", 12))
        self.entrytipo = tk.Entry(self.ventanaPrincipal, textvariable=usuario.tipo)
        labelmaterial = tk.Label(self.ventanaPrincipal, text="Material", bg="light blue", font=("arial", 12))
        self.entrymaterial = tk.Entry(self.ventanaPrincipal, textvariable=usuario.material)
        labelId = tk.Label(self.ventanaPrincipal, text="ID", bg="light blue", font=("arial", 12))
        self.entryId = tk.Entry(self.ventanaPrincipal)

        labelConsultamarca = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultacolor = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultatipo = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultamaterial = tk.Label(self.ventanaPrincipal, text='',fg="red")

        #Etiquetas de error
        marca_error = tk.Label(self.ventanaPrincipal,bg="light blue", text="", fg="red")
        marca_error.place(x=260, y=20)
        color_error = tk.Label(self.ventanaPrincipal,bg="light blue", text="", fg="red")
        color_error.place(x=260, y=60)
        tipo_error = tk.Label(self.ventanaPrincipal,bg="light blue", text="", fg="red")
        tipo_error.place(x=260, y=100)
        material_error = tk.Label(self.ventanaPrincipal,bg="light blue", text="", fg="red")
        material_error.place(x=260, y=140)

        #Comandos con el teclado
        self.entrymarca.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entrymarca.get(), marca_error))
        self.entrycolor.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entrycolor.get(), color_error))
        self.entrytipo.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entrytipo.get(), tipo_error))
        self.entrymaterial.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entrymaterial.get(), material_error))

        boton_actualizar = tk.Button(self.ventanaPrincipal, bg="purple", text="Actualizar", command=lambda:
        self.limpiar_y_actualizar_y_consultar(self.entryId.get(), self.entrymarca.get(), self.entrycolor.get(), self.entrytipo.get(), self.entrymaterial.get()))
        
        boton_guardar = tk.Button(self.ventanaPrincipal, bg="purple",text="Guardar", command=lambda: 
        self.guardar_y_limpiar_y_consultar(self.entrymarca.get(), self.entrycolor.get(), self.entrytipo.get(), self.entrymaterial.get(), marca_error, color_error, material_error, tipo_error))
        
        boton_consultar_1 = tk.Button(self.ventanaPrincipal, bg="purple",text="Consultar 1", command=lambda:
        self.accion_consultar_boton(labelConsultamarca, labelConsultacolor, labelConsultamaterial, labelConsultatipo, self.entryId.get()))
        
        boton_limpiar = tk.Button(self.ventanaPrincipal, bg="purple",text="Limpiar", command= lambda:
        self.limpiar_entradas())
        
        boton_consultar_todos = tk.Button(self.ventanaPrincipal, bg="purple", text="Consultar todos", command=lambda:
        self.accion_consultar_todo(self.entrymarca.get(), self.entrycolor.get(), self.entrymaterial.get(), self.entrytipo.get()))
        self.accion_consultar_todo(self.entrymarca.get(), self.entrycolor.get(), self.entrymaterial.get(), self.entrytipo.get())
        self.accion_consultar_todo(self.entrymarca.get(), self.entrycolor.get(), self.entrymaterial.get(), self.entrytipo.get())

        self.ventanaPrincipal.title("Ventana Principal")
        self.ventanaPrincipal.geometry("400x400")

        #Coordenadas de las entradas y texto principal
        labelmarca.place(x=20, y=20)
        self.entrymarca.place(x=120, y=20)
        labelcolor.place(x=20, y=60)
        self.entrycolor.place(x=120, y=60)
        labeltipo.place(x=20, y=100)
        self.entrytipo.place(x=120, y=100)
        labelmaterial.place(x=20, y=140)
        self.entrymaterial.place(x=120, y=140)

        boton_guardar.config(bd=10)
        boton_consultar_1.config(bd=10)
        boton_consultar_todos.config(bd=10)
        boton_actualizar.config(bd=10)
        boton_limpiar.config(bd=10)

        boton_guardar.place(x=20, y=180)
        boton_consultar_1.place(x=100, y=180)
        boton_consultar_todos.place(x=200, y=180)
        boton_actualizar.place(x=320, y=180)
        boton_limpiar.place(x=420, y=180)
        
        
        self.tabla.tabla.place(x=100, y=250, width=1200)
        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        labelId.place(x=400, y=20)
        self.entryId.place(x=430, y=20)

        self.ventanaPrincipal.mainloop()
    
    def limpiar_y_actualizar_y_consultar(self, Id, marca, color, tipo, material):
        self.limpiar_entradas()
        self.actualizar_boton(Id,marca, color, tipo, material)
        self.accion_consultar_todo(marca, color, tipo, material)
    
    def guardar_y_limpiar_y_consultar(self, marca, color, tipo, material, marca_error, color_error, tipo_error, material_error):
        self.accion_guardar_boton(marca, color, tipo, material, marca_error, color_error, tipo_error, material_error)

        self.limpiar_entradas()
        
        self.accion_consultar_todo(marca, color, tipo, material)