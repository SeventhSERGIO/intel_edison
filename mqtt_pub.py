import paho.mqtt.client as paho
import mraa
import sys
import time

def on_subscribe(client1, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client1, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    


broker="192.168.1.108"
port=1883
client1= paho.Client("Edison_Adrian")   
client1.on_subscribe = on_subscribe
client1.on_message = on_message                                              
client1.connect(broker,port)    
client1.subscribe("topico/relay_1",0)                             
# Publish
pot = mraa.Aio(0) 

client1.loop_start()

while 1:
	potVal = float(pot.read())
	ret= client1.publish("topico/ejemplo_1",str(potVal)) 
	time.sleep(1)                  