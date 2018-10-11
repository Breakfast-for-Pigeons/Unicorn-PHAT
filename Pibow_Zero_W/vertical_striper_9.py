#!/usr/bin/python3
"""
Vertical Striper 9 - Pibow Zero W

With the Raspberry Pi oriented with the GPIO pins at the top, this
program stripes from the bottom to the top and from right to left.

This is exactly the same as Vertical Striper 1 except the color order
is reversed.

....................

Functions:
- vertical_striper_9: Gets x and y coordinates and sends them to the
      striping function

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from bfp_unicornphat import print_header
from bfp_unicornphat import stop
from bfp_unicornphat import stripe_vertically_reverse

########################################################################
#                         Import variables                             #
########################################################################

from bfp_unicornphat import X_COORDINATES
from bfp_unicornphat import Y_COORDINATES

########################################################################
#                            Functions                                 #
########################################################################


def vertical_striper_9():
    """
    Gets x and y coordinates and sends them to the striping function
    """

    x_coordinate_list = X_COORDINATES
    y_coordinate_list = Y_COORDINATES

    stripe_vertically_reverse(x_coordinate_list, y_coordinate_list)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        vertical_striper_9()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
