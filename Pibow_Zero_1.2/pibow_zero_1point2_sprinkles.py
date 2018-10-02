#!/usr/bin/python3
"""
Sprinkles - Pibow Zero 1.2

Using the colors of the Pibow Zero 1.2 case, this program lights up
and turns off random LEDs.

....................

Functions:

- get_random_color: Selects a random color from a list
- light_up_random_led: Lights up a random LED.
- get_random_x_coordinate: Returns a random value from the
  X_COORDINATES list
- get_random_y_coordinate: Returns a random value from the
  Y_COORDINATES list
- stop: Print exit message and turn off the UnicornHAT

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
#########################################################################
#                          Import modules                              #
########################################################################

from time import sleep
import random
import unicornhat
from print_unicornphat_header import print_unicornphat_header

########################################################################
#                           Initialize                                 #
########################################################################

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

Y_COORDINATES = [0, 1, 2, 3, 4]
X_COORDINATES = [0, 1, 2, 3, 4, 5, 6, 7]

COLOR_LIST = [(0, 0, 255), (0, 204, 204),
              (127, 0, 255), (255, 255, 255)]

# (0, 0, 255)         Blue
# (0, 204, 204)       Indigo
# (127, 0, 255)       Violet
# (255, 255, 255)     White

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
            # STEP01: Get a random color
            red, green, blue = get_random_color()
            # STEP02: Turn on a random LED with the random color
            light_up_random_led(red, green, blue)
            # STEP03: Turn off a random LED
            unicornhat.set_pixel(get_random_x_coordinate(),
                                 get_random_y_coordinate(),
                                 0, 0, 0)
            unicornhat.show()
            sleep(0.01)
    except KeyboardInterrupt:
        stop()


def get_random_color():
    """
    This function selects a random color from the COLOR_LIST, extracts
    the individual red, green, and blue color values, and returns those
    individual values.
    """

    color_tuple = random.choice(COLOR_LIST)
    return int(color_tuple[0]), int(color_tuple[1]), int(color_tuple[2])


def light_up_random_led(red, green, blue):
    """
    This function lights up a random LED.

    Arguments:
        red: the red color value
        green: the green color value
        blue: the blue color value
    """
    unicornhat.set_pixel(get_random_x_coordinate(),
                         get_random_y_coordinate(),
                         red, green, blue)


def get_random_x_coordinate():
    """
    Returns a random value from the X_COORDINATES list
    """

    return int(random.choice(X_COORDINATES))


def get_random_y_coordinate():
    """
    Returns a random value from the Y_COORDINATES list
    """

    return int(random.choice(Y_COORDINATES))


def stop():
    """
    Print exit message and turn off the UnicornHAT
    """
    print("\nExiting program.")
    unicornhat.off()


if __name__ == '__main__':
    main()
