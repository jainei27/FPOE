import threading
import datetime
import logging
import time 
from hilo4 import Hilo4
from hilo5 import Hilo5
from hilo6 import Hilo6

logging.basicConfig(level=logging.DEBUG)

tiempoInicial= datetime.datetime.now()

def consultar(nombre):
        logging.debug('Consultando: ' + nombre)
        time.sleep(5)
        return

def numeros():
        list = [1, 2, 3, 4, 5]
        for element in list:
                logging.debug(element)
                time.sleep(1)
        return

def letras():
        list = ['a', 'b', 'c', 'd', 'e']
        for element in list:
                logging.debug(element)
                time.sleep(2)
        return

hilo1 = threading.Thread(name = 'Hilo1', target= numeros)
hilo2 = threading.Thread(name = 'Hilo2', target= letras)
hilo3 = threading.Thread(name = 'Hilo3', target= consultar, args=('Mateo', ))
hilo4 = Hilo4('hilo4', 'Mateo')
hilo5 = Hilo5('hilo5')
hilo6 = Hilo6('hilo6')

#hilo1.start()
#hilo1.join()
#hilo2.start()
#hilo2.join()
#hilo3.start()
#hilo3.join()
#hilo4.start()
#hilo4.join()
hilo5.start()
#hilo5.join()
hilo6.start()
hilo6.join()

tiempoFinal = datetime.datetime.now()

logging.debug('Tiempo transcurrido '
                + str(tiempoFinal.second - tiempoInicial.second) + '\n')