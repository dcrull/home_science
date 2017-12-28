#!/usr/bin/env python

# This closely follows the library developed by Nicholas Johnson fo NYU CUSP.


# This program stores data collected by a BME280 temp,humidity,pressure sensor controlled
# by a Raspberry Pi 3 via an I2C protocol. The data is written to a .csv file stored in an SD card.

import csv, os.path
import RPi.GPIO as GPIO
import time
import Adafruit_BME280 as BME280
import tsl2561 as TSL2561

# pathname for saved data
root = "/home/pi/Documents/qc"

def write_csv(data):
	"Write data to .csv file"

	fname = root+'/l_data.csv'

	with open(fname, 'a') as f:
		w = csv.DictWriter(f, data.keys())
		w.writerow(data)

	f.close()

def main(bme280,tsl):
	"Collect data"

	while True:
		temp_list = []
		pres_list = []
		humid_list = []
		lux_list = []

		data  = {
				'Lux': tsl.lux()
			}

		# t_end = time.time() + 30
		# while time.time() < t_end:
			# temp_list.append(bme280.read_temperature())
			# pres_list.append(bme280.read_pressure() / 100)
			# humid_list.append(bme280.read_humidity())
			# lux_list.append(tsl.lux())


		# Read data from sensors
		# data = {
		# 	'Time': time.time(),
		# 	'Temp': sum(temp_list)*1.0/len(temp_list),
		# 	'Pressure': sum(pres_list)*1.0/len(pres_list),
		# 	'Humidity': sum(humid_list)*1.0/len(humid_list),
		# 	'Lux': sum(lux_list)*1.0/len(lux_list),
		# }

		# write to csv
		write_csv(data)
		time.sleep(5)

if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)
	# initialize sensors
	print 'Reading sensors...'

	try:
		bme280 = BME280.BME280()
		tsl = TSL2561.TSL2561()

	except Exception as e:
		print e
		exit()

	main(bme280,tsl)