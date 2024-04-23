# Write your code here :-)
import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value


    for (i,led) in enumerate(leds):

        if (volume > 19000 + 3000*i):
            leds[i].value = 1
        else:
            leds[i].value = 0

    '''
    for (i,led) in enumerate(leds):

        if (volume > 1900 - 3000*i):
            leds[i].value = 1
        else:
            leds[i].value = 0
            sleep(.5)
   # delay = max(0.1, 0.1 - (volume / 65535) * 0.09)  # Adjust the range and scaling as needed
    '''
    #




    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
