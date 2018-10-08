#!/usr/bin/python3
"""
Sprinkles - Pibow Zero W

This program lights up and turns off random LEDS using the colors of the
Pibow Zero 1.2 case

....................

Functions:
- sprinkles: Lights up and turns off random LEDs

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

import time
import unicornhat
from bfp_unicornphat import print_header
from bfp_unicornphat import stop
from bfp_unicornphat import get_random_color
from bfp_unicornphat import light_up_random_led
from bfp_unicornphat import random_x_coordinate
from bfp_unicornphat import random_y_coordinate

########################################################################
#                            Functions                                 #
########################################################################


def sprinkles():
    """
    Lights up and turns off random LEDs
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        # Turn on a random LED
        red, green, blue = get_random_color()
        light_up_random_led(red, green, blue)
        # Turn OFF a random LED
        unicornhat.set_pixel(random_x_coordinate(),
                             random_y_coordinate(),
                             0, 0, 0)
        unicornhat.show()
        time.sleep(0.01)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        sprinkles()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
