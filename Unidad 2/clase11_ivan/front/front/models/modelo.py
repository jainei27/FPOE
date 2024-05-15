import re
import requests

response = requests.get("http://localhost:8000")

class Modelo:
    def __init__(self):
        self.nombre = ""
        self.edad = ""
        self.altura = ""
        self.raza = ""

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_altura(self, altura):
        self.altura = altura

    def set_raza(self, raza):
        self.raza = raza

    def validar_datos(self):
        if not re.match("^[a-zA-Z0-9 ]+$", self.nombre):
            return False
        if not re.match("^[a-zA-Z0-9 ]+$", self.edad):
            return False
        if not re.match("^[a-zA-Z0-9 ]+$", self.altura):
            return False
        if not re.match("^[a-zA-Z0-9 ]+$", self.raza):
            return False
        return True

    def enviarDatos(self):
        data = {
            "nombre": self.nombre,  
            "edad": self.edad,  
            "altura": self.altura,  
            "raza": self.raza  
        }

        response = requests.post("http://127.0.0.1:8000/v1/mascota",data)
        print(response.status_code)
        print(response.content)
