import RPi.GPIO as gpio
import time
import random

btn1,btn2,btn3 = 16,20,21
led1,led2,led3 = 17,27,22

#
# Do all the GPIO pin setup
#
# Modify if you want to change the pins or add more buttons/leds
#
def setup():
    gpio.setmode(gpio.BCM)

    # Setup buttons
    for btn in (btn1, btn2, btn3):
        gpio.setup(btn, gpio.IN, pull_up_down=gpio.PUD_UP)

    # Setup LEDs
    for led in (led1, led2, led3):
        gpio.setup(led, gpio.OUT)
        gpio.output(led, False)

#
# Blink a given led (list)
#
# leds - list of led BCM pin numbers to "blink"
# timeOn - Amount of time to turn LEDs on
# timeOff - How much time to wait after we turn LEDs off (default is 0)
#
def blink(leds, timeOn, timeOff=0.0):
    for led in leds:
        gpio.output(led, True)
    time.sleep(timeOn)

    for led in leds:
        gpio.output(led, False)
    time.sleep(timeOff)

#
# display LED sequence
#
# Shows current LED sequence by blinking each LED
#
def display():
    for led in ledSequence:
        blink([led], ledWait, 0.3)

# Show "game over" animation
#
# Blinks all LEDs on/off a set of times to indicate game is over
#
def animate(repeat, time):
    for i in range(repeat):
        blink([led1,led2,led3], time, time)

# Read pressed button
#
# Reads the currently read button, returns the corresponding LED pin
# number for that button
#
# Returns LED pin number of button pressed
#
def readInput():
    done = False

    setup()

    while not done:
        buttons = []
        for btn in(btn1, btn2, btn3):
            if not gpio.input(btn):
                buttons.append(btn)

        if (len(buttons) == 1):
            done = True
            btn = buttons[0]
            if btn == btn1:
                return led1
            elif btn == btn2:
                return led2
            elif btn == btn3:
                return led3

        time.sleep(0.1)

#

while True:
        blink([readInput()], 0.3, 0.2)
