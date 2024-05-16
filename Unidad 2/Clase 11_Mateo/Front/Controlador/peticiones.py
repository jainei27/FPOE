import requests
from tkinter import messagebox
from Front.Controlador.validaciones import Validaciones
from Front.Views import interfaz

class Peticiones():
    def ingresar_lapicero(txtMarca, txtColor, txtTipo, txtMaterial):
        marca = txtMarca.get()
        color = txtColor.get()
        tipo = txtTipo.get()
        material = txtMaterial.get()

        if not marca or not color or not tipo or not material:
            messagebox.showwarning("Error", "Por favor completa todos los campos.")
            return
        
        if (txtMarca.lblAdvertencia1.winfo_viewable() or
            txtColor.lblAdvertencia2.winfo_viewable() or
            txtTipo.lblAdvertencia3.winfo_viewable() or
            txtMaterial.lblAdvertencia4.winfo_viewable()):
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
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")