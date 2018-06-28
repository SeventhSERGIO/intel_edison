import mraa
import time
import paho.mqtt.subscribe as subscribe

# initialise gpio 2
gpio_1 = mraa.Gpio(2)

# set gpio 2 to output
gpio_1.dir(mraa.DIR_OUT)

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    if message.payload == "ON":
		gpio_1.write(1)
		#print("Hola")
	elif message.payload == "OFF":
		gpio_1.write(0)
		#print("Adios")

subscribe.callback(on_message_print, "topico/ejemplo", hostname="192.168.1.108")
