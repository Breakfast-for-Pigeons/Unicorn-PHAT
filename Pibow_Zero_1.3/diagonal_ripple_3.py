#!/usr/bin/python3
"""
Diagonal Ripple 3 - Pibow Zero 1.3

Retrieves the rainbows and sends them to the ripple function.
With the GPIO pins at the top of the Raspberry Pi, the rainbows ripple
from the bottom right to the top left.

....................

Functions:
- diagonal_ripple_3: Gets 12 rainbows and sends them to the ripple
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
from bfp_unicornphat import get_diagonal_ripple_rainbows_2
from bfp_unicornphat import ripple_diagonally

########################################################################
#                            Functions                                 #
########################################################################


def diagonal_ripple_3():
    """
    Gets 12 rainbows and sends them to the ripple diagonally function
    """

    rainbow00 = get_horizontal_rainbow_00()

    rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, rainbow06, \
        rainbow07, rainbow08, rainbow09, rainbow10, \
        rainbow11 = get_diagonal_ripple_rainbows_2()

    diagonal_rainbows_3 = [rainbow01, rainbow02, rainbow03, rainbow04,
                           rainbow05, rainbow06, rainbow07, rainbow08,
                           rainbow09, rainbow10, rainbow11]

    ripple_diagonally(rainbow00, diagonal_rainbows_3)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        diagonal_ripple_3()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
