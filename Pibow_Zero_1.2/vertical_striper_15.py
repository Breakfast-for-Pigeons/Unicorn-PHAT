#!/usr/bin/python3
"""
Vertical Striper 7 - Pibow Zero 1.2

With the Raspberry Pi oriented with the GPIO pins at the top, this
program stripes from right to left and alternates between from top to
bottom and from bottom to top.

This is exactly the same at Horizontal Striper 7 except the color order
is reversed.

....................

Functions:
- vertical_striper_7: Gets x and y coordinates and sends them to the
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
from bfp_unicornphat import stripe_vertically_reverse_alt_2

########################################################################
#                         Import variables                             #
########################################################################

from bfp_unicornphat import X_COORDINATES
from bfp_unicornphat import Y_COORDINATES

########################################################################
#                            Functions                                 #
########################################################################


def vertical_striper_15():
    """
    Sends x and y coordinates to the striper function
    """

    x_coordinate_list = X_COORDINATES
    y_coordinate_list = Y_COORDINATES[::-1]

    stripe_vertically_reverse_alt_2(x_coordinate_list, y_coordinate_list)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        vertical_striper_15()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
