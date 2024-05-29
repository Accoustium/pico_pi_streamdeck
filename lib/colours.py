#  This creates RGB Class used to hold values to send to the Pimoroni Keypad LEDs.
#  All values are integers, but when sent to the REPR or converted to a string,
#  they are displayed as Hex.


class RGB:
    def __init__(self, red = 0xff, green = 0xff, blue = 0xff):
        self.red = red
        self.green = green
        self.blue = blue
        self.loc = 0
    
    def __repr__(self):
        return f"RBG({hex(self.red)}, {hex(self.green)}, {hex(self.blue)})"
    
    def __str__(self):
        return self.__repr__()

    def __iter__(self):
        return self

    def __next__(self):
        if self.loc > 2:
            raise StopIteration
        else:
            self.loc = self.loc + 1
            if self.loc == 1:
                return self.red
            elif self.loc == 2:
                return self.green
            elif self.loc == 3:
                return self.blue
    
    def copy(self):
        return RGB(self.red, self.green, self.blue)


#  This creates a Class that simplifies the creation of a Rainbow color.
#  There is a list of colors cycling through a standard selection of the
#  rainbow.  When using the Rainbow color, it will increment to color
#  automatically before sending the current RGB Class back to the user.


class COLOURS:
    colour = [
        RGB(128, 0, 0),
        RGB(128, 16, 0),
        RGB(128, 32, 0),
        RGB(128, 48, 0),
        RGB(128, 64, 0),
        RGB(128, 80, 0),
        RGB(128, 96, 0),
        RGB(128, 112, 0),
        RGB(128, 128, 0),
        RGB(112, 128, 0),
        RGB(96, 128, 0),
        RGB(80, 128, 0),
        RGB(64, 128, 0),
        RGB(48, 128, 0),
        RGB(32, 128, 0),
        RGB(16, 128, 0),
        RGB(0, 128, 0),
        RGB(0, 128, 16),
        RGB(0, 128, 32),
        RGB(0, 128, 48),
        RGB(0, 128, 64),
        RGB(0, 128, 80),
        RGB(0, 128, 96),
        RGB(0, 128, 112),
        RGB(0, 128, 128),
        RGB(0, 112, 128),
        RGB(0, 96, 128),
        RGB(0, 80, 128),
        RGB(0, 64, 128),
        RGB(0, 48, 128),
        RGB(0, 32, 128),
        RGB(0, 16, 128),
        RGB(0, 0, 128),
        RGB(16, 0, 128),
        RGB(32, 0, 128),
        RGB(48, 0, 128),
        RGB(64, 0, 128),
        RGB(80, 0, 128),
        RGB(96, 0, 128),
        RGB(112, 0, 128),
        RGB(128, 0, 128),
        RGB(128, 0, 112),
        RGB(128, 0, 96),
        RGB(128, 0, 80),
        RGB(128, 0, 64),
        RGB(128, 0, 48),
        RGB(128, 0, 32),
        RGB(128, 0, 16)
    ]

    def __init__(self, starting_colour = 0):
        self.colour_pos = starting_colour
        self.current_colour = self.get_colour(self.colour_pos)


    def __add__(self, add):
        self.colour_pos = self.colour_pos + 1
        if self.colour_pos >= len(self.colour):
            self.colour_pos = self.colour_pos % len(self.colour)
        
        return self

    def get(self):
        self = self + 1
        return self.get_colour(self.colour_pos)

    @classmethod
    def get_colour(self, idx):
        return self.colour[idx]


#  These are standard RGB color combinations.


RED = COLOURS.get_colour(0)
ORANGE = COLOURS.get_colour(4)
YELLOW = COLOURS.get_colour(8)
DRK_GREEN = COLOURS.get_colour(12)
GREEN = COLOURS.get_colour(16)
TEAL = COLOURS.get_colour(20)
LT_BLUE = COLOURS.get_colour(24)
CYAN = COLOURS.get_colour(28)
BLUE = COLOURS.get_colour(32)
PURPLE = COLOURS.get_colour(36)
PINK = COLOURS.get_colour(40)
RAINBOW = COLOURS()
