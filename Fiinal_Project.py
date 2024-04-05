#!/usr/bin/env python3
import serial
from gpiozero import LED
import time

data=0
led = LED(26)
ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1000
)


while 1:
    data = ser.read(1)
    print("Received data:", data)
    if data == b'1':
        led.on()
        print("Received data:", data)
  
    #elif data== '2':
      #   led.on()
        #led.off()
    else:
        led.off()
       
