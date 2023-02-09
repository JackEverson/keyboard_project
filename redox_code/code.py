print("Starting") #print statment is for debugging

#importing circuit python "board" ability to use GPIO pins.
import board

#General KMK keyboard import 
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

#Redox has 7 columns on left and 7 columns on right (total 14, left to right) and 5 rows, as it is COL2ROW diodes the 1N4148 diodes attach to the rows with the black side of the diode attached to the row (not the switch)
keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,         board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13)
#Columns left to right      1         2         3         4         5         6         7   |split|         8         9        10         11        12          13         14                 

keyboard.row_pins = (board.GP14,board.GP15,board.GP16,board.GP17,board.GP18)
#Rows top to bottom         1           2           3         4          5

keyboard.diode_orientation = DiodeOrientation.COL2ROW

from kmk.modules.layers import Layers
keyboard.modules.append(Layers())

#easier to see function, empty, and transpartent keys
XXXXX = KC.NO
_____ = KC.TRNS
tog_num =  KC.TT(2)
tog_move = KC.TT(1)

keyboard.keymap = [
    [#layer 0: Base layer
    KC.ESC,  KC.N1,      KC.N2,      KC.N3,      KC.N4,        KC.N5,      KC.GRAVE,                        KC.PGUP,    KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINUS,

    KC.TAB,    KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.EQL,                         KC.PGDN,    KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.LBRC,

    KC.CAPS,   KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.RBRC,                          KC.END,     KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOTE,

    KC.LSHIFT, KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.BSLS,                         KC.HOME,    KC.N,       KC.M,       KC.COMMA,   KC.DOT,     KC.SLSH,    KC.RSHIFT,

    KC.LCTRL,  KC.LGUI,      XXXXX,   KC.LALT,      XXXXX,      KC.ENTER,   KC.SPACE,                       KC.BSPC,    tog_move, KC.DEL,   KC.RALT,    tog_num,     KC.RGUI,     KC.RCTRL,
    ],

    [#Layer 1: Motions
    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    KC.LEFT,      KC.DOWN,      KC.UP,     KC.RGHT,      _____,       _____,

    _____,    _____,      KC.DEL,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    ],

    [#layer 2: Numbers and functions layer
    KC.ESC,  KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,       KC.F6,                          KC.F7,    KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12,      KC.MINUS,

    KC.TAB,    _____,      _____,      _____,        KC.LPRN,       KC.RPRN,       _____,                        _____,       _____,       KC.P7,      KC.P8,      KC.P9,       KC.PPLS,       _____,

    KC.CAPS,   _____,      _____,      _____,       KC.LCBR,       KC.RCBR,       _____,                          _____,       _____,       KC.P4,      KC.P5,      KC.P6,       KC.PPLS,    _____,

    KC.LSHIFT, _____,      _____,      _____,        KC.LABK,       KC.RABK,       _____,                          _____,       _____,       KC.P1,      KC.P2,      KC.P3,     KC.PENT,    _____,

    _____,       _____,    _____,      _____,       _____,       _____,           _____,                       _____,       _____,   _____,   KC.P0,    KC.PDOT,    KC.PENT,      _____,
    ],

    [#Layer X: template
    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    ],

    ]



 
if __name__ == '__main__':
    keyboard.go()
