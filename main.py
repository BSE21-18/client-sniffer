print("Main.py run")
#Connect to the Internet Via WiFi

from client import sendSample
sample = {"Topic":"DV00023","message":'{"gas1":"345PH","gas2":"345PH","gas3":"345PH","gas4":"345PH","gas5":"345PH","gas6":"345PH"}'}
sendSample(sample)

#==============================COLLECTING SENSOR DATA FOR TRAINING OUR MODEL===============================================
"""
import os
from machine import Pin, SoftSPI
from sdcard import SDCard

# Pin assignment:
# MISO -> GPIO 13
# MOSI -> GPIO 12
# SCK  -> GPIO 14
# CS   -> GPIO 27

spisd = SoftSPI(-1, miso=Pin(13), mosi=Pin(12), sck=Pin(14))
sd = SDCard(spisd, Pin(27))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
os.chdir('sd')

#os.mkdir('sample folder')

# 2. To create a new file for writing:
#f = open('opentest.csv', 'w')
#f.write('"MQ135","MQ3","MQ9","MQ8","MQ4","MQ5","TEMP","HUMD"\n')

#print("-MQ135->","-MQ3->",MQ_3_value,"-MQ9->",MQ_9_value,"-MQ8->",MQ_8_value,"-MQ4->",MQ_4_value,"-MQ5->",MQ_5_value,"-TEMP->",Temp,"-HUM->",Humd)
"""
#==========================================================================================================================


def getVocData():
    #------------------------Temperature and Relative Humidity------------------------------
    sensor = dht.DHT22(Pin(25))
    
    #=====================================GAS SENSORS=======================================
    MQ_135 = ADC(Pin(36))            #MQ-135 FOR BEZENE ALCHOL
    MQ_135.atten(ADC.ATTN_11DB)
    time.sleep_ms(1000)
    MQ_9 = ADC(Pin(35))              #MQ-6 FOR ALCHOL NATURE GAS
    MQ_9.atten(ADC.ATTN_11DB)
    time.sleep_ms(1000)
    MQ_5 = ADC(Pin(39))              #MQ-5 FOR ALCHOL AND METHANE
    MQ_5.atten(ADC.ATTN_11DB)
    time.sleep_ms(1000)
    MQ_8 = ADC(Pin(32))              #MQ-2 FOR ALCHOL
    MQ_8.atten(ADC.ATTN_11DB)
    time.sleep_ms(1000)
    MQ_4 = ADC(Pin(33))              #
    MQ_4.atten(ADC.ATTN_11DB)
    time.sleep_ms(1000)
    MQ_3 = ADC(Pin(34))              #creating potentiometer object
    MQ_3.atten(ADC.ATTN_11DB)
    MQ_4 = ADC(Pin(33))              #creating potentiometer object
    MQ_4.atten(ADC.ATTN_11DB)
    time.sleep_ms(1000)
    
    #3MINS FOR SENSORS TO WARMUP BEFORE PICKING UP READINGS
    #time.sleep_ms(20000)
    

    while True:
        #==============================GAS SENSOR READINGS==============================
        MQ_135_value = MQ_135.read()   #reading analog pin
        MQ_3_value = MQ_3.read()       #reading analog pin
        MQ_9_value = MQ_9.read()       #reading analog pin
        MQ_4_value = MQ_4.read()       #reading analog pin
        MQ_5_value = MQ_5.read()       #reading analog pin
        MQ_8_value = MQ_8.read()       #reading analog pin
        
        #======================TEMPERATURE AND RELATIVE HUMIDITY========================        
        sensor.measure()
        Temp = sensor.temperature()
        Humd = sensor.humidity()
        
        #======================FREQUECY FOR SAMPLE PICKING 3SECs========================
        time.sleep_ms(3000)
        
        #==========================CORESPONDING ADC VALUES==============================
        sample = {"Topic":"DV00023","message":'{"MQ135":'+str(MQ_135_value)+',"MQ3":'+str(MQ_3_value)+',"MQ9":'+str(MQ_9_value)+',"MQ8":'+str(MQ_8_value)+',"MQ4":'+str(MQ_4_value)+',"MQ5":'+str(MQ_5_value)+',"TEMP":'+str(Temp)+',"HUM":'+str(Humd)+'}'}
        
        #========================SENDING SAMPLE TO BE PROCESSED=========================
        #sendSample(sample)
        
        #==================CREATING OUR OWN DATASET TO TRAIN THE MODEL==================
        """
        f = open('UnHealthyTomatoes.csv', 'a')
        f.write('"'+str(MQ_135_value)+'","'+str(MQ_3_value)+'","'+str(MQ_9_value)+'","'+str(MQ_8_value)+'","'+str(MQ_4_value)+'","'+str(MQ_5_value)+'","'+str(Temp)+'","'+str(Humd)+'"\n')
        print(sample)
        f.close()
        """

getVocData()
     