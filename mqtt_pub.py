import paho.mqtt.client as paho
import pyupm_i2clcd as lcd
import mraa
import sys
import time

# initialise gpio 2
gpio_1 = mraa.Gpio(2)
# set gpio 2 to output
gpio_1.dir(mraa.DIR_OUT)

EdisonLCD = lcd.Jhd1313m1(0, 0x3E, 0x62)
EdisonLCD.setColor(0, 255, 0)

def on_subscribe(client1, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client1, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    EdisonLCD.clear()
    EdisonLCD.setCursor(0,0)
    EdisonLCD.write(msg.payload)
    if str(msg.payload) == "ON":
	   gpio_1.write(1)
    elif str(msg.payload) == "OFF":
	   gpio_1.write(0)    


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