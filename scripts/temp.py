#!/usr/bin/env python

# This closely follows the library developed by Nicholas Johnson fo NYU CUSP.


# This program stores data collected by a BME280 temp,humidity,pressure sensor controlled
# by a Raspberry Pi 3 via an I2C protocol. The data is written to a .csv file stored in an SD card.

import csv, os.path
import RPi.GPIO as GPIO
import time
import sys
from os import path
import Adafruit_BME280 as BME280

# pathname for saved data
root = sys.argv[1]

def write_csv(data):
	"Write data to .csv file"

	fname = os.path.join(root, 'data.csv')

	with open(fname, 'a') as f:
		w = csv.writer(f)
		w.writerow(data)

	f.close()

def main(bme280):
	"Collect data"

	while True:
		temp_list = []
		pres_list = []
		humid_list = []

		t_end = time.time() + 30
		while time.time() < t_end:
			temp_list.append(bme280.read_temperature())
			pres_list.append(bme280.read_pressure() / 100)
			humid_list.append(bme280.read_humidity())

		# Read data from sensors
		data = (time.time(),
			sum(temp_list)*1.0/len(temp_list),
			sum(pres_list)*1.0/len(pres_list),
			sum(humid_list)*1.0/len(humid_list))

		# write to csv
		write_csv(data)

if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)
	# initialize sensors
	print 'Reading sensors...'

	try:
		bme280 = BME280.BME280()

	except Exception as e:
		print e
		exit()

	main(bme280)
