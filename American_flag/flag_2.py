#!/usr/bin/python3
"""
American Flag 2

This program lights up the Pimoroni Unicorn PHAT with the colors of the
American Flag. It's 180 degree version of American Flag.

....................

Functions:
- display_flag: Lights up the LEDs to create a picture of the
      American flag.
- stop: Print exit message and turn OFF the UnicornHAT

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from signal import pause
import unicornhat
from print_unicornphat_header import print_unicornphat_header

########################################################################
#                           Initialize                                 #
########################################################################

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

R = (255, 0, 0)
W = (255, 255, 255)
B = (0, 0, 255)
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
        display_flag()
    except KeyboardInterrupt:
        stop()


def display_flag():
    """
    The function lights up the LEDs to create a picture of the
    American flag.
    """

    flag = [
        [W, W, W, W, W, W, W, W],
        [R, R, R, R, R, R, R, R],
        [W, W, W, W, B, B, B, B],
        [R, R, R, R, B, B, B, B],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF,OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    unicornhat.set_pixels(flag)
    unicornhat.show()
    pause()


def stop():
    """
    Print exit message and turn OFF the UnicornHAT
    """
    print("\nExiting program.")
    unicornhat.off()


if __name__ == '__main__':
    main()
