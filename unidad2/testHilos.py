import threading
import datetime
import logging
import time
from hilo4 import Hilo4
from hilo5 import Hilo5
from hilo6 import Hilo6  

logging.basicConfig(level=logging.DEBUG)

tiempo_inicial = datetime.datetime.now()

def numeros():
    list = [1,2,3,4,5]
    for element in list:
        logging.debug(element)
        time.sleep(1)

def letras():
    list = ['a','b','c','d','e']
    for element in list:
        logging.debug(element)
        time.sleep(2)

def consultar(nombre):
    logging.debug('consultar: ' + nombre)
    time.sleep(5)
    return

hilo_1 = threading.Thread(name='hiilo_1', target=numeros)
hilo_2 = threading.Thread(name='hiilo_2', target=letras)
hilo_3 = threading.Thread(name='hiilo_3', target=consultar, args=('raul',))
hilo_4 = Hilo4('hilo_4', 'Raul')
hilo_5 = Hilo5('hilo_5')
hilo_6 = Hilo6('hilo_6')  


hilo_5.start()
hilo_6.start() 
hilo_6.join()

tiempo_final = datetime.datetime.now()
logging.debug("tiempo transcurrido: " + str(tiempo_final.second - tiempo_inicial.second) + '\n')