#!/usr/bin/python3
"""
Pibow Zero 1.2 Demo

This program is a collection of all my Pibow Candy programs. It picks
one at random and runs it for 15 seconds.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
#########################################################################
#                          Import modules                              #
########################################################################

import random
from bfp_unicornphat import print_header
from bfp_unicornphat import stop
from cycle_colors import cycle_colors
from diagonal_ripple_1 import diagonal_ripple_1
from diagonal_ripple_2 import diagonal_ripple_2
from diagonal_ripple_3 import diagonal_ripple_3
from diagonal_ripple_4 import diagonal_ripple_4
from double_ripple_1 import double_ripple_1
from double_ripple_2 import double_ripple_2
from double_ripple_3 import double_ripple_3
from double_ripple_4 import double_ripple_4
from horizontal_ripple_1 import horizontal_ripple_1
from horizontal_ripple_2 import horizontal_ripple_2
from horizontal_striper_1 import horizontal_striper_1
from horizontal_striper_2 import horizontal_striper_2
from horizontal_striper_3 import horizontal_striper_3
from horizontal_striper_4 import horizontal_striper_4
from horizontal_striper_5 import horizontal_striper_5
from horizontal_striper_6 import horizontal_striper_6
from horizontal_striper_7 import horizontal_striper_7
from horizontal_striper_8 import horizontal_striper_8
from horizontal_striper_9 import horizontal_striper_9
from horizontal_striper_10 import horizontal_striper_10
from horizontal_striper_11 import horizontal_striper_11
from horizontal_striper_12 import horizontal_striper_12
from horizontal_striper_13 import horizontal_striper_13
from horizontal_striper_14 import horizontal_striper_14
from horizontal_striper_15 import horizontal_striper_15
from horizontal_striper_16 import horizontal_striper_16
from moving_diagonal_rainbow_1 import moving_diagonal_rainbow_1
from moving_diagonal_rainbow_2 import moving_diagonal_rainbow_2
from moving_diagonal_rainbow_3 import moving_diagonal_rainbow_3
from moving_diagonal_rainbow_4 import moving_diagonal_rainbow_4
from moving_horizontal_rainbow_1 import moving_horizontal_rainbow_1
from moving_horizontal_rainbow_2 import moving_horizontal_rainbow_2
from moving_vertical_rainbow_1 import moving_vertical_rainbow_1
from moving_vertical_rainbow_2 import moving_vertical_rainbow_2
from sprinkles import sprinkles
from vertical_ripple_1 import vertical_ripple_1
from vertical_ripple_2 import vertical_ripple_2
from vertical_striper_1 import vertical_striper_1
from vertical_striper_2 import vertical_striper_2
from vertical_striper_3 import vertical_striper_3
from vertical_striper_4 import vertical_striper_4
from vertical_striper_5 import vertical_striper_5
from vertical_striper_6 import vertical_striper_6
from vertical_striper_7 import vertical_striper_7
from vertical_striper_8 import vertical_striper_8
from vertical_striper_9 import vertical_striper_9
from vertical_striper_10 import vertical_striper_10
from vertical_striper_11 import vertical_striper_11
from vertical_striper_12 import vertical_striper_12
from vertical_striper_13 import vertical_striper_13
from vertical_striper_14 import vertical_striper_14
from vertical_striper_15 import vertical_striper_15
from vertical_striper_16 import vertical_striper_16

########################################################################
#                            Functions                                 #
########################################################################


def pibow_zero_13_demo():
    """
    Selects a random function from a list and runs it.
    """

    function_list = [cycle_colors, diagonal_ripple_1, diagonal_ripple_2,
                     diagonal_ripple_3, diagonal_ripple_4,
                     double_ripple_1, double_ripple_2, double_ripple_3,
                     double_ripple_4, horizontal_ripple_1,
                     horizontal_ripple_2, horizontal_striper_1,
                     horizontal_striper_2, horizontal_striper_3,
                     horizontal_striper_4, horizontal_striper_5,
                     horizontal_striper_6, horizontal_striper_7,
                     horizontal_striper_8, horizontal_striper_9,
                     horizontal_striper_10, horizontal_striper_11,
                     horizontal_striper_12, horizontal_striper_13,
                     horizontal_striper_14, horizontal_striper_15,
                     horizontal_striper_16, moving_diagonal_rainbow_1,
                     moving_diagonal_rainbow_2, moving_diagonal_rainbow_3,
                     moving_diagonal_rainbow_4, moving_horizontal_rainbow_1,
                     moving_horizontal_rainbow_2, moving_vertical_rainbow_1,
                     moving_vertical_rainbow_2, sprinkles,
                     vertical_ripple_1, vertical_ripple_2,
                     vertical_striper_1, vertical_striper_2,
                     vertical_striper_3, vertical_striper_4,
                     vertical_striper_5, vertical_striper_6,
                     vertical_striper_7, vertical_striper_8,
                     vertical_striper_9, vertical_striper_10,
                     vertical_striper_11, vertical_striper_12,
                     vertical_striper_13, vertical_striper_14,
                     vertical_striper_15, vertical_striper_16]

    cycle_colors()

    # Keep selecting a random function until Ctrl-C is pressed
    while True:
        random.choice(function_list)()


if __name__ == '__main__':
    # STEP01: Print header
    print_header()
    # STEP02: Print instructions in white text
    print("\033[1;37;40mPress Ctrl-C to stop the program.")
    # STEP03: Run Demo
    try:
        pibow_zero_13_demo()
    except KeyboardInterrupt:
        stop()
