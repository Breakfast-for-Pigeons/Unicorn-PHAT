#!/usr/bin/python3
"""
Double Ripple 4 - Pibow Zero 1.3

Retrieves the rainbows and sends them to the ripple function.
With the GPIO pins at the top of the Raspberry Pi, the rainbows ripple
from the top right to the bottom left.

....................

Functions:
- double_ripple_4: Gets 9 rainbows and sends them to the double ripple
      function

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
from bfp_unicornphat import get_double_ripple_rainbows_2
from bfp_unicornphat import double_ripple

########################################################################
#                            Functions                                 #
########################################################################


def double_ripple_4():
    """
    Gets 9 rainbow, assigns them in reverse order, and sends them to
    the double ripple function
    """

    rainbow00 = get_horizontal_rainbow_00()

    rainbow08, rainbow07, rainbow06, rainbow05, rainbow04, rainbow03, \
        rainbow02, rainbow01 = get_double_ripple_rainbows_2()

    double_ripple(rainbow00, rainbow01, rainbow02, rainbow03, rainbow04,
                  rainbow05, rainbow06, rainbow07, rainbow08)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        double_ripple_4()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
