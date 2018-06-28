import mraa
import sys
import time
import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish

# initialise gpio 2
gpio_1 = mraa.Gpio(2)
# set gpio 2 to output
gpio_1.dir(mraa.DIR_OUT)
pot = mraa.Aio(0) 

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    if message.payload == "ON":
	   gpio_1.write(1)
    elif message.payload == "OFF":
	   gpio_1.write(0)

subscribe.callback(on_message_print, "topico/relay_1", hostname="192.168.1.108")

while 1:
    potVal = float(pot.read())
    print(potVal)
    publish.single("topico/ejemplo_1", str(potVal), hostname="192.168.1.108")