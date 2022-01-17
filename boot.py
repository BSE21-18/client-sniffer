# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
print("Boot Has Run")
from machine import Pin, ADC, SoftI2C
import dht
import time

from i2c_lcd import I2cLcd 

DEFAULT_I2C_ADDR =  0x27

i2c = SoftI2C (scl=Pin(22), sda=Pin(21), freq=400000)



def connect():
    print("Trying to connect")
    import network
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nets = nic.scan()
    print(nets)
    if nic.isconnected():
        print("WIFI connected Aready ........")
        return
    nic.connect('GoldenTouch', '@1234567890')
    
    #nic.connect('HUAWEI-CLOUD', '@W1fi#2021$')
    #nic.connect('wimea-ict', '@wimea-ict2021')
    print("connecting....")
    #print(nic.isconnected())
    while not nic.isconnected():
        pass
    print(nic.isconnected())
    print("Connection successful ......")
    print(nic.ifconfig())

connect()
    