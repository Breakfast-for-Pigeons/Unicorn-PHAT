#!/usr/bin/python3
"""
bfp_unicornphat - Pibow Zero 1.3

This is a module containing the support functions and variables for my
UnicornPHAT programs. Each program imports only the needed functions and
variables.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

import time
import random
import unicornhat

########################################################################
#                      Initialize UnicornPHAT                          #
########################################################################

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

########################################################################
#                           Variables                                  #
########################################################################

HEADER_COLORS = ['\033[1;31;40m', '\033[1;32;40m', '\033[1;33;40m',
                 '\033[1;34;40m', '\033[1;35;40m', '\033[1;36;40m',
                 '\033[1;37;40m']

R = (255, 0, 0)         # Red
O = (255, 128, 0)       # Orange
Y = (255, 255, 0)       # Yellow
W = (255, 255, 255)     # White
OFF = (0, 0, 0)
R2 = (128, 0, 0)        # Half the values of Red
O2 = (128, 64, 0)       # Half the values of Orange
Y2 = (128, 128, 0)      # Half the values of Yellow
W2 = (128, 128, 128)    # Half the values of White

Y_COORDINATES = [0, 1, 2, 3]
X_COORDINATES = [0, 1, 2, 3, 4, 5, 6, 7]

Y0_COLOR_TUPLE = R      # Red
Y1_COLOR_TUPLE = O      # Orange
Y2_COLOR_TUPLE = Y      # Yellow
Y3_COLOR_TUPLE = W      # White

# Red, Orange, Yellow, White respectively
COLOR_LIST = [R, O, Y, W]

X0_COLOR_TUPLE = R      # Red
X1_COLOR_TUPLE = O      # Orange
X2_COLOR_TUPLE = Y      # Yellow
X3_COLOR_TUPLE = W      # White
X4_COLOR_TUPLE = R      # Red
X5_COLOR_TUPLE = O      # Orange
X6_COLOR_TUPLE = Y      # Yellow
X7_COLOR_TUPLE = W      # White

########################################################################
#                            Functions                                 #
########################################################################


def print_header():
    """
    Prints the UnicornPHAT Header

    Arguments:
       color: the header will be printed in this color
    """

    color = random.choice(HEADER_COLORS)

    print(color)
    print(r"""
  _   _       _                        ____  _   _    _  _____
 | | | |_ __ (_) ___ ___  _ __ _ __   |  _ \| | | |  / \|_   _|
 | | | | '_ \| |/ __/ _ \| '__| '_ \  | |_) | |_| | / _ \ | |
 | |_| | | | | | (_| (_) | |  | | | | |  __/|  _  |/ ___ \| |
  \___/|_| |_|_|\___\___/|_|  |_| |_| |_|   |_| |_/_/   \_\_|


    """)


def stop():
    """
    Print exit message and turn off the UnicornPHAT
    """

    print("\nExiting program.")
    unicornhat.off()


def get_horizontal_rainbow_00():
    """
    Returns the main horizontal rainbow

    Programs that use this function:
        - Diagonal Ripple 1
        - Diagonal Ripple 2
        - Diagonal Ripple 3
        - Diagonal Ripple 4
        - Double Ripple 1
        - Double Ripple 2
        - Double Ripple 3
        - Double Ripple 4
        - Horizontal Ripple 1
        - Horizontal Ripple 2
        - Moving Horizontal Rainbow 1
        - Moving Horizontal Rainbow 2
    """

    rainbow00 = [
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    return rainbow00


def get_diagonal_ripple_rainbows_1():
    """
    Returns 11 diagonal ripple rainbows.

    Programs that use this function:
        - Diagonal Ripple 1
        - Diagonal Ripple 2
        - Diagonal Ripple 3
        - Diagonal Ripple 4
    """

    rainbow01 = [
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [R, O, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        [R, O, Y2, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [R2, O, Y, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        [R, O, Y2, W, R, O, Y, W],
        [R, O, Y, W2, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow05 = [
        [R, O2, Y, W, R, O, Y, W],
        [R, O, Y2, W, R, O, Y, W],
        [R, O, Y, W2, R, O, Y, W],
        [R, O, Y, W, R2, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow06 = [
        [R, O, Y2, W, R, O, Y, W],
        [R, O, Y, W2, R, O, Y, W],
        [R, O, Y, W, R2, O, Y, W],
        [R, O, Y, W, R, O2, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow07 = [
        [R, O, Y, W2, R, O, Y, W],
        [R, O, Y, W, R2, O, Y, W],
        [R, O, Y, W, R, O2, Y, W],
        [R, O, Y, W, R, O, Y2, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow08 = [
        [R, O, Y, W, R2, O, Y, W],
        [R, O, Y, W, R, O2, Y, W],
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O, Y, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow09 = [
        [R, O, Y, W, R, O2, Y, W],
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow10 = [
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow11 = [
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07, rainbow08, rainbow09, rainbow10, rainbow11


def get_diagonal_ripple_rainbows_2():
    """
    Returns 11 diagonal ripple rainbows

    Programs that use this function:
        - Diagonal Ripple 3
        - Diagonal Ripple 4
    """

    rainbow01 = [
        [R2, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [R, O2, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [R, O, Y2, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [R, O, Y, W2, R, O, Y, W],
        [R, O, Y2, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow05 = [
        [R, O, Y, W, R2, O, Y, W],
        [R, O, Y, W2, R, O, Y, W],
        [R, O, Y2, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow06 = [
        [R, O, Y, W, R, O2, Y, W],
        [R, O, Y, W, R2, O, Y, W],
        [R, O, Y, W2, R, O, Y, W],
        [R, O, Y2, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow07 = [
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O2, Y, W],
        [R, O, Y, W, R2, O, Y, W],
        [R, O, Y, W2, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow08 = [
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O2, Y, W],
        [R, O, Y, W, R2, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow09 = [
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O2, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow10 = [
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y2, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow11 = [
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W],
        [R, O, Y, W, R, O, Y, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07, rainbow08, rainbow09, rainbow10, rainbow11


def get_double_ripple_rainbows_1():
    """
    Returns 8 rainbows

    Programs that use this function:
        - Double Ripple 1
        - Double Ripple 2
    """

    rainbow01 = [
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R2, O, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R, O2, Y, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [R, O, Y2, W, R, O, Y, W],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R, O, Y2, W, R, O, Y, W],
        [R, O, Y2, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [R, O, Y, W2, R, O, Y, W],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R, O, Y, W2, R, O, Y, W],
        [R, O, Y, W2, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow05 = [
        [R, O, Y, W, R2, O, Y, W],
        [R, O, Y, W, R2, O, Y, W],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R, O, Y, W, R2, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow06 = [
        [R, O, Y, W, R, O2, Y, W],
        [R, O, Y, W, R, O2, Y, W],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R, O, Y, W, R, O2, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow07 = [
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O, Y2, W],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow08 = [
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y, W2],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07, rainbow08


def get_double_ripple_rainbows_2():
    """
    Returns 8 rainbows

    Programs that use this function:
        - Double Ripple 3
        - Double Ripple 4
    """

    rainbow01 = [
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O, Y2, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [R, O, Y, W, R, O2, Y, W],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R, O, Y, W, R, O2, Y, W],
        [R, O, Y, W, R, O2, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [R, O, Y, W, R2, O, Y, W],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R, O, Y, W, R2, O, Y, W],
        [R, O, Y, W, R2, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow05 = [
        [R, O, Y, W2, R, O, Y, W],
        [R, O, Y, W2, R, O, Y, W],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R, O, Y, W2, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow06 = [
        [R, O, Y2, W, R, O, Y, W],
        [R, O, Y2, W, R, O, Y, W],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        [R, O, Y2, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow07 = [
        [R, O2, Y, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow08 = [
        [R2, O, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        [R2, O2, Y2, W2, R2, O2, Y2, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07, rainbow08


def get_horizontal_ripple_rainbows():
    """
    Returns 8 rainbows

    Programs that use this function:
        - Horizontal Ripple 1
        - Horizontal Ripple 2
    """

    rainbow01 = [
        [R2, O, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        [R2, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [R, O2, Y, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        [R, O2, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [R, O, Y2, W, R, O, Y, W],
        [R, O, Y2, W, R, O, Y, W],
        [R, O, Y2, W, R, O, Y, W],
        [R, O, Y2, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [R, O, Y, W2, R, O, Y, W],
        [R, O, Y, W2, R, O, Y, W],
        [R, O, Y, W2, R, O, Y, W],
        [R, O, Y, W2, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow05 = [
        [R, O, Y, W, R2, O, Y, W],
        [R, O, Y, W, R2, O, Y, W],
        [R, O, Y, W, R2, O, Y, W],
        [R, O, Y, W, R2, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow06 = [
        [R, O, Y, W, R, O2, Y, W],
        [R, O, Y, W, R, O2, Y, W],
        [R, O, Y, W, R, O2, Y, W],
        [R, O, Y, W, R, O2, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow07 = [
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O, Y2, W],
        [R, O, Y, W, R, O, Y2, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow08 = [
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y, W2],
        [R, O, Y, W, R, O, Y, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04, rainbow05, \
        rainbow06, rainbow07, rainbow08


def get_diagonal_rainbows_1():
    """
    Returns 4 different versions of diagonal rainbows

    Programs that use this function:
        - Moving Diagonal Rainbow 1
        - Moving Diagonal Rainbow 2
    """

    rainbow00 = [
        [W, R, O, Y, W, R, O, Y],
        [Y, W, R, O, Y, W, R, O],
        [O, Y, W, R, O, Y, W, R],
        [R, O, Y, W, R, O, Y, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow01 = [
        [Y, W, R, O, Y, W, R, O],
        [O, Y, W, R, O, Y, W, R],
        [R, O, Y, W, R, O, Y, W],
        [W, R, O, Y, W, R, O, Y],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [O, Y, W, R, O, Y, W, R],
        [R, O, Y, W, R, O, Y, W],
        [W, R, O, Y, W, R, O, Y],
        [Y, W, R, O, Y, W, R, O],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]
    rainbow03 = [
        [R, O, Y, W, R, O, Y, W],
        [W, R, O, Y, W, R, O, Y],
        [Y, W, R, O, Y, W, R, O],
        [O, Y, W, R, O, Y, W, R],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    return rainbow00, rainbow01, rainbow02, rainbow03


def get_diagonal_rainbows_2():
    """
    Returns 4 different versions of diagonal rainbows

    Programs that use this function:
        - Moving Diagonal Rainbow 3
        - Moving Diagonal Rainbow 4
    """

    rainbow00 = [
        [Y, O, R, W, Y, O, R, W],
        [O, R, W, Y, O, R, W, Y],
        [R, W, Y, O, R, W, Y, O],
        [W, Y, O, R, W, Y, O, R],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow01 = [
        [O, R, W, Y, O, R, W, Y],
        [R, W, Y, O, R, W, Y, O],
        [W, Y, O, R, W, Y, O, R],
        [Y, O, R, W, Y, O, R, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [R, W, Y, O, R, W, Y, O],
        [W, Y, O, R, W, Y, O, R],
        [Y, O, R, W, Y, O, R, W],
        [O, R, W, Y, O, R, W, Y],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]
    rainbow03 = [
        [W, Y, O, R, W, Y, O, R],
        [Y, O, R, W, Y, O, R, W],
        [O, R, W, Y, O, R, W, Y],
        [R, W, Y, O, R, W, Y, O],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    return rainbow00, rainbow01, rainbow02, rainbow03


def get_horizontal_rainbows():
    """
    Returns 3 different versions of horizontal rainbows

    Programs that use this function:
        - Moving Horizontal Rainbow 1
        - Moving Horizontal Rainbow 2
    """

    rainbow01 = [
        [O, Y, W, R, O, Y, W, R],
        [O, Y, W, R, O, Y, W, R],
        [O, Y, W, R, O, Y, W, R],
        [O, Y, W, R, O, Y, W, R],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [Y, W, R, O, Y, W, R, O],
        [Y, W, R, O, Y, W, R, O],
        [Y, W, R, O, Y, W, R, O],
        [Y, W, R, O, Y, W, R, O],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [W, R, O, Y, W, R, O, Y],
        [W, R, O, Y, W, R, O, Y],
        [W, R, O, Y, W, R, O, Y],
        [W, R, O, Y, W, R, O, Y],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    return rainbow01, rainbow02, rainbow03


def get_vertical_rainbow_00():
    """
    Returns the main vertical rainbow

    Programs that use this function:
        - Moving Vertical Rainbow 1
        - Moving Vertical Rainbow 2
        - Vertical Ripple 1
        - Vertical Ripple 1
    """

    rainbow00 = [
        [W, W, W, W, W, W, W, W],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [O, O, O, O, O, O, O, O],
        [R, R, R, R, R, R, R, R],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
        ]

    return rainbow00


def get_vertical_rainbows():
    """
    Returns 3 different versions of vertical rainbows

    Programs that use this function:
        - Moving Vertical Rainbow 1
        - Moving Vertical Rainbow 2
    """

    rainbow01 = [
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [O, O, O, O, O, O, O, O],
        [R, R, R, R, R, R, R, R],
        [W, W, W, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [O, O, O, O, O, O, O, O],
        [R, R, R, R, R, R, R, R],
        [W, W, W, W, W, W, W, W],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [R, R, R, R, R, R, R, R],
        [W, W, W, W, W, W, W, W],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [O, O, O, O, O, O, O, O],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    return rainbow01, rainbow02, rainbow03


def get_vertical_ripple_rainbows():
    """
    Returns 4 vertical rainbows


    Programs that use this function:
        - Vertical Ripple 1
        - Vertical Ripple 2
    """

    rainbow01 = [
        [W2, W2, W2, W2, W2, W2, W2, W2],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [O, O, O, O, O, O, O, O],
        [R, R, R, R, R, R, R, R],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [W, W, W, W, W, W, W, W],
        [Y2, Y2, Y2, Y2, Y2, Y2, Y2, Y2],
        [O, O, O, O, O, O, O, O],
        [R, R, R, R, R, R, R, R],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [W, W, W, W, W, W, W, W],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [O2, O2, O2, O2, O2, O2, O2, O2],
        [R, R, R, R, R, R, R, R],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [W, W, W, W, W, W, W, W],
        [Y, Y, Y, Y, Y, Y, Y, Y],
        [O, O, O, O, O, O, O, O],
        [R2, R2, R2, R2, R2, R2, R2, R2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    return rainbow01, rainbow02, rainbow03, rainbow04


def get_y_color(y_color_tuple):
    """
    Extracts 3 individual integers from a tuple and returns them.

    Programs that use this function:
        - Horizontal Striper 1
        - Horizontal Striper 2
        - Horizontal Striper 3
        - Horizontal Striper 4
        - Horizontal Striper 5
        - Horizontal Striper 6
        - Horizontal Striper 7
        - Horizontal Striper 8
        - Horizontal Striper 9
        - Horizontal Striper 10
        - Horizontal Striper 11
        - Horizontal Striper 12
        - Horizontal Striper 13
        - Horizontal Striper 14
        - Horizontal Striper 15
        - Horizontal Striper 16
    """

    return int(y_color_tuple[0]), int(y_color_tuple[1]), \
        int(y_color_tuple[2])


def get_x_color(x_color_tuple):
    """
    Extracts 3 individual integers from a tuple and returns them.

    Programs that use this function:
        - Vertical Striper 1
        - Vertical  Striper 2
        - Vertical  Striper 3
        - Vertical  Striper 4
        - Vertical  Striper 5
        - Vertical  Striper 6
        - Vertical  Striper 7
        - Vertical  Striper 8
        - Vertical  Striper 9
        - Vertical  Striper 10
        - Vertical  Striper 11
        - Vertical  Striper 12
        - Vertical  Striper 13
        - Vertical  Striper 14
        - Vertical  Striper 15
        - Vertical  Striper 16
    """

    return int(x_color_tuple[0]), int(x_color_tuple[1]), \
        int(x_color_tuple[2])


def ripple_diagonally(rainbow00, rainbow01, rainbow02, rainbow03,
                      rainbow04, rainbow05, rainbow06, rainbow07,
                      rainbow08, rainbow09, rainbow10, rainbow11):
    """
    Cycles through 12 rainbows to make them ripple diagonally

    Arguments:
        Rainbows 00 through 11

    Programs that use this function:
        - Diagonal Ripple 1
        - Diagonal Ripple 2
        - Diagonal Ripple 3
        - Diagonal Ripple 4
    """

    rainbow00 = rainbow00
    rainbows = [rainbow01, rainbow02, rainbow03, rainbow04,
                rainbow05, rainbow06, rainbow07, rainbow08,
                rainbow09, rainbow10, rainbow11]

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Show main horizontal rainbow
        seconds_elapsed = time.time() - start_time
        unicornhat.set_pixels(rainbow00)
        unicornhat.show()
        time.sleep(2.0)
        # Loop through the rainbows so they appear to ripple
        for rainbow in rainbows:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def double_ripple(rainbow00, rainbow01, rainbow02, rainbow03, rainbow04,
                  rainbow05, rainbow06, rainbow07, rainbow08):
    """
    Cycles through 9 rainbows to ripple them

    Arguments:
        Rainbows 00 through 08

    Programs that use this function:
        - Double Ripple 1
        - Double Ripple 2
        - Double Ripple 3
        - Double Ripple 4
    """

    rainbow00 = rainbow00
    rainbows = [rainbow01, rainbow02, rainbow03, rainbow04,
                rainbow05, rainbow06, rainbow07, rainbow08]

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Show main horizontal rainbow
        seconds_elapsed = time.time() - start_time
        unicornhat.set_pixels(rainbow00)
        unicornhat.show()
        time.sleep(2.0)
        # Loop through the rainbows so they appear to ripple
        for rainbow in rainbows:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def ripple_horizontally(rainbow00, rainbow01, rainbow02, rainbow03,
                        rainbow04, rainbow05, rainbow06, rainbow07,
                        rainbow08):
    """
    Cycles through 9 rainbows to ripple them horizontally

    Programs that use this function:
        - Horizontal Ripple 1
        - Horizontal Ripple 1
    """

    rainbow00 = rainbow00
    rainbows = [rainbow01, rainbow02, rainbow03, rainbow04,
                rainbow05, rainbow06, rainbow07, rainbow08]

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Show main horizontal rainbow
        seconds_elapsed = time.time() - start_time
        unicornhat.set_pixels(rainbow00)
        unicornhat.show()
        time.sleep(2.0)
        # Loop through the rainbows so they appear to ripple
        for rainbow in rainbows:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def stripe_horizontally(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 3

    Programs that use this function:
        - Horizontal Striper 1
        - Horizontal Striper 2
        - Horizontal Striper 3
        - Horizontal Striper 4
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
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


def stripe_horizontally_alternate(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. It alternates from right to left and left to right.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs that use this function:
        - Horizontal Striper 5
        - Horizontal Striper 6
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)

            # Light up selected y column, alternately
            if y_coordinate_list[y_coordinate] == 0 or \
               y_coordinate_list[y_coordinate] == 2 or \
               y_coordinate_list[y_coordinate] == 4 or \
               y_coordinate_list[y_coordinate] == 6:
                x_coordinate_list = X_COORDINATES
            else:
                x_coordinate_list = X_COORDINATES[::-1]

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_horizontally_alternate_2(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. It alternates from left to right to right to left.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

     Programs that use this function:
        - Horizontal Striper 7
        - Horizontal Striper 8
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)

            # Light up selected y column, alternately
            if y_coordinate_list[y_coordinate] == 0 or \
               y_coordinate_list[y_coordinate] == 2 or \
               y_coordinate_list[y_coordinate] == 4 or \
               y_coordinate_list[y_coordinate] == 6:
                x_coordinate_list = X_COORDINATES[::-1]
            else:
                x_coordinate_list = X_COORDINATES

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_horizontally_reverse(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 3

    Programs that use this function:
        - Horizontal Striper 9
        - Horizontal Striper 10
        - Horizontal Striper 11
        - Horizontal Striper 12
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_horizontally_reverse_alt(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. This function is used with Horizontal Striper 5 and 6.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs that use this function:
        - Horizontal Striper 13
        - Horizontal Striper 14
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)

            # Light up selected y column, alternately
            if y_coordinate_list[y_coordinate] == 0 or \
               y_coordinate_list[y_coordinate] == 2 or \
               y_coordinate_list[y_coordinate] == 4 or \
               y_coordinate_list[y_coordinate] == 6:
                x_coordinate_list = X_COORDINATES
            else:
                x_coordinate_list = X_COORDINATES[::-1]

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_horizontally_reverse_alt_2(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. This function is used with Horizontal Striper 7 and 8.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs that use this function:
        - Horizontal Striper 15
        - Horizontal Striper 16
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for y_coordinate in y_coordinate_list:
            # Get the RGB color for the y coordinate
            if y_coordinate == 0:
                red, green, blue = get_y_color(Y3_COLOR_TUPLE)
            if y_coordinate == 1:
                red, green, blue = get_y_color(Y2_COLOR_TUPLE)
            if y_coordinate == 2:
                red, green, blue = get_y_color(Y1_COLOR_TUPLE)
            if y_coordinate == 3:
                red, green, blue = get_y_color(Y0_COLOR_TUPLE)

            # Light up selected y column, alternately
            if y_coordinate_list[y_coordinate] == 0 or \
               y_coordinate_list[y_coordinate] == 2 or \
               y_coordinate_list[y_coordinate] == 4 or \
               y_coordinate_list[y_coordinate] == 6:
                x_coordinate_list = X_COORDINATES[::-1]
            else:
                x_coordinate_list = X_COORDINATES

            for x_coordinate in x_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def move_diagonally(rainbow00, rainbow01, rainbow02, rainbow03):
    """
    Cycles through 4 rainbows to make them appear to move diagonally

    Arguments:
        4 different rainbow imagaes for the UnicornPHAT

    Programs that use this function:
        - Moving Diagonal Rainbow 1
        - Moving Diagonal Rainbow 2
        - Moving Diagonal Rainbow 3
        - Moving Diagonal Rainbow 4
    """

    rainbows = [rainbow00, rainbow01, rainbow02, rainbow03]

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Loop through the rainbows so they appear to move
        for rainbow in rainbows:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.5)


def move_horizontally(rainbow00, rainbow01, rainbow02, rainbow03):
    """
    Cycles through 4 rainbows to make them appear to move horizontally

    This function runs for 10 seconds

    Arguments:
        4 different rainbow imagaes for the UnicornPHAT

    Programs that use this function:
        - Moving Horizontal Rainbow 1
        - Moving Horizontal Rainbow 2
    """

    rainbows = [rainbow00, rainbow01, rainbow02, rainbow03]

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Loop through the rainbows so they appear to move
        for rainbow in rainbows:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.5)


def move_vertically(rainbow00, rainbow01, rainbow02, rainbow03):
    """
    Cycles through 4 rainbows to make them appear to move vertically

    Programs that use this function:
        - Moving Vertical Rainbow 1
        - Moving Vertical Rainbow 2
    """

    rainbows = [rainbow00, rainbow01, rainbow02, rainbow03]

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Loop through the rainbows so they appear to move
        for rainbow in rainbows:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.5)


def get_random_color():
    """
    Extracts 3 individual integers from a tuple and returns them.

    The integers represent the red, green, and blue color values
    respectively. Index 0 is red, index 1 is green, index 2 is blue.

    Programs that use this function:
        - Sprinkles
    """

    color_tuple = random.choice(COLOR_LIST)

    return int(color_tuple[0]), int(color_tuple[1]), int(color_tuple[2])


def light_up_random_led(red, green, blue):
    """
    Lights up a random LED

    Arguments:
        red, green, and blue: integers that represent the amount of
            red, green, and blue in an LED

     Programs that use this function:
        - Sprinkles
    """

    unicornhat.set_pixel(random_x_coordinate(), random_y_coordinate(),
                         red, green, blue)


def random_x_coordinate():
    """
    Returns a random x coordinate

    Programs that use this function:
        - Sprinkles
    """

    return int(random.choice(X_COORDINATES))


def random_y_coordinate():
    """
    Returns a random y coordinate

    Programs that use this function:
        - Sprinkles
    """

    return int(random.choice(Y_COORDINATES))


def ripple_vertically(rainbow00, rainbow01, rainbow02, rainbow03,
                      rainbow04):
    """
    Cycles through 5 rainbows to ripple them vertically

    Programs that use this function:
        - Vertical Ripple 1
        - Vertical Ripple 2
    """

    rainbow00 = rainbow00
    rainbows = [rainbow01, rainbow02, rainbow03, rainbow04]

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Show main vertical rainbow
        unicornhat.set_pixels(rainbow00)
        unicornhat.show()
        time.sleep(2.0)
        # Loop through the rainbows so they appear to ripple
        for rainbow in rainbows:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def stripe_vertically(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 3

    Programs that use this function:
        - Vertical Striper 1
        - Vertical Striper 2
        - Vertical Striper 3
        - Vertical Striper 4
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)

            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_vertically_alternate(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs that use this function:
        - Vertical Striper 5
        - Vertical Striper 6
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)
            # Light up selected x column, alternately
            if x_coordinate_list[x_coordinate] == 0 or \
               x_coordinate_list[x_coordinate] == 2 or \
               x_coordinate_list[x_coordinate] == 4 or \
               x_coordinate_list[x_coordinate] == 6:
                y_coordinate_list = Y_COORDINATES
            else:
                y_coordinate_list = Y_COORDINATES[::-1]
            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_vertically_alternate_2(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs in this function:
        - Vertical Striper 7
        - Vertical Striper 8
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)
            # Light up selected x column, alternately
            if x_coordinate_list[x_coordinate] == 0 or \
               x_coordinate_list[x_coordinate] == 2 or \
               x_coordinate_list[x_coordinate] == 4 or \
               x_coordinate_list[x_coordinate] == 6:
                y_coordinate_list = Y_COORDINATES[::-1]
            else:
                y_coordinate_list = Y_COORDINATES
            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_vertically_reverse(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 3

    Programs that use this function:
        - Vertical Striper 9
        - Vertical Striper 10
        - Vertical Striper 11
        - Vertical Striper 12
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 15:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the y coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)

            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_vertically_reverse_alt(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7

    Programs that use this function:
        - Vertical Striper 13
        - Vertical Striper 14
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)
            # Light up selected x column, alternately
            if x_coordinate_list[x_coordinate] == 0 or \
               x_coordinate_list[x_coordinate] == 2 or \
               x_coordinate_list[x_coordinate] == 4 or \
               x_coordinate_list[x_coordinate] == 6:
                y_coordinate_list = Y_COORDINATES
            else:
                y_coordinate_list = Y_COORDINATES[::-1]
            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)


def stripe_vertically_reverse_alt_2(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. This function is used with Vertical Striper 7 and 8

    Arguments:
        x_coordidate_list: a list of the numbers 0 - 7
        y_coordidate_list: a list of the numbers 0 - 7


    Programs that use this function:
        - Vertical Striper 15
        - Vertical Striper 16
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        seconds_elapsed = time.time() - start_time
        unicornhat.clear()

        for x_coordinate in x_coordinate_list:
            # Get the RGB color for the x_coordinate coordinate
            if x_coordinate == 0:
                red, green, blue, = get_x_color(X7_COLOR_TUPLE)
            if x_coordinate == 1:
                red, green, blue, = get_x_color(X6_COLOR_TUPLE)
            if x_coordinate == 2:
                red, green, blue, = get_x_color(X5_COLOR_TUPLE)
            if x_coordinate == 3:
                red, green, blue, = get_x_color(X4_COLOR_TUPLE)
            if x_coordinate == 4:
                red, green, blue, = get_x_color(X3_COLOR_TUPLE)
            if x_coordinate == 5:
                red, green, blue, = get_x_color(X2_COLOR_TUPLE)
            if x_coordinate == 6:
                red, green, blue, = get_x_color(X1_COLOR_TUPLE)
            if x_coordinate == 7:
                red, green, blue, = get_x_color(X0_COLOR_TUPLE)
            # Light up selected x column, alternately
            if x_coordinate_list[x_coordinate] == 0 or \
               x_coordinate_list[x_coordinate] == 2 or \
               x_coordinate_list[x_coordinate] == 4 or \
               x_coordinate_list[x_coordinate] == 6:
                y_coordinate_list = Y_COORDINATES[::-1]
            else:
                y_coordinate_list = Y_COORDINATES
            for y_coordinate in y_coordinate_list:
                unicornhat.set_pixel(x_coordinate, y_coordinate,
                                     red, green, blue)
                unicornhat.show()
                time.sleep(0.05)
        time.sleep(1.0)
