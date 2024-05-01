import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class Hilo5(threading.Thread):
    
    def __init__(self, nombreHilo):
        threading.Thread.__init__(self, name=nombreHilo)
        self.nombreHilo = nombreHilo

    def run(self):
        self.infinito()
    
    def infinito(self):
        while True: 
            logging.debug('Esto se escribe infinitamente ')
            time.sleep(1)