from colours import RGB, COLOURS
from adafruit_hid.keycode import Keycode


class StreamKey:
    def __init__(self, key, response, colour = RGB()):
        self.key = key
        self.response = response
        self.colour = colour

    def __repr__(self):
        return f"Key({self.key}, {self.response})"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.key == other

    def __gt__(self, other):
        return self.key > other

    def __ge__(self, other):
        return self.key >= other

    def __lt__(self, other):
        return self.key < other

    def __le__(self, other):
        return self.key_skeytate <= other

    def save(self):
        if type(self.colour) == COLOURS:
            return f"{self.key}", f"[{', '.join(self.response)}]", "RAINBOW"
        else:
            return f"{self.key}", f"[{', '.join(self.response)}]", f"0x{self.colour.red:02x}", f"0x{self.colour.green:02x}", f"0x{self.colour.blue:02x}" # type: ignore

    def light(self, keyboard):
        if type(self.colour) == COLOURS:
            colour = self.colour.get()
        else:
            colour = self.colour.copy()

        keyboard.keys[self.key].set_led(colour.red, colour.green, colour.blue) # type: ignore
