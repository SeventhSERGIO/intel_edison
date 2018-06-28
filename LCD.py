
import pyupm_i2clcd as lcd
import mraa
import time
import sys

pot = mraa.Aio(0) 
EdisonLCD = lcd.Jhd1313m1(0, 0x3E, 0x62)
EdisonLCD.setColor(0, 255, 0)

while 1:
    potVal = float(pot.read())
    EdisonLCD.setCursor(0,0)
    EdisonLCD.write(str(potVal))
    time.sleep(1)
    EdisonLCD.clear()