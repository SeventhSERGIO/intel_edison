import paho.mqtt.client as paho
import mraa
import sys
import time

broker="192.168.1.108"
port=1883
# Create function for callback
#def on_publish(client,userdata,result):             
#        print("data published \n")
#pass
# Create client object
client1= paho.Client("Edison_Adrian")                           
# Assign function to callback
#client1.on_publish = on_publish 
# Establish connection                        
client1.connect(broker,port)                                 
# Publish
pot = mraa.Aio(0) 

while 1:
	potVal = float(pot.read())
	ret= client1.publish("topico/ejemplo_1",str(pot))                   