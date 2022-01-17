import uwebsockets.client
import os
import ujson
from time import sleep_ms, ticks_ms 
from machine import SoftI2C, Pin 
from i2c_lcd import I2cLcd 

DEFAULT_I2C_ADDR =  0x27

i2c = SoftI2C (scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 4, 16)

def sendSample(sample):
    with uwebsockets.client.connect('ws://xxx.xxx.xx.xxx:xxxxx/xxxxx') as websocket:
        lcd.putstr("Diagnosing please wait ....")

        encoded_sample_data = ujson.dumps(sample)
        
        websocket.send(encoded_sample_data)
        print("> {}".format(encoded_sample_data))

        LCD_message = websocket.recv()
        print("< {}".format(LCD_message))
        sleep_ms(1000)
        lcd.clear()        
        lcd.move_to(2, 1)
        lcd.putstr("{}".format(LCD_message))



