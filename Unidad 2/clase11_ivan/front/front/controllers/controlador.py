from models.modelo import Modelo
import re

class Controlador:
    def __init__(self):
        self.modelo = Modelo()

    def validar_datos(self, nombre, edad, altura, raza):
        self.modelo.set_nombre(nombre)
        self.modelo.set_edad(edad)
        self.modelo.set_altura(altura)
        self.modelo.set_raza(raza)

        return self.modelo.validar_datos()
    

    
    def validar_caracteres(self, texto):
        
        patron = re.compile(r'^[a-zA-Z0-9 ]+$')
        return bool(patron.match(texto))
    


    def enviar_datos(self, nombre, edad, altura, raza):
        self.modelo.set_nombre(nombre)
        self.modelo.set_edad(edad)
        self.modelo.set_altura(altura)
        self.modelo.set_raza(raza)

        return self.modelo.enviarDatos()
    

