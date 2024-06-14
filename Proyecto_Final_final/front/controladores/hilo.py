import threading
import time

class HiloActualizador:
    def __init__(self, comunicacion):
        self.comunicacion = comunicacion
        self.hilo = threading.Thread(target=self.tarea_periodica)
        self.hilo.daemon = True

    def iniciar_hilo(self):
        self.hilo.start()

    def tarea_periodica(self):
        while True:
            clientes = self.comunicacion.consultar_todo_clientes("", "", "", "", "")
            servicios = self.comunicacion.consultar_todo_servicios("", "", "", "")
            with open("datos_clientes_servicios.txt", "w") as archivo:
                archivo.write("Clientes:\n")
                for cliente in clientes:
                    archivo.write(f"{cliente}\n")
                archivo.write("Servicios:\n")
                for servicio in servicios:
                    archivo.write(f"{servicio}\n")
            print("Datos actualizados y guardados en 'datos_clientes_servicios.txt'")
            time.sleep(60)