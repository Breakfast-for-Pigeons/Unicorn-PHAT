#!/usr/bin/python3
"""
Waving Flag 3

This program lights up the Pimoroni Unicorn PHAT with the colors of the
American Flag and makes the flag appear to be waving in the wind. This
version waves the flag diagonally instead of horizontally.

....................

Functions:
- display_flag: Lights up the LEDs to create a picture of the
      American flag.
- waving_flag: Makes the flag appear to be waving in the wind.
- stop: Print exit message and turn off the UnicornHAT

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from time import sleep
import unicornhat

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

    wave00 = [
        [B, B, B, B, R, R, R, R],
        [B, B, B, B, W, W, W, W],
        [R, R, R, R, R, R, R, R],
        [W2, W, W, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    wave01 = [
        [B, B, B, B, R, R, R, R],
        [B, B, B, B, W, W, W, W],
        [R2, R, R, R, R, R, R, R],
        [W, W2, W, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    wave02 = [
        [B, B, B, B, R, R, R, R],
        [B2, B, B, B, W, W, W, W],
        [R, R2, R, R, R, R, R, R],
        [W, W, W2, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    wave03 = [
        [B2, B, B, B, R, R, R, R],
        [B, B2, B, B, W, W, W, W],
        [R, R, R2, R, R, R, R, R],
        [W, W, W, W2, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    wave04 = [
        [B, B2, B, B, R, R, R, R],
        [B, B, B2, B, W, W, W, W],
        [R, R, R, R2, R, R, R, R],
        [W, W, W, W, W2, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    wave05 = [
        [B, B, B2, B, R, R, R, R],
        [B, B, B, B2, W, W, W, W],
        [R, R, R, R, R2, R, R, R],
        [W, W, W, W, W, W2, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    wave06 = [
        [B, B, B, B2, R, R, R, R],
        [B, B, B, B, W2, W, W, W],
        [R, R, R, R, R, R2, R, R],
        [W, W, W, W, W, W, W2, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    wave07 = [
        [B, B, B, B, R2, R, R, R],
        [B, B, B, B, W, W2, W, W],
        [R, R, R, R, R, R, R2, R],
        [W, W, W, W, W, W, W, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    wave08 = [
        [B, B, B, B, R, R2, R, R],
        [B, B, B, B, W, W, W2, W],
        [R, R, R, R, R, R, R, R2],
        [W, W, W, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    wave09 = [
        [B, B, B, B, R, R, R2, R],
        [B, B, B, B, W, W, W, W2],
        [R, R, R, R, R, R, R, R],
        [W, W, W, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    wave10 = [
        [B, B, B, B, R, R, R, R2],
        [B, B, B, B, W, W, W, W],
        [R, R, R, R, R, R, R, R],
        [W, W, W, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    waves = [wave00, wave01, wave02, wave03, wave04, wave05,
             wave06, wave07, wave08, wave09, wave10]


    # Loop through the rainbows so they appear to move
    for wave in waves:
        unicornhat.set_pixels(wave)
        unicornhat.show()
        sleep(0.05)


def stop():
    """
    Print exit message and turn off the UnicornHAT
    """
    print("\nExiting program.")
    unicornhat.off()


if __name__ == '__main__':
    # Force white text after selecting random colored header
    print("\033[1;37;40mPress Ctrl-C to stop the program.")

    try:
        while True:
            display_flag()
            waving_flag()
    except KeyboardInterrupt:
        stop()
