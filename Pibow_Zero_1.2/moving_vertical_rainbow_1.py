#!/usr/bin/python3
"""
Moving Vertical Rainbow 1 - Pibow Zero 1.2

Retrieves the rainbows and sends them to the move function.
With the GPIO pins at the top of the Raspberry Pi, the rainbows move
from top to bottom.

....................

Functions:
- moving_vertical_rainbow_1: Retrieves the Pibow Zero rainbows and
      sends them to the move function.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from bfp_unicornphat import print_header
from bfp_unicornphat import stop
from bfp_unicornphat import get_vertical_rainbow_00
from bfp_unicornphat import get_vertical_rainbows
from bfp_unicornphat import move_vertically

########################################################################
#                            Functions                                 #
########################################################################


def moving_vertical_rainbow_1():
    """
    Retrieves the rainbows and sends them as an argument to the move
    function.
    """

    rainbow00 = get_vertical_rainbow_00()

    rainbow01, rainbow02, rainbow03 = get_vertical_rainbows()

    mv_rainbows_1 = (rainbow00, rainbow01, rainbow02, rainbow03)

    move_vertically(mv_rainbows_1)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        moving_vertical_rainbow_1()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
