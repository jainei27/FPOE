import requests

class Peticiones():
    
    def __init__(self, frame):
        self.url = 'http://127.0.0.1:8000/v1/lapicero'
        self.frame = frame
        pass
    
    def guardar(self, marca, color, tipo, material):
        try:
            print(marca, color, tipo, material)
            data = {
                "marca": marca,
                "color": color,
                "tipo": tipo,
                "material": material
            }   
            resultado = requests.post(self.url, json=data)
            print(resultado.json)
            return resultado
        except:
            pass


    def actualizar(self, id, marca, color, tipo, material):
        try:
            print(marca, color, tipo, material)
            data = {
                'marca': marca,
                'color': color,
                'tipo': tipo,
                'material': material
            }
            resultado = requests.put(self.url + '/' + id + '/', json=data)
            print(resultado.json)
            return resultado
        except:
            pass

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code

    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        print(resultado.text)
        print(resultado.status_code)
        try:
            return resultado.json()
        except ValueError:
            print("Respuesta no es un JSON válido.")
            return None
    
    def consultar_todo(self, marca, color, tipo, material):
        url = self.url + "?"
        print(type(marca))
        if marca != '':
            url = url + 'marca=' + str(marca) + "&"
        if color != '':
            url = url + 'color=' + str(color) + "&"
        if tipo != '':
            url = url + 'tipo=' + str(tipo) + "&"
        if material != '':
            url = url + 'material=' + str(material) + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()