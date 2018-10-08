#!/usr/bin/python3
"""
Horizontal Ripple 1 - Pibow Zero 1.2

Retrieves the rainbows and sends them to the ripple function.
With the GPIO pins at the top of the Raspberry Pi, the rainbows ripple
from right to left.

....................

Functions:
- horizontal_ripple_2: Gets 9 rainbows and sends them to the ripple
      horizontally function

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
#########################################################################
#                          Import modules                              #
########################################################################

from bfp_unicornphat import print_header
from bfp_unicornphat import stop
from bfp_unicornphat import get_horizontal_rainbow_00
from bfp_unicornphat import get_horizontal_ripple_rainbows
from bfp_unicornphat import ripple_horizontally

########################################################################
#                            Functions                                 #
########################################################################


def horizontal_ripple_1():
    """
    Gets 9 rainbows and sends them to the ripple diagonally function
    """

    rainbow00 = get_horizontal_rainbow_00()

    rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, rainbow06, \
        rainbow07, rainbow08 = get_horizontal_ripple_rainbows()

    ripple_horizontally(rainbow00, rainbow01, rainbow02, rainbow03,
                        rainbow04, rainbow05, rainbow06, rainbow07,
                        rainbow08)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        horizontal_ripple_1()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
