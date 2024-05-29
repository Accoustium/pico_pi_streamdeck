import time
import colours
import usb_hid # type: ignore
from rgbkeypad import RgbKeypad
from streamkeys import StreamKey
from adafruit_hid.keyboard import Keyboard # type: ignore
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS # type: ignore
from adafruit_hid.keycode import Keycode # type: ignore


class StreamDeck:
    def __init__(self):
        self.keymap = []
        self.keypad = RgbKeypad()

        self.keyboard = Keyboard(usb_hid.devices)
        self.layout = KeyboardLayoutUS(self.keyboard)

        for key_load in self.load_data():
            self.keymap.append(self.load_key(key_load))

    def load_data(self):
        f = open('data.csv')
        data = f.read()
        for line in data.split('\r\n'):
            yield line
        f.close()

    def load_key(self, data_value):
        key, key_press, *colour= eval(data_value)
        # print(eval(key_press))
        if colour[0] == "RAINBOW":
            colour = colours.COLOURS()
        else:
            colour = colours.RGB(colour[0], colour[1], colour[2])
            print(repr(colour))
        
        streamkey = StreamKey(key, key_press, colour)
        _key = self.keypad.keys[key]
        
        @self.keypad.on_press(_key)
        def press_handler(_key):
            keycode = []
            for press in streamkey.response:
                keycode.append(Keycode.__dict__[press])
            
            print(keycode)
            self.keyboard.send(*keycode)

        return streamkey

    def save_data(self):
        f = open('data.csv', 'w')
        for key_value in range(1, 17):
            f.write(", ".join(self.__dict__[f"K{key_value}"].save()))
            if key_value < 16:
                f.write("\r\n")
        f.close()

    def render(self):
        for key in self.keymap:
            key.light(self.keypad)
    
    def start(self):
        while True:
            self.render()
            self.keypad.update()

