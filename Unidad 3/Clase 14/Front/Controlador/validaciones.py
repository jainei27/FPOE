import re 
from tkinter import messagebox
from Front.Views import interfaz
import requests

class Validaciones():
    
    def __init__(self):
        pass
    
    def ingresar_lapicero(self):
        marca = interfaz.txtMarca.get()
        color = interfaz.txtColor.get()
        tipo = interfaz.txtTipo.get()
        material = interfaz.txtMaterial.get()

        if not marca or not color or not tipo or not material:
            messagebox.showwarning("Error", "Por favor completa todos los campos.")
            return
        
        if (marca.lblAdvertencia1.winfo_viewable() or
            color.lblAdvertencia2.winfo_viewable() or
            tipo.lblAdvertencia3.winfo_viewable() or
            material.lblAdvertencia4.winfo_viewable()):
            messagebox.showwarning("Error", "Por favor completa todos los campos correctamente.")
            return

        data = {
            "marca": marca,
            "color": color,
            "tipo": tipo,
            "material": material
            }

        #url
        url = 'http://127.0.0.1:8000/v1/lapicero'

        try:
            response = requests.post(url, json=data)
            if response.status_code == 201:  
                messagebox.showinfo("Exito", "Información creada con exito")
            else:
                messagebox.showerror("Error", f"Error al agregar la información sobre el lapicero: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}") 

            
    def validarLetras(entrada):
        return re.match("^[a-zA-Z ]*$", entrada) is not None
    
    def validarNumeros(entrada):
        return re.match("^[0-9]{1,2}$", entrada) is not None and len(entrada) <= 2

    def Advertencia1(event=None):
        nuevoValor = event.widget.get()
        if not nuevoValor:
            event.widget.lblAdvertencia1.grid_remove() 
        elif not re.match("^[a-zA-Z ]*$", nuevoValor):    
            event.widget.lblAdvertencia1.grid(row=4, column=1)
        else:
            event.widget.lblAdvertencia1.grid_remove()
                
    def Advertencia2(event=None):
            nuevoValor = event.widget.get()
            if not nuevoValor:
                event.widget.lblAdvertencia2.grid_remove()
            elif not re.match("^[a-zA-Z ]*$", nuevoValor):    
                event.widget.lblAdvertencia2.grid(row=6, column=1)
            else:
                event.widget.lblAdvertencia2.grid_remove()
                
    def Advertencia3(event=None):
            nuevoValor = event.widget.get()
            if not nuevoValor:
                event.widget.lblAdvertencia3.grid_remove() 
            elif not re.match("^[a-zA-Z ]*$", nuevoValor):
                event.widget.lblAdvertencia3.grid(row=8, column=1) 
            else:
                event.widget.lblAdvertencia3.grid_remove() 
            
    def Advertencia4(event=None):
            nuevoValor = event.widget.get()
            if not nuevoValor:
                event.widget.lblAdvertencia4.grid_remove() 
            elif not re.match("^[a-zA-Z ]*$", nuevoValor):
                event.widget.lblAdvertencia4.grid(row=10, column=1) 
            else:
                event.widget.lblAdvertencia4.grid_remove()
