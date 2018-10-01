#!/usr/bin/python3
"""
American Flag

This program lights up the Pimoroni Unicorn PHAT with the colors of the
American Flag.

....................

Functions:
- display_flag: Lights up the LEDs to create a picture of the
      American flag.
- waving_flag: Makes the flag appear to be waving in the wind.
- stop: Print exit message and turn OFF the UnicornHAT

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from time import sleep
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
R2 = (128, 0, 0)
W2 = (128, 128, 128)
B2 = (0, 0, 128)

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
            display_flag()
            waving_flag()
    except KeyboardInterrupt:
        stop()


def display_flag():
    """
    The function lights up the LEDs to create a picture of the
    American flag.
    """

    flag = [
        [B, B, B, B, R, R, R, R],
        [B, B, B, B, W, W, W, W],
        [R, R, R, R, R, R, R, R],
        [W, W, W, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    unicornhat.set_pixels(flag)
    unicornhat.show()
    sleep(3.0)


def waving_flag():
    """
    The function makes the flag appear to be waving in the wind.
    """

    wave0 = [
        [B2, B, B, B, R, R, R, R],
        [B2, B, B, B, W, W, W, W],
        [R2, R, R, R, R, R, R, R],
        [W2, W, W, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    wave1 = [
        [B, B2, B, B, R, R, R, R],
        [B, B2, B, B, W, W, W, W],
        [R, R2, R, R, R, R, R, R],
        [W, W2, W, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    wave2 = [
        [B, B, B2, B, R, R, R, R],
        [B, B, B2, B, W, W, W, W],
        [R, R, R2, R, R, R, R, R],
        [W, W, W2, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    wave3 = [
        [B, B, B, B2, R, R, R, R],
        [B, B, B, B2, W, W, W, W],
        [R, R, R, R2, R, R, R, R],
        [W, W, W, W2, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    wave4 = [
        [B, B, B, B, R2, R, R, R],
        [B, B, B, B, W2, W, W, W],
        [R, R, R, R, R2, R, R, R],
        [W, W, W, W, W2, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    wave5 = [
        [B, B, B, B, R, R2, R, R],
        [B, B, B, B, W, W2, W, W],
        [R, R, R, R, R, R2, R, R],
        [W, W, W, W, W, W2, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    wave6 = [
        [B, B, B, B, R, R, R2, R],
        [B, B, B, B, W, W, W2, W],
        [R, R, R, R, R, R, R2, R],
        [W, W, W, W, W, W, W2, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    wave7 = [
        [B, B, B, B, R, R, R, R2],
        [B, B, B, B, W, W, W, W2],
        [R, R, R, R, R, R, R, R2],
        [W, W, W, W, W, W, W, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    unicornhat.set_pixels(wave0)
    unicornhat.show()
    sleep(0.05)
    unicornhat.set_pixels(wave1)
    unicornhat.show()
    sleep(0.05)
    unicornhat.set_pixels(wave2)
    unicornhat.show()
    sleep(0.05)
    unicornhat.set_pixels(wave3)
    unicornhat.show()
    sleep(0.05)
    unicornhat.set_pixels(wave4)
    unicornhat.show()
    sleep(0.05)
    unicornhat.set_pixels(wave5)
    unicornhat.show()
    sleep(0.05)
    unicornhat.set_pixels(wave6)
    unicornhat.show()
    sleep(0.05)
    unicornhat.set_pixels(wave7)
    unicornhat.show()
    sleep(0.05)


def stop():
    """
    Print exit message and turn OFF the UnicornHAT
    """
    print("\nExiting program.")
    unicornhat.off()


if __name__ == '__main__':
    main()
