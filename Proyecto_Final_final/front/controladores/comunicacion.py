import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://localhost:8000/v1/Servicios'
        self.url1 = 'http://localhost:8000/v1/Cliente'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    #guardar datos de cliente
    def guardar_clientes(self, nombre,apellido,cedula,telefono, correo):
        try:
            print(nombre,apellido,cedula,telefono, correo)

            data = {
                'nombre': nombre,
                'apellido': apellido,
                'cedula': cedula,
                'telefono': telefono,
                'correo': correo
            }
            resultado = requests.post(self.url1, json=data)
            print(resultado.json)
            return resultado

        except:
            pass

        #guardar datos de servicio
    def guardar_servicios(self, nombre_del_servicio, cedula_servicio, descripcion, valor):
        try:
            print(nombre_del_servicio, cedula_servicio, descripcion, valor)

            data = {
                'nombre': nombre_del_servicio,
                'cedula': cedula_servicio,
                'descripcion': descripcion,
                'valor': valor
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json)
            return resultado

        except:
            pass

    def consultar_cedula(self, cedula):
        resultado = requests.get(self.url1 + '?cedula=' + str(cedula))
        data = resultado.json()  

        if data and len(data) > 0:
            return True
        else:
            return False
 
    #actualizar datos de cliente
    def actualizar_clientes(self, id, nombre, apellido, cedula, telefono, correo):
        try:
            data = {
                'nombre': nombre,
                'apellido': apellido,
                'cedula': cedula,
                'telefono': telefono,
                'correo': correo
            }
            url = self.url1 + '/' + id + '/'
            print("URL de la solicitud PUT:", url)
            resultado = requests.put(url, json=data)
            if resultado.status_code == 200:
                print("Los datos se actualizaron correctamente.")
                return True
            else:
                print(f"Hubo un problema al actualizar los datos. Código de error: {resultado.status_code}")
                return False
        except requests.RequestException as e:
            print("Error al realizar la solicitud:", e)
            return False
        



    #actualizar datos de servicio
    def actualizar_servicios(self,id, nombre_del_servicio, cedula_servicio, descripcion, valor):
        try:
            print(nombre_del_servicio, cedula_servicio, descripcion, valor)
            data = {
                'nombre': nombre_del_servicio,
                'cedula': cedula_servicio,
                'descripcion': descripcion,
                'valor': valor,
            }
            resultado = requests.put(self.url + '/' + id + '/', json=data)
            print(resultado.json)
            return resultado

        except:
            pass
    
    def consultar_clientes(self, id):
        resultado = requests.get(self.url1 + '/' + str(id))
        return resultado.json()


    def consultar_servicios(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        return resultado.json()

    
    def eliminar_clientes(self, id):
        resultado = requests.delete(self.url1 + '/' + str(id))
        return resultado.status_code

    def eliminar_servicios(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code

    
    #consulta cliente
    def consultar_todo_clientes(self, nombre,apellido,cedula,telefono, correo):
        url = self.url1+ "?"
        print(type(cedula))

        if nombre != '':
            url = url + 'nombre=' + str(nombre) + "&"
        if apellido != '':
            url = url + 'apellido=' + str(apellido) + "&"
        if  cedula != '':
            url = url + 'cedula=' + str(cedula) + "&"
        if  telefono != '':
            url = url + 'telefono=' + str(telefono) + "&"
        if  correo != '':
            url = url + 'correo=' + str(correo) + "&"
        print(url)
        resultado = requests.get(url)
        print(resultado)
        return resultado.json()

    
    #consulta servicios
    def consultar_todo_servicios(self, nombre_del_servicio, cedula_servicio, descripcion, valor):
        url = self.url+ "?"
        print(type(cedula_servicio))

        if nombre_del_servicio != '':
            url = url + 'nombre del servicio=' + str(nombre_del_servicio) + "&"
        if cedula_servicio != '':
            url = url + 'cedula=' + str(cedula_servicio) + "&"
        if  descripcion != '':
            url = url + 'descripcion=' + str(descripcion) + "&"
        if  valor != '':
            url = url + 'valor=' + str(valor) + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()