#!/usr/bin/python3
"""
bfp_unicornphat - Pibow Zero 1.2

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

V = (127, 0, 255)       # Violet
B = (0, 0, 255)         # Blue
I = (0, 204, 204)       # Indigo
W = (255, 255, 255)     # White
OFF = (0, 0, 0)
V2 = (64, 0, 128)       # Half the values of Violet
B2 = (0, 0, 128)        # Half the values of Blue
I2 = (0, 102, 102)      # Half the values of Indigo
W2 = (128, 128, 128)    # Half the values of White

Y_COORDINATES = [0, 1, 2, 3]
X_COORDINATES = [0, 1, 2, 3, 4, 5, 6, 7]

Y0_COLOR_TUPLE = V      # Violet
Y1_COLOR_TUPLE = B      # Blue
Y2_COLOR_TUPLE = I      # Indigo
Y3_COLOR_TUPLE = W      # White

# Violet, Blue, Indigo, White respectively
COLOR_LIST = [V, B, I, W]

X0_COLOR_TUPLE = V      # Violet
X1_COLOR_TUPLE = B      # Blue
X2_COLOR_TUPLE = I      # Indigo
X3_COLOR_TUPLE = W      # White
X4_COLOR_TUPLE = V      # Violet
X5_COLOR_TUPLE = B      # Blue
X6_COLOR_TUPLE = I      # Indigo
X7_COLOR_TUPLE = W      # White

########################################################################
#                            Functions                                 #
########################################################################


def print_header():
    """
    Prints the UnicornPHAT Header
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
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
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
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [V, B, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        [V, B, I2, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [V2, B, I, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        [V, B, I2, W, V, B, I, W],
        [V, B, I, W2, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow05 = [
        [V, B2, I, W, V, B, I, W],
        [V, B, I2, W, V, B, I, W],
        [V, B, I, W2, V, B, I, W],
        [V, B, I, W, V2, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow06 = [
        [V, B, I2, W, V, B, I, W],
        [V, B, I, W2, V, B, I, W],
        [V, B, I, W, V2, B, I, W],
        [V, B, I, W, V, B2, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow07 = [
        [V, B, I, W2, V, B, I, W],
        [V, B, I, W, V2, B, I, W],
        [V, B, I, W, V, B2, I, W],
        [V, B, I, W, V, B, I2, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow08 = [
        [V, B, I, W, V2, B, I, W],
        [V, B, I, W, V, B2, I, W],
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B, I, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow09 = [
        [V, B, I, W, V, B2, I, W],
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow10 = [
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow11 = [
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
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
        [V2, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [V, B2, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [V, B, I2, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [V, B, I, W2, V, B, I, W],
        [V, B, I2, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow05 = [
        [V, B, I, W, V2, B, I, W],
        [V, B, I, W2, V, B, I, W],
        [V, B, I2, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow06 = [
        [V, B, I, W, V, B2, I, W],
        [V, B, I, W, V2, B, I, W],
        [V, B, I, W2, V, B, I, W],
        [V, B, I2, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow07 = [
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B2, I, W],
        [V, B, I, W, V2, B, I, W],
        [V, B, I, W2, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow08 = [
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B2, I, W],
        [V, B, I, W, V2, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow09 = [
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B2, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow10 = [
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I2, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow11 = [
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W],
        [V, B, I, W, V, B, I, W2],
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
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V2, B, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V, B2, I, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [V, B, I2, W, V, B, I, W],
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V, B, I2, W, V, B, I, W],
        [V, B, I2, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [V, B, I, W2, V, B, I, W],
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V, B, I, W2, V, B, I, W],
        [V, B, I, W2, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow05 = [
        [V, B, I, W, V2, B, I, W],
        [V, B, I, W, V2, B, I, W],
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V, B, I, W, V2, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow06 = [
        [V, B, I, W, V, B2, I, W],
        [V, B, I, W, V, B2, I, W],
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V, B, I, W, V, B2, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow07 = [
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B, I2, W],
        [V2, B2, I2, W2, V2, B2, I2, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow08 = [
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I, W2],
        [V2, B2, I2, W2, V2, B2, I2, W2],
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
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B, I2, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [V, B, I, W, V, B2, I, W],
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V, B, I, W, V, B2, I, W],
        [V, B, I, W, V, B2, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [V, B, I, W, V2, B, I, W],
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V, B, I, W, V2, B, I, W],
        [V, B, I, W, V2, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow05 = [
        [V, B, I, W2, V, B, I, W],
        [V, B, I, W2, V, B, I, W],
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V, B, I, W2, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow06 = [
        [V, B, I2, W, V, B, I, W],
        [V, B, I2, W, V, B, I, W],
        [V2, B2, I2, W2, V2, B2, I2, W2],
        [V, B, I2, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow07 = [
        [V, B2, I, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        [V2, B2, I2, W2, V2, B2, I2, W2],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow08 = [
        [V2, B, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        [V2, B2, I2, W2, V2, B2, I2, W2],
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
        [V2, B, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        [V2, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [V, B2, I, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        [V, B2, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [V, B, I2, W, V, B, I, W],
        [V, B, I2, W, V, B, I, W],
        [V, B, I2, W, V, B, I, W],
        [V, B, I2, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [V, B, I, W2, V, B, I, W],
        [V, B, I, W2, V, B, I, W],
        [V, B, I, W2, V, B, I, W],
        [V, B, I, W2, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow05 = [
        [V, B, I, W, V2, B, I, W],
        [V, B, I, W, V2, B, I, W],
        [V, B, I, W, V2, B, I, W],
        [V, B, I, W, V2, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow06 = [
        [V, B, I, W, V, B2, I, W],
        [V, B, I, W, V, B2, I, W],
        [V, B, I, W, V, B2, I, W],
        [V, B, I, W, V, B2, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow07 = [
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B, I2, W],
        [V, B, I, W, V, B, I2, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow08 = [
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I, W2],
        [V, B, I, W, V, B, I, W2],
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
        [W, V, B, I, W, V, B, I],
        [I, W, V, B, I, W, V, B],
        [B, I, W, V, B, I, W, V],
        [V, B, I, W, V, B, I, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow01 = [
        [I, W, V, B, I, W, V, B],
        [B, I, W, V, B, I, W, V],
        [V, B, I, W, V, B, I, W],
        [W, V, B, I, W, V, B, I],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [B, I, W, V, B, I, W, V],
        [V, B, I, W, V, B, I, W],
        [W, V, B, I, W, V, B, I],
        [I, W, V, B, I, W, V, B],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]
    rainbow03 = [
        [V, B, I, W, V, B, I, W],
        [W, V, B, I, W, V, B, I],
        [I, W, V, B, I, W, V, B],
        [B, I, W, V, B, I, W, V],
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
        [I, B, V, W, I, B, V, W],
        [B, V, W, I, B, V, W, I],
        [V, W, I, B, V, W, I, B],
        [W, I, B, V, W, I, B, V],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow01 = [
        [B, V, W, I, B, V, W, I],
        [V, W, I, B, V, W, I, B],
        [W, I, B, V, W, I, B, V],
        [I, B, V, W, I, B, V, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [V, W, I, B, V, W, I, B],
        [W, I, B, V, W, I, B, V],
        [I, B, V, W, I, B, V, W],
        [B, V, W, I, B, V, W, I],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]
    rainbow03 = [
        [W, I, B, V, W, I, B, V],
        [I, B, V, W, I, B, V, W],
        [B, V, W, I, B, V, W, I],
        [V, W, I, B, V, W, I, B],
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
        [B, I, W, V, B, I, W, V],
        [B, I, W, V, B, I, W, V],
        [B, I, W, V, B, I, W, V],
        [B, I, W, V, B, I, W, V],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [I, W, V, B, I, W, V, B],
        [I, W, V, B, I, W, V, B],
        [I, W, V, B, I, W, V, B],
        [I, W, V, B, I, W, V, B],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [W, V, B, I, W, V, B, I],
        [W, V, B, I, W, V, B, I],
        [W, V, B, I, W, V, B, I],
        [W, V, B, I, W, V, B, I],
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
        [I, I, I, I, I, I, I, I],
        [B, B, B, B, B, B, B, B],
        [V, V, V, V, V, V, V, V],
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
        [I, I, I, I, I, I, I, I],
        [B, B, B, B, B, B, B, B],
        [V, V, V, V, V, V, V, V],
        [W, W, W, W, W, W, W, W],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [B, B, B, B, B, B, B, B],
        [V, V, V, V, V, V, V, V],
        [W, W, W, W, W, W, W, W],
        [I, I, I, I, I, I, I, I],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [V, V, V, V, V, V, V, V],
        [W, W, W, W, W, W, W, W],
        [I, I, I, I, I, I, I, I],
        [B, B, B, B, B, B, B, B],
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
        [I, I, I, I, I, I, I, I],
        [B, B, B, B, B, B, B, B],
        [V, V, V, V, V, V, V, V],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow02 = [
        [W, W, W, W, W, W, W, W],
        [I2, I2, I2, I2, I2, I2, I2, I2],
        [B, B, B, B, B, B, B, B],
        [V, V, V, V, V, V, V, V],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow03 = [
        [W, W, W, W, W, W, W, W],
        [I, I, I, I, I, I, I, I],
        [B2, B2, B2, B2, B2, B2, B2, B2],
        [V, V, V, V, V, V, V, V],
        # Don't use the 4 rows below for UnicornPHAT
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF]
    ]

    rainbow04 = [
        [W, W, W, W, W, W, W, W],
        [I, I, I, I, I, I, I, I],
        [B, B, B, B, B, B, B, B],
        [V2, V2, V2, V2, V2, V2, V2, V2],
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

    Parameter:
        y_color_tuple: a tuple of red, green and blue values for y
            coordinates

    Programs that use this function:
        - Horizontal Striper 1 through 16, but get_y_color is called
          directly by the following functions
            - stripe_horizontally
            - stripe_horizontally_alternate
            - stripe_horizontally_alternate_2
            - stripe_horizontally_reverse
            - stripe_horizontally_reverse_alt
            - stripe_horizontally_rev_alt_2

    """

    return int(y_color_tuple[0]), int(y_color_tuple[1]), \
        int(y_color_tuple[2])


def get_x_color(x_color_tuple):
    """
    Extracts 3 individual integers from a tuple and returns them.

    Parameter:
        x_color_tuple: a tuple of red, green and blue values for x
            coordinates

    Programs that use this function:
        - Vertical Striper 1 through 16, but get_x_color is called
          directly by the following functions.
            - stripe_vertically
            - stripe_vertically_alternate
            - stripe_vertically_alternate_2
            - stripe_vertically_reverse
            - stripe_vertically_reverse_alt
            - stripe_vertically_reverse_alt_2
    """

    return int(x_color_tuple[0]), int(x_color_tuple[1]), \
        int(x_color_tuple[2])


def ripple_diagonally(rainbow00, rainbow_list):
    """
    Cycles through 12 rainbows to make them ripple diagonally

    Parameters:
        rainbow00: a static horizontal rainbow
        rainbow_list: a list containing 11 rainbows that will ripple

    Programs that use this function:
       - Diagonal Ripple 1: passes in rainbow00 and diagonal_rainbows_1
       - Diagonal Ripple 2: passes in rainbow00 and diagonal_rainbows_2
       - Diagonal Ripple 3: passes in rainbow00 and diagonal_rainbows_3
       - Diagonal Ripple 4: passes in rainbow00 and diagonal_rainbows_4
    """

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
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def double_ripple(rainbow00, rainbow_list):
    """
    Cycles through 9 rainbows to ripple them

    Parameters:
        rainbow00: a static horizontal rainbow
        rainbow_list: a list containing 9 rainbows that will ripple

    Programs that use this function:
        - Double Ripple 1: passes in rainbow00 and dr_rainbows_1
        - Double Ripple 2: passes in rainbow00 and dr_rainbows_2
        - Double Ripple 3: passes in rainbow00 and dr_rainbows_3
        - Double Ripple 4: passes in rainbow00 and dr_rainbows_4
    """

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
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def ripple_horizontally(rainbow00, rainbow_list):
    """
    Cycles through 9 rainbows to ripple them horizontally

    Parameters:
        rainbow00: a static horizontal rainbow
        rainbow_list: a list containing 8 rainbows that will ripple

    Programs that use this function:
        - Horizontal Ripple 1: passes in rainbow00 and hr_rainbows_1
        - Horizontal Ripple 2: passes in rainbow00 and hr_rainbows_1
    """

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
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def stripe_horizontally(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Parameters:
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

    Parameters:
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

    Parameters:
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

    Parameters:
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

    Parameters:
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


def stripe_horizontally_rev_alt_2(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it. This function is used with Horizontal Striper 7 and 8.

    Parameters:
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


def move_diagonally(rainbow_list):
    """
    Cycles through 4 rainbows to make them appear to move diagonally

    Parameters:
        rainbow_list: 4 different rainbow images

    Programs that use this function:
        - Moving Diagonal Rainbow 1: passes in md_rainbows_1
        - Moving Diagonal Rainbow 2: passes in md_rainbows_2
        - Moving Diagonal Rainbow 3: passes in md_rainbows_3
        - Moving Diagonal Rainbow 4: passes in md_rainbows_4
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Loop through the rainbows so they appear to move
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.5)


def move_horizontally(rainbow_list):
    """
    Cycles through 4 rainbows to make them appear to move horizontally

    Parameters:
        rainbow_list: a list containing 4 horizontal rainbows that will
        ripple

    Programs that use this function:
        - Moving Horizontal Rainbow 1: passes in mh_rainbows_1
        - Moving Horizontal Rainbow 2: passes in mh_rainbows_2
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Loop through the rainbows so they appear to move
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.5)


def move_vertically(rainbow_list):
    """
    Cycles through 4 rainbows to make them appear to move vertically

    Programs that use this function:
        - Moving Vertical Rainbow 1: passes in mv_rainbows_1
        - Moving Vertical Rainbow 2: passes in mv_rainbows_2
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Loop through the rainbows so they appear to move
        for rainbow in rainbow_list:
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

    Parameters:
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


def ripple_vertically(rainbow00, rainbow_list):
    """
    Cycles through 5 rainbows to ripple them vertically

    Parameters:
        rainbow00: a static horizontal rainbow
        rainbow_list: a list containing 8 rainbows that will ripple

    Programs that use this function:
        - Vertical Ripple 1: passes in rainbow00 and vr_rainbows_1
        - Vertical Ripple 2: passes in rainbow00 and vr_rainbows_2
    """

    start_time = time.time()
    time.clock()
    seconds_elapsed = 0

    while seconds_elapsed < 10:
        # Show main vertical rainbow
        unicornhat.set_pixels(rainbow00)
        unicornhat.show()
        time.sleep(2.0)
        # Loop through the rainbows so they appear to ripple
        for rainbow in rainbow_list:
            seconds_elapsed = time.time() - start_time
            unicornhat.set_pixels(rainbow)
            unicornhat.show()
            time.sleep(0.05)


def stripe_vertically(x_coordinate_list, y_coordinate_list):
    """
    Lights up the LEDs based on the x and y coordinates that were sent
    to it.

    Parameters:
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

    Parameters:
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

    Parameters:
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

    Parameters:
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

    Parameters:
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

    Parameters:
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
