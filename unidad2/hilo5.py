import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG)

class Hilo5(threading.Thread):
    def __init__(self, nombre_hilo):
        threading.Thread.__init__(self, name=nombre_hilo, target=Hilo5.run)
        self.nombre_hilo = nombre_hilo
        

    def run(self):
        self.infinito()
    
    def infinito(self):
        while True:
            logging.debug('esto se escribe infinitamente')
            time.sleep(5)
        return