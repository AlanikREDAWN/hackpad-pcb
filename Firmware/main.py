import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap, Delay

macros = Macros()


# class LayerTracker(RGB):
#     def on_layer_change(self, layer):
#         if layer == 0:
#             display.entries = [
#                 ImageEntry(image="catswhite.bmp", x=0, y=0),
#                 TextEntry(text="Layer 0", x=64, y=32, x_anchor="B", y_anchor="M")
#             ]
#             keyboard.extensions.append(display)
#         elif layer == 1:
#             display.entries = [
#                 ImageEntry(image="catswhite.bmp", x=0, y=0),
#                 TextEntry(text="Layer 1", x=64, y=32, x_anchor="B", y_anchor="M")
#             ]
#             keyboard.extensions.append(display)
#         elif layer == 2:
#             display.entries = [
#                 ImageEntry(image="catswhite.bmp", x=0, y=0),
#                 TextEntry(text="Layer 2", x=64, y=32, x_anchor="B", y_anchor="M")
#             ]
#             keyboard.extensions.append(display)
#         elif layer == 4:
#             display.entries = [
#                 ImageEntry(image="catswhite.bmp", x=0, y=0),
#                 TextEntry(text="Layer 1", x=64, y=32, x_anchor="B", y_anchor="M")
#             ]
#             keyboard.extensions.append(display)            # white

COL0 = board.D10
COL1 = board.D9
COL2 = board.D8
COL3 = board.D7
COL4 = board.D6

ROW0 = board.D3
ROW1 = board.D2
ROW2 = board.D1
ROW3 = board.D0

print("Starting")
keyboard = KMKKeyboard()
layers = Layers()

col_pins = (COL0, COL1, COL2, COL3, COL4)
row_pins = (ROW0, ROW1, ROW2, ROW3)
diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(layers)
keyboard.modules.append(macros)

# Layers
TOGGLE = KC.TG(1)

CONTROL_S_MACRO = KC.MACRO(
    Press(KC.RCTRL),
    Press(KC.S),
    Delay(500),
    Release(KC.RCTRL),
    Release(KC.S),
)

ALT_S = KC.RALT(KC.S)

ALT_T = KC.RALT(KC.T)

ALT_F = KC.RALT(KC.F)

ALT_V = KC.RCALT(KC.V)

ALT_M = KC.RCALT(KC.M)



keyboard.keymap = [
    # Base Layer
    [

    ],

    # Function Layer
    [

    ],
]

i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    display=driver,
    entries=[
        ImageEntry(image="catswhite.bmp", x=0, y=0),
    ]
    width=128, # screen size
    height=32, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=0.8, # initial screen brightness level
    brightness_step=0.1, # used for brightness increase/decrease keycodes
    dim_time=20, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=60, # time in seconds to turn off screen
    powersave_dim_time=10, # time in seconds to reduce screen brightness
    powersave_dim_target=0.1, # set level for brightness decrease
    powersave_off_time=30, # time in seconds to turn off screen
)

keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()


# print("Starting")

# import board

# from kmk.kmk_keyboard import KMKKeyboard
# from kmk.keys import KC
# from kmk.scanners import DiodeOrientation

# keyboard = KMKKeyboard()

# keyboard.col_pins = (board.GP0,)
# keyboard.row_pins = (board.GP1,)
# keyboard.diode_orientation = DiodeOrientation.COL2ROW

# keyboard.keymap = [
#     [KC.A,]
# ]

# if __name__ == '__main__':
#     keyboard.go()