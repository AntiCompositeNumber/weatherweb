#! /usr/bin/python

import rrdtool
import Adafruit_DHT

#Set up sensor
sensor = Adafruit_DHT.AM2302
pin = 17

#Get data from sensor
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#Convert temperature from Celsius to Fahrenheit
temperature = (temperature * 9/5) + 32

#Round to tenths
#round(temperature,1)
#round(humidity,1)

#Send data to RRD
rrdtool.update('weatherweb.rrd, N:{0:0.1f}:N:{1:0.1f}'.format(temperature, humidity))
print(temperature","humidity)
