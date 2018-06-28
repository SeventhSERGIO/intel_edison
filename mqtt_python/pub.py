import mraa
import sys
import time

import paho.mqtt.publish as publish

pot = mraa.Aio(0) 

while 1:
    potVal = float(pot.read())
    print(potVal)
    publish.single("topico/ejemplo_1", str(potVal), hostname="192.168.1.108")