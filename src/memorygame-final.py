# Raspberry Pi Memory Game
# --------------------------
# Like the "Simon" game
#
# Setup is 3 LEDs (gpio 17,27,22) and 3 buttons (gpio 2,3,4).
# The game comes up with a sequence of LEDs, that the user has to
# "play back" using the buttons.
#
# Win: Game continues if the user repeats the current sequence, in which
#      case the game adds one more LED to the existing sequence until
#      the game is over
#
# Lose: The game ends when the user hits the wrong button for the
#       corresponding LED in the current sequence
#
# Score: Score is the length of the sequence by the time the game
#        is over
#

import RPi.GPIO as gpio
import time
import random

btn1,btn2,btn3 = 16,20,21
led1,led2,led3 = 17,27,22

gameOver=False
ledSequence=[]
ledWait=1

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
    print("Disp =>", ledSequence)
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

        print("Buttons pressed =>", buttons)
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
# Game ...
#

setup()
animate(5, 0.1)

while not gameOver:
    time.sleep(0.5)
    ledSequence.append(random.choice( [led1, led2, led3] ))
    display()

    for led in ledSequence:
        button = readInput()
        blink([led], ledWait, 0.3)
 
        if (led != button):
            gameOver = True
            animate(3, 0.3)