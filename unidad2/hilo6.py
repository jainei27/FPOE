import threading
import time

class Hilo6(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        while True:
            nombre = input("Por favor, ingresa tu nombre: ")
            print(nombre)
            with open("nombres.txt", "a") as archivo:
                archivo.write(nombre + "\n")
            time.sleep(5)