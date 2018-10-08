#!/usr/bin/python3
"""
Vertical Striper 3 - Pibow Zero 1.2

With the Raspberry Pi oriented with the GPIO pins at the top, this
program stripes from the bottom to the top and from left to right.

....................

Functions:
- vertical_striper_3: Gets x and y coordinates and sends them to the
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
from bfp_unicornphat import stripe_vertically

########################################################################
#                         Import variables                             #
########################################################################

from bfp_unicornphat import X_COORDINATES
from bfp_unicornphat import Y_COORDINATES

########################################################################
#                            Functions                                 #
########################################################################


def vertical_striper_3():
    """
    Gets x and y coordinates and sends them to the striping function

    This version reverses the order of the x coordinates.
    """

    x_coordinate_list = X_COORDINATES[::-1]
    y_coordinate_list = Y_COORDINATES

    stripe_vertically(x_coordinate_list, y_coordinate_list)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        vertical_striper_3()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
