"""
Arduino controls for lighting up LEDs

In Arduino IDE, set up by going to Files --> Examples --> Firmata --> StandardFirmata
Upload this code to Arduino with correct ports hooked up
"""

import pyfirmata

#connect to Arduino port
comport = "/dev/cu.usbmodem1301"
board = pyfirmata.Arduino(comport)

led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')
led_5 = board.get_pin('d:12:o')

def led(finger_up):
    leds = [led_1, led_2, led_3, led_4, led_5]

    #light up led corresponding to finger
    for (idx, x) in enumerate(finger_up):
        curr_led = leds[idx]
        if(x == 1):
            curr_led.write(1)
        else:
            curr_led.write(0)