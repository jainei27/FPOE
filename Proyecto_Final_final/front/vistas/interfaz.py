import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.usuario import Usuario
from controladores.validaciones import Validaciones
from tkinter import messagebox
from vistas.tabla import Tabla

class Interfaz:

    def __init__(self):
        titulos_cliente = ['Identificador','Nombre','Apellido','Cedula','Telefono', 'Correo']
        columnas_cliente = ['id','nombre','apellido','cedula','telefono', 'correo']

        titulos_servicios = ['identificador','nombre del servicio','cedula','descripcion','valor']
        columnas_servicios= ['id','nombre','cedula','descripcion','valor']

        data = []
        data1 = []

        self.ventanaPrincipal = tk.Tk()
        self.ventanaPrincipal.geometry("1000x1000")
        #self.ventanaPrincipal.resizable(0, 0)
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.tabla = Tabla(self.ventanaPrincipal,titulos_cliente, columnas_cliente, data)
        self.tablas = Tabla(self.ventanaPrincipal,titulos_servicios, columnas_servicios, data1)

    def validar_entrada(self, valor, etiqueta_error):
        mensaje_error = Validaciones.validarLetrasNumeros(valor)
        if mensaje_error:
            etiqueta_error.config(text=mensaje_error)
        else:
            etiqueta_error.config(text="")

    def guardar_boton_cliente(self, nombre, apellido, cedula, telefono, correo, nombre_error, apellido_error, 
        cedula_servicio_error, telefono_error, correo_error):


        # Validaciones
        nombre_msg = Validaciones.validarLetrasNumeros(nombre)
        apellido_msg = Validaciones.validarLetrasNumeros(apellido)
        cedula_servicio_msg = Validaciones.validarLetrasNumeros(cedula)
        telefono_msg = Validaciones.validarLetrasNumeros(telefono)
        correo_msg = Validaciones.validarLetrasNumeros(correo)

        if nombre_msg or apellido_msg or cedula_servicio_msg or telefono_msg or correo_msg:
            nombre_error.config(text=nombre_msg or "")
            apellido_error.config(text=apellido_msg or "")
            cedula_servicio_error.config(text=cedula_servicio_msg or "")
            telefono_error.config(text=telefono_msg or "")
            correo_error.config(text=correo_msg or "")
            # Mostrar un mensaje de error general si algún campo no es válido
            messagebox.showwarning("Error", "Por favor, complete todos los campos correctamente.")
        else:
            self.comunicacion.guardar_clientes(nombre,apellido,cedula,telefono)
            nombre_error.config(text="")
            apellido_error.config(text="")
            cedula_servicio_error.config(text="")
            telefono_error.config(text="")
            correo_error.config(text="")
            # Mostrar un mensaje de éxito
            messagebox.showwarning("Éxito", "Los datos han sido guardados correctamente.")
            self.limpiar_cajas_clientes()
            self.consultar_todo_clientes(self.entryNombre.get(), self.entryApellido.get(), self.entryCedula.get(), self.entryTelefono.get(), self.entrycorreo.get()   )



    def guardar_boton_servicios(self, nombre_del_servicio, cedula_servicio, descripcion, valor, nombre_del_servicio_error, cedula_servicio_error, descripcion_error, valor_error):

        nombre_del_servicio_msg = Validaciones.validarLetrasNumeros(nombre_del_servicio)
        cedula_servicio_msg = Validaciones.validarLetrasNumeros(cedula_servicio)
        descripcion_msg = Validaciones.validarLetrasNumeros(descripcion)
        valor_msg = Validaciones.validarLetrasNumeros(valor)


        if nombre_del_servicio_msg or cedula_servicio_msg or descripcion_msg or valor_msg:
            nombre_del_servicio_error.config(text=nombre_del_servicio_msg or "")
            cedula_servicio_error.config(text=cedula_servicio_msg or "")
            descripcion_error.config(text=descripcion_msg or "")
            valor_error.config(text=valor_msg or "")
            # Mostrar un mensaje de error general si algún campo no es válido
            messagebox.showwarning("Error", "Por favor, complete todos los campos correctamente.")
        else:
            self.comunicacion.guardar_servicios(nombre_del_servicio,cedula_servicio,descripcion,valor)
            nombre_del_servicio_error.config(text="")
            cedula_servicio_error.config(text="")
            descripcion_error.config(text="")
            valor_error.config(text="")

            # Mostrar un mensaje de éxito
            messagebox.showwarning("Éxito", "Los datos han sido guardados correctamente.")
            self.limpiar_cajas_servicios()
            self.consultar_todo_servicios(self.entryNombre_del_servicio.get(), self.entryCedula_servicio.get(), self.entryDescripcion.get(), self.entryValor.get())

    

    def actualizar_clientes(self, id ,nombre,apellido,cedula,telefono,correo):
        if id =='':
            self.comunicacion.guardar_clientes(nombre,apellido,cedula,telefono,correo)

        
        else:
            self.comunicacion.actualizar_clientes(id, nombre,apellido,cedula,telefono,correo)
            self.limpiar_cajas_clientes()
            self.consultar_todo_clientes(self.entryNombre.get(), self.entryApellido.get(), self.entryCedula.get(), self.entryTelefono.get(), self.entrycorreo.get())





    def actualizar_servicios(self, id, nombre_del_servicio, cedula_servicio, descripcion, valor):
        if id =='':
            self.comunicacion.guardar_servicios(nombre_del_servicio, cedula_servicio, descripcion, valor)
        
        else:

            self.comunicacion.actualizar_servicios(id, nombre_del_servicio, cedula_servicio, descripcion, valor)
            self.limpiar_cajas_servicios()
            self.consultar_todo_servicios(self.entryNombre_del_servicio.get(), self.entryCedula_servicio.get(), self.entryDescripcion.get(), self.entryValor.get())



        

    def consultar_boton_clientes(self, id):
        resultados = self.comunicacion.consultar_clientes(id)
        print(resultados)




    def consultar_boton_servicios(self, id):
        resultado = self.comunicacion.consultar_servicios(id)
        print(resultado)



        
    
    def consultar_todo_clientes(self, nombre,apellido,cedula,telefono,correo):
        resultado = self.comunicacion.consultar_todo_clientes(nombre,apellido,cedula,telefono,correo)
        data= []


        for elemento in resultado:
            data.append((elemento.get('id'),elemento.get('nombre'), elemento.get('apellido'),elemento.get('cedula'),elemento.get('telefono'),elemento.get('correo')))
        self.tabla.refrescar(data)

        print(resultado)
        print(type(resultado))


    def consultar_todo_servicios(self, nombre_del_servicio,cedula_servicio,descripcion,valor):
        resultado = self.comunicacion.consultar_todo_servicios(nombre_del_servicio,cedula_servicio,descripcion,valor)
        data= []
        for elemento in resultado:

            data.append((elemento.get('id'),elemento.get('nombre_del_servicio'), 
                        elemento.get('cedula_servicio'),elemento.get('descripcion'),elemento.get('valor')))
        self.tablas.refrescar(data)

        print(resultado)
        print(type(resultado))



    def limpiar_cajas_clientes(self):
        self.entryNombre.delete(0,tk.END)
        self.entryApellido.delete(0,tk.END)
        self.entryCedula.delete(0,tk.END)
        self.entryTelefono.delete(0,tk.END)
        self.entryId.delete(0,tk.END)

    def limpiar_cajas_servicios(self):
        self.entryNombre_del_servicio.delete(0,tk.END)
        self.entryCedula_servicio.delete(0,tk.END)
        self.entryDescripcion.delete(0,tk.END)
        self.entryValor.delete(0,tk.END)

    def mostrar_interfaz(self):
        usuario = Usuario(self.ventanaPrincipal)

#Espacios de texto y entardas de texto principales
        labelNombre = tk.Label(self.ventanaPrincipal, text="Nombre")
        self.entryNombre = tk.Entry(self.ventanaPrincipal, textvariable=usuario.nombre)
        labelApellido = tk.Label(self.ventanaPrincipal, text="Apellido")
        self.entryApellido = tk.Entry(self.ventanaPrincipal, textvariable=usuario.apellido)
        labelCedula = tk.Label(self.ventanaPrincipal, text="Cedula")
        self.entryCedula = tk.Entry(self.ventanaPrincipal, textvariable=usuario.cedula)
        labelTelefono = tk.Label(self.ventanaPrincipal, text="Telefono")
        self.entryTelefono = tk.Entry(self.ventanaPrincipal, textvariable=usuario.telefono)
        labelCorreo= tk.Label(self.ventanaPrincipal, text="Correo")
        self.entryCorreo = tk.Entry(self.ventanaPrincipal, textvariable=usuario.telefono)

#epacios de texto de servicios
        labelNombre_del_servicio = tk.Label(self.ventanaPrincipal, text="Nombre servicio")
        self.entryNombre_del_servicio = tk.Entry(self.ventanaPrincipal, textvariable=usuario.nombre_del_servicio)
        labelCedula_servicio = tk.Label(self.ventanaPrincipal, text="Cedula")
        self.entryCedula_servicio = tk.Entry(self.ventanaPrincipal, textvariable=usuario.cedula_servicio)
        labelDescripcion = tk.Label(self.ventanaPrincipal, text="Descripcion")
        self.entryDescripcion = tk.Entry(self.ventanaPrincipal, textvariable=usuario.descripcion)
        labelValor = tk.Label(self.ventanaPrincipal, text="Valor")
        self.entryValor = tk.Entry(self.ventanaPrincipal, textvariable=usuario.valor)

        labelId = tk.Label(self.ventanaPrincipal, text="ID")
        self.entryId = tk.Entry(self.ventanaPrincipal)

        labelId_servicios = tk.Label(self.ventanaPrincipal, text="ID/Ser.")
        self.entryId_servicios = tk.Entry(self.ventanaPrincipal)


        #Etiquetas de error del usuario
        nombre_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        nombre_error.place(x=260, y=20)
        apellido_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        apellido_error.place(x=260, y=60)
        cedula_servicio_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        cedula_servicio_error.place(x=260, y=100)
        telefono_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        telefono_error.place(x=260, y=140)
        correo_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        correo_error.place(x=260, y=140)

        #Etiquetas de error del servicio
        nombre_del_servicio_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        nombre_del_servicio_error.place(x=260, y=20)
        cedula_servicio_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        cedula_servicio_error.place(x=260, y=60)
        descripcion_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        descripcion_error.place(x=260, y=100)
        valor_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        valor_error.place(x=260, y=140)

        #Comandos con el teclado usuario
        self.entryNombre.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryNombre.get(), nombre_error))
        self.entryApellido.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryApellido.get(), apellido_error))
        self.entryCedula.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryCedula.get(), cedula_servicio_error))
        self.entryTelefono.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryTelefono.get(), telefono_error))
        self.entryCorreo.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryCorreo.get(), correo_error))

        #Comandos con el teclado servicio
        self.entryNombre_del_servicio.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryNombre_del_servicio.get(), nombre_del_servicio_error))
        self.entryCedula_servicio.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryCedula_servicio.get(), cedula_servicio_error))
        self.entryDescripcion.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryDescripcion.get(), descripcion_error))
        self.entryValor.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryValor.get(), valor_error))

        boton_guardar_cliente = tk.Button(self.ventanaPrincipal, text="Guardar", command=lambda: 
        self.guardar_boton_cliente(self.entryNombre.get(), self.entryApellido.get(), self.entryCedula.get(), 
        self.entryTelefono.get(), self.entryCorreo.get(), nombre_error, apellido_error, cedula_servicio_error, telefono_error, correo_error))

        
        boton_guardar_servicio = tk.Button(self.ventanaPrincipal, text="Guardar", command=lambda: 
        self.guardar_boton_servicios(self.entryNombre_del_servicio.get(), self.entryCedula_servicio.get(), self.entryDescripcion.get(), 
        self.entryValor.get(), nombre_del_servicio_error, cedula_servicio_error, descripcion_error, valor_error))

        boton_consultar_1_cliente = tk.Button(self.ventanaPrincipal, text="Consultar 1", command=lambda:
        self.consultar_boton_clientes(self.entryId.get()))

        boton_consultar_1_servicio = tk.Button(self.ventanaPrincipal, text="Consultar 1", command=lambda:
        self.consultar_boton_servicios(self.entryId_servicios.get()))

        boton_consultar_todos_clientes = tk.Button(self.ventanaPrincipal, text="Consultar todos", command=lambda:
        self.consultar_todo_clientes(self.entryNombre.get(), self.entryApellido.get(), self.entryCedula.get(), 
        self.entryTelefono.get(), self.entryCorreo.get()))

        boton_consultar_todos_servicios = tk.Button(self.ventanaPrincipal, text="Consultar todos", command=lambda:
        self.consultar_todo_servicios(self.entryNombre_del_servicio.get(), self.entryCedula_servicio.get(), self.entryDescripcion.get(), 
        self.entryValor.get()))


        boton_actualizar_clientes = tk.Button(self.ventanaPrincipal, text="Actualizar", command=lambda: 
        self.actualizar_clientes(self.entryId.get(), self.entryNombre.get(), self.entryApellido.get(), self.entryCedula.get(), 
        self.entryTelefono.get(), self.entryCorreo.get()))

        boton_actualizar_servicio = tk.Button(self.ventanaPrincipal, text="Actualizar", command=lambda: 
        self.actualizar_servicios(self.entryId.get(), self.entryNombre_del_servicio.get(), self.entryCedula_servicio.get(), 
        self.entryDescripcion.get(), self.entryValor.get()))


        boton_limpiar_clientes = tk.Button(self.ventanaPrincipal, text="Limpiar", command=lambda:self.limpiar_cajas_clientes())

        boton_limpiar_servicios = tk.Button(self.ventanaPrincipal, text="Limpiar", command=lambda:self.limpiar_cajas_servicios())


    
        self.ventanaPrincipal.title("Ventana Principal")
        self.ventanaPrincipal.geometry("1000x1000")

        #Coordenadas de las entradas y texto principal de los clientes
        labelNombre.place(x=20, y=20)
        self.entryNombre.place(x=120, y=20)
        labelApellido.place(x=20, y=60)
        self.entryApellido.place(x=120, y=60)
        labelCedula.place(x=20, y=100)
        self.entryCedula.place(x=120, y=100)
        labelTelefono.place(x=20, y=140)
        self.entryTelefono.place(x=120, y=140)
        labelCorreo.place(x=20, y=180)
        self.entryCorreo.place(x=120, y=180)

        #Coordenadas de las entradas y texto principal de los servicios
        labelNombre_del_servicio.place(x=500, y=20)
        self.entryNombre_del_servicio.place(x=600, y=20)
        labelCedula_servicio.place(x=500, y=60)
        self.entryCedula_servicio.place(x=600, y=60)
        labelDescripcion.place(x=500, y=100)
        self.entryDescripcion.place(x=600, y=100)
        labelValor.place(x=500, y=140)
        self.entryValor.place(x=600, y=140)


        boton_guardar_cliente.place(x=20, y=210)
        boton_consultar_1_cliente.place(x=100, y=210)
        boton_consultar_todos_clientes.place(x=180, y=210)
        boton_actualizar_clientes.place(x=300, y=210)
        boton_limpiar_clientes.place(x=380, y=210)

        
        boton_guardar_servicio.place(x=500, y=210)
        boton_consultar_1_servicio.place(x=580, y=210)
        boton_consultar_todos_servicios.place(x=660, y=210)
        boton_actualizar_servicio.place(x=760, y=210)
        boton_limpiar_servicios.place(x=840, y=210)

        

        labelId.place(x=20, y=250)
        self.entryId.place(x=60, y=250)
        labelId_servicios.place(x=500, y=250)
        self.entryId_servicios.place(x=540, y=250)

        self.tabla.tabla.place(x=50,y=330)
        self.tablas.tabla.place(x=50,y=580)

        def seleccionar_elemento_clientes(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                self.entryId.delete(0,tk.END)
                self.entryId.insert(0, str(valores[0]))
                self.entryNombre.delete(0,tk.END)
                self.entryNombre.insert(0, str(valores[1]))
                self.entryApellido.delete(0,tk.END)
                self.entryApellido.insert(0, str(valores[2]))
                self.entryCedula.delete(0,tk.END)
                self.entryCedula.insert(0, str(valores[3]))
                self.entryTelefono.delete(0,tk.END)
                self.entryTelefono.insert(0, str(valores[4]))
                self.entryCorreo.delete(0,tk.END)
                self.entryCorreo.insert(0, str(valores[5]))
                
        def seleccionar_elemento_servicios(_):
            for i in self.tablas.tablas.selection():
                valores = self.tablas.tablas.item(i)['values']
                self.entryId.delete(0,tk.END)
                self.entryId.insert(0, str(valores[0]))
                self.entryNombre_del_servicio.delete(0,tk.END)
                self.entryNombre_del_servicio.insert(0, str(valores[1]))
                self.entryCedula_servicio.delete(0,tk.END)
                self.entryCedula_servicio.insert(0, str(valores[2]))
                self.entryDescripcion.delete(0,tk.END)
                self.entryDescripcion.insert(0, str(valores[3]))
                self.entryValor.delete(0,tk.END)
                self.entryValor.insert(0, str(valores[4]))

        def borrar_elemento_clientes(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar_clientes(self.tabla.tabla.item(i)['values'][0])

                self.tabla.tabla.delete(i)

        def borrar_elemento_servicios(_):
            for i in self.tablas.tablas.selection():
                self.comunicacion.eliminar_servicios(self.tablas.tablas.item(i)['values'][0])

                self.tablas.tablas.delete(i)

        self.tabla.tabla.bind('<<TreeviewSelect>>',seleccionar_elemento_clientes)
        self.tabla.tabla.bind('<Delete>',borrar_elemento_clientes)


        self.tablas.tabla.bind('<<TreeviewSelect>>',seleccionar_elemento_servicios)
        self.tablas.tabla.bind('<Delete>',borrar_elemento_servicios)


        self.consultar_todo_clientes(self.entryNombre.get(), self.entryApellido.get(), self.entryCedula.get(), self.entryTelefono.get(), self.entryCorreo.get())

        
        self.consultar_todo_servicios(self.entryNombre_del_servicio.get(), self.entryCedula_servicio.get(), self.entryDescripcion.get(), self.entryValor.get())


        self.ventanaPrincipal.mainloop()
