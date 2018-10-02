#!/usr/bin/python3
"""
Moving Rainbow - Pibow Zero 1.2

This is a moving rainbow program that only displays the colors of the
Pibow Zero case for the Raspberry Pi Zero 1.2

....................

Functions:
- display_rainbow: Lights up the LEDs to create a rainbow using only the
    colors of the Pibow Zero 1.2 case. The rainbow is static.
- moving_rainbow: Lights up the LEDs to create a rainbow using only the
    colors of the Pibow Zero 1.2 case. The rainbow "moves."
- stop: Print exit message and turn off the UnicornHAT

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

import time
import unicornhat
from print_unicornphat_header import print_unicornphat_header

########################################################################
#                           Initialize                                 #
########################################################################

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

B = (0, 0, 255)       # Blue
I = (0, 204, 204)     # Indigo
V = (127, 0, 255)     # Violet
W = (255, 255, 255)   # White
OFF = (0, 0, 0)

########################################################################
#                            Functions                                 #
########################################################################


def main():
    """
    This is the main function
    """

    print_unicornphat_header()

    # Force white text after selecting random colored header
    print("\033[1;37;40mPress Ctrl-C to stop the program.")

    try:
        while True:
            display_rainbow()
            moving_rainbow()
    except KeyboardInterrupt:
        stop()


def display_rainbow():
    """
    The function lights up the LEDs to create a rainbow using only the
    colors of the Pibow Zero 1.2 case.
    """

    rainbow = [
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    unicornhat.set_pixels(rainbow)
    unicornhat.show()
    time.sleep(3.0)


def moving_rainbow():
    """
    The function makes the rainbow move
    """

    rainbow0 = [
        [B, I, W, V, B, I, W, V],
        [B, I, W, V, B, I, W, V],
        [B, I, W, V, B, I, W, V],
        [B, I, W, V, B, I, W, V],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    rainbow1 = [
        [I, W, V, B, I, W, V, B],
        [I, W, V, B, I, W, V, B],
        [I, W, V, B, I, W, V, B],
        [I, W, V, B, I, W, V, B],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    rainbow2 = [
        [W, V, B, I, W, V, B, I],
        [W, V, B, I, W, V, B, I],
        [W, V, B, I, W, V, B, I],
        [W, V, B, I, W, V, B, I],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    rainbow3 = [
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.set_pixels(rainbow0)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_pixels(rainbow1)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_pixels(rainbow2)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_pixels(rainbow3)
        unicornhat.show()
        time.sleep(0.5)


def stop():
    """
    Print exit message and turn off the UnicornHAT
    """
    print("\nExiting program.")
    unicornhat.off()


if __name__ == '__main__':
    main()
