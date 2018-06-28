import pyupm_i2clcd as lcd
import mraa
import time
import paho.mqtt.subscribe as subscribe
import sys
# initialise gpio 2
gpio_1 = mraa.Gpio(2)
# set gpio 2 to output
gpio_1.dir(mraa.DIR_OUT)

EdisonLCD = lcd.Jhd1313m1(0, 0x3E, 0x62)
EdisonLCD.setColor(0, 255, 0)

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    EdisonLCD.clear()
    EdisonLCD.setCursor(0,0)
    EdisonLCD.write(message.payload)

subscribe.callback(on_message_print, "topico/ejemplo", hostname="192.168.1.108")