#!/usr/bin/python3
"""
Vertical Striper - Pibow Zero 1.2

Using the colors of the Pibow Zero 1.2 case, this program lights up
each colomn.

....................

Functions:

- get_y_color: Extracts the red, green, and blue values
- pibow_zero_vertical_striper_1: Keeps x and y the same
- pibow_zero_vertical_striper_2: Reverses y coordinates
- pibow_zero_vertical_striper_3: Reverses x coordinates
- pibow_zero_vertical_striper_4: Reverses both x and y coordinates
- pibow_zero_vertical_striper: Lights up columns of the UnicornPHAT
- stop: Print exit message and turn off the UnicornHAT

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
#########################################################################
#                          Import modules                              #
########################################################################

import time
import random
import unicornhat
from print_unicornphat_header import print_unicornphat_header

########################################################################
#                           Initialize                                 #
########################################################################

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)


Y_COORDINATES = [0, 1, 2, 3]
X_COORDINATES = [0, 1, 2, 3, 4, 5, 6, 7]

Y0_COLOR_TUPLE = (127, 0, 255)        # Violet
Y1_COLOR_TUPLE = (0, 0, 255)          # Blue
Y2_COLOR_TUPLE = (0, 204, 204)        # Indigo
Y3_COLOR_TUPLE = (255, 255, 255)      # White

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

    function_list = [pibow_zero_vertical_striper_1,
                     pibow_zero_vertical_striper_2,
                     pibow_zero_vertical_striper_3,
                     pibow_zero_vertical_striper_4]
    try:
        while True:
            random.choice(function_list)()
    except KeyboardInterrupt:
        stop()


def get_y_color(y_color_tuple):
    """
    This function extracts the individual red, green, and blue color
    values and returns them.
    """

    return int(y_color_tuple[0]), int(y_color_tuple[1]), \
        int(y_color_tuple[2])


def pibow_zero_vertical_striper_1():
    """
    Gets the x and y coordinates in their original order and sends them
    to the main striping function (pibow_zero_vertical_striper)
    """

    x_coordinate_list = X_COORDINATES
    y_coordinate_list = Y_COORDINATES

    pibow_zero_vertical_striper(x_coordinate_list, y_coordinate_list)


def pibow_zero_vertical_striper_2():
    """
    Gets the x coordinates in their original order. Reverses the order
    of the y coordinates.  Then sends the x and y coordinates to the
    main striping function (pibow_zero_vertical_striper)
    """

    x_coordinate_list = X_COORDINATES
    y_coordinate_list = Y_COORDINATES[::-1]

    pibow_zero_vertical_striper(x_coordinate_list, y_coordinate_list)


def pibow_zero_vertical_striper_3():
    """
    Reverses the order of the x coordinates. Gets the y coordinates in
    their original order.  Then sends the x and y coordinates to the
    main striping function (pibow_zero_vertical_striper)
    """
    x_coordinate_list = X_COORDINATES[::-1]
    y_coordinate_list = Y_COORDINATES

    pibow_zero_vertical_striper(x_coordinate_list, y_coordinate_list)


def pibow_zero_vertical_striper_4():
    """
    Reverses the order of both the x and y coordinates and sends them
    to the main striping function (pibow_zero_vertical_striper)
    """
    x_coordinate_list = X_COORDINATES[::-1]
    y_coordinate_list = Y_COORDINATES[::-1]

    pibow_zero_vertical_striper(x_coordinate_list, y_coordinate_list)


def pibow_zero_vertical_striper(x_coordinate_list, y_coordinate_list):
    """
    Lights up a column of LEDs in a particular color, based on the
    coordinates that were sent to it

    Arguments:
        x_coordinate_list: a list of x coordinates
        y_coordinate_list: a list of y coordinates
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0
    unicornhat.clear()

    while seconds_elapsed < 10:

        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the x coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stop():
    """
    Print exit message and turn off the UnicornHAT
    """
    print("\nExiting program.")
    unicornhat.off()


if __name__ == '__main__':
    main()
