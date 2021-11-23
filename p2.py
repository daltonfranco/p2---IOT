import random as rd
import time
from datetime import datetime
import urllib.request

def sensorDeMovimento():
    return rd.randint(0,1)

valor = 0

myAPI = "P6ZOAIEYRPKUCFLH"
baseURL = "https://api.thingspeak.com/update?api_key="+myAPI

while True:
    time.sleep(5)
    valor = sensorDeMovimento()
    horario = datetime.now()

    if valor == 1:
        print("Passou uma alguma coisa na frente da loja")
        print(horario)

        conn = urllib.request.urlopen((baseURL+'&field1=%s&field2="%s"'%(valor, horario)).replace(" ", "-"))
        conn.close()
    else:
        print("Nao passou nada na frente da loja")
        print(horario)

        conn = urllib.request.urlopen((baseURL+'&field1=%s&field2="%s"'%(valor, horario)).replace(" ", "-"))
        conn.close()
