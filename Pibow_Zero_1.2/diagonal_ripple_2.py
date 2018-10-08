#!/usr/bin/python3
"""
Diagonal Ripple 2 - Pibow Zero 1.2

Retrieves the rainbows and sends them to the ripple function.
With the GPIO pins at the top of the Raspberry Pi, the rainbows ripple
from the bottom left to the top right.

....................

Functions:
- diagonal_ripple_2: Gets 12 rainbows and sends them to the ripple
      diagonally function

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from bfp_unicornphat import print_header
from bfp_unicornphat import stop
from bfp_unicornphat import get_horizontal_rainbow_00
from bfp_unicornphat import get_diagonal_ripple_rainbows_1
from bfp_unicornphat import ripple_diagonally

########################################################################
#                            Functions                                 #
########################################################################


def diagonal_ripple_2():
    """
    Gets 12 rainbows, but assigns them in reverse order, and sends them
    to the ripple diagonally function
    """

    rainbow00 = get_horizontal_rainbow_00()

    rainbow11, rainbow10, rainbow09, rainbow08, rainbow07, rainbow06, \
        rainbow05, rainbow04, rainbow03, rainbow02, \
        rainbow01 = get_diagonal_ripple_rainbows_1()

    ripple_diagonally(rainbow00, rainbow01, rainbow02, rainbow03,
                      rainbow04, rainbow05, rainbow06, rainbow07,
                      rainbow08, rainbow09, rainbow10, rainbow11)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        diagonal_ripple_2()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
