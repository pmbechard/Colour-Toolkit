from random import randint
from tkinter import Tk, Label, colorchooser
import re

"""
The Colour Toolkit is a Python library designed to make working with HEX and RGB colours more convenient.
"""


def get_hex():
    """Produce a randomly generated HEX value"""
    hex = list(f'#{randint(100000, 999999)}')
    for i in range(1, 7):
        change_or_not = randint(0, 1)
        if change_or_not:
            letter = chr(randint(0, 5) + 97)
            hex[i] = letter
    return ''.join(hex)


def get_hex_list(length=5):
    """ Produce a list of randomly generated HEX values of a length determined by the user (default 5)"""
    hex_list = []
    for i in range(length):
        hex_list += [get_hex()]
    return hex_list


def hex_colour_picker():
    colour = colorchooser.askcolor(initialcolor='#ffffff')
    return colour[1]


def get_rgb():
    """Produce a randomly generated RGB value"""
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def get_rgb_list(length=5):
    """ Produce a list of randomly generated RGB values of a length determined by the user (default 5)"""
    rgb_list = []
    for i in range(length):
        rgb_list += [get_rgb()]
    return rgb_list


def rgb_colour_picker():
    colour = colorchooser.askcolor(initialcolor='#ffffff')
    return colour[0]


def hex_to_rgb(colour_value):
    colour_value = colour_value.lstrip('#')
    return tuple(int(colour_value[i:i + len(colour_value) // 3], 16) for i in range(0, len(colour_value),
                                                                                    len(colour_value) // 3))


def rgb_to_hex(colour_value):
    return '#%02x%02x%02x' % colour_value


def test_colour(colour_value):
    """ Creates a pop-up window for the user to see the colour value """
    format_type = check_format(colour_value)

    if format_type == 'hex':
        pass
    elif format_type == 'rgb':
        colour_value = f'#{colour_value[0]:02x}{colour_value[1]:02x}{colour_value[2]:02x}'
    else:
        return "Invalid args: please choose one format."

    root = Tk()
    root.title('Colour Sample')
    root.geometry('320x240+200+200')
    Label(root, text='', background=colour_value).pack(fill='both', expand=True)
    root.mainloop()


def check_format(colour_value):
    """ Ensure that the color value matches one of the valid formats """
    e = Exception("Invalid format.")
    regex = "^#[0-9a-f]{6}"
    try:
        if isinstance(colour_value, str):
            if re.match(regex, colour_value):
                return "hex"
        elif isinstance(colour_value, tuple) and len(colour_value) == 3:
            for i in range(3):
                if not 0 <= colour_value[i] <= 255:
                    return None
            return "rgb"
    except:
        return None


def get_help():
    print("\nThanks for using The Colour Toolkit by Peyton Bechard.\n"

          "\nHere is a list of the methods available in this toolkit with a short explanation for each:\n"

          "\n\t> get_hex() returns a randomly generated hexadecimal value for a colour as a string (e.g. '#b43c81')\n"

          "\n\t> get_hex_list(length=5) returns a list of randomly generated hexadecimal values for colours. "
          "\n\tThe length of the list is at 5 by default but this can be changed by passing an integer of the desired "
          "length as an arg\n"

          "\n\t> hex_colour_picker() allows you to choose a colour visually using a system colour chooser GUI and"
          "returns a hex value"

          "\n\t> get_rgb() returns a randomly generated RGB value for a colour as a tuple (e.g. (232, 197, 2) )\n"

          "\n\t> get_rgb_list(length=5) returns a list of randomly generated RGB tuples for colours. \n\tThe length of "
          "the list is at 5 by default but this can be changed by passing an integer of the desired length as an arg\n"

          "\n\t> rgb_colour_picker() allows you to choose a colour visually using a system colour chooser GUI and"
          "returns a rgb value"

          "\n\t> test_colour(colour_value) accepts a colour value (hex or RGB format) and creates a pop-up window using"
          "tkinter to display the colour.\n"

          "\n\t> check_format(colour_value) accepts a colour value and returns either 'hex' or 'rgb' depending on the "
          "format of the provided colour value. \n\tIf the colour value does not match either format, a value of None "
          "is returned. NOTE: hex values are prefixed with a # in this toolkit.\n"

          "\n\t> get_help() does exactly what you see here!\n"

          "\nThanks again for using The Colour Toolkit by Peyton Bechard.\n"

          "Feel free to check out and/or contribute to this and other projects at: https://github.com/pmbechard")
