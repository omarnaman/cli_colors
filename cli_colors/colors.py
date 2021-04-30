# Color Modifiers
MOD_4BIT = '\033['
MOD_8BIT = '\033[38;5;'
MOD_RGB = '\033[38;2;'

# 4-Bit Colors
BLACK = MOD_4BIT + '30'
RED = MOD_4BIT + '31'
GREEN = MOD_4BIT + '32'
YELLOW = MOD_4BIT + '33'
BLUE = MOD_4BIT + '34'
MAGENTA = MOD_4BIT + '35'
CYAN = MOD_4BIT + '36'
WHITE = MOD_4BIT + '37'

BRIGHT_BLACK = MOD_4BIT + '90'
BRIGHT_RED = MOD_4BIT + '91'
BRIGHT_GREEN = MOD_4BIT + '92'
BRIGHT_YELLOW = MOD_4BIT + '93'
BRIGHT_BLUE = MOD_4BIT + '94'
BRIGHT_MAGENTA = MOD_4BIT + '95'
BRIGHT_CYAN = MOD_4BIT + '96'
BRIGHT_WHITE = MOD_4BIT + '97'

# 8-Bit Colors
RED_SHADE1 = MOD_8BIT + '88'
RED_SHADE2 = MOD_8BIT + '160'

GREEN_SHADE1 = MOD_8BIT + '22'
GREEN_SHADE2 = MOD_8BIT + '28'

YELLOW_SHADE1 = MOD_8BIT + '142'
YELLOW_SHADE2 = MOD_8BIT + '226'

ORANGE_SHADE1 = MOD_8BIT + '166'
ORANGE_SHADE2 = MOD_8BIT + '208'

BLUE_SHADE1 = MOD_8BIT + '20'
BLUE_SHADE2 = MOD_8BIT + '27'

MAGENTA_SHADE1 = MOD_8BIT + '53'
MAGENTA_SHADE2 = MOD_8BIT + '90'

CYAN_SHADE1 = MOD_8BIT + '39'
CYAN_SHADE2 = MOD_8BIT + '51'

PINK = MOD_8BIT + '201'


RESET = '\033[0m'


# Modifiers
MOD_BOLD = "1"
MOD_FAINT = "2"
MOD_ITALIC = "3"
MOD_UNDERLINE = "4"
MOD_SLOW_BLINK = "5"
MOD_RAPID_BLINK = "6"
MOD_CROSS_OUT = "9"




def color_print(text, color, *modifiers):
    """
    Prints `text` with the color `color` and a list of modifiers 
    `color` can be either a 4-bit, 8-bit or RGB color
    
    4-bit colors can be directly accessed from the library alongside a selection of 8-bit colors.
    Custom 8 bit colors can be passed to the function as a string `MOD_8BIT + "<8bit-color code>"`.
    If color is passed as a tuple with THREE items, it is interpreted as RGB; otherwise it is handled as an escaped color sequence.

    A list of modifiers can be passed to the function further modify the appearance of the text.
    NOTE: This function does not add new lines to the printed text.

    """
    if type(color) is str:
        if len(modifiers) > 0:
            color += ";"
        print(f"{color}{';'.join(modifiers)}m{text}{RESET}", end="")

    elif type(color) is tuple:
        if len(color) != 3:
            raise "RGB color sent does not have 3 values"
        
        color = ['38', '2'] + list(map(str, color))
        color = f"{';'.join(color)}"
        if len(modifiers) > 0:
            color += ";"
        print(f"\033[{color}{';'.join(modifiers)}m{text}{RESET}", end="")