#!/usr/bin/python3

import rrdtool
import Adafruit_DHT
import time

# Set up sensor
sensor = Adafruit_DHT.AM2302
pin = 17

while True:
    # Get data from sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Convert temperature from Celsius to Fahrenheit
    temperature = (temperature * 9 / 5) + 32

    # The RRD stores everything as floating-point numbers,
    # so don't bother rounding anything here.
    # Send data to RRD
    try:
        rrdtool.update("weatherweb.rrd", "N:{0}:{1}".format(temperature, humidity))
        print(time.time(), "N:{0}:{1}".format(temperature, humidity))
    except Exception:
        print("RRD error, ", time.time(), "N:{0}:{1}".format(temperature, humidity))

    # And now we wait.
    time.sleep(55)
