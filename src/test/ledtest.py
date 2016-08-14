# Test our LEDs for the game, then test the inputs

import RPi.GPIO as gpio
import time
import random

gpio.setmode(gpio.BCM)

led1,led2,led3 = 17,27,22

toggle = True

for led in (led1,led2,led3):
	gpio.setup(led, gpio.OUT)

for i in range(4):
	for led in (led1,led2,led3):
		toggle = not toggle
		gpio.output(led, toggle)
	time.sleep(0.5)


for led in (led1,led2,led3):
	gpio.output(led, False)

for i in range(8):
	leds = led2,led3
	for led in leds:
		gpio.output(led,True)
		time.sleep(0.1)
		gpio.output(led,False)
	
	leds = led2,led1
	for led in leds:
		gpio.output(led,True)
		time.sleep(0.1)
		gpio.output(led,False)

gpio.cleanup()

