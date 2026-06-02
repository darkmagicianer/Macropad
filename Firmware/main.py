import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.digitalio import DigitalioPinScanner
from kmk.modules.macros import Macros, Tap, Press, Release

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)
macro_copy = KC.M(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL))
macro_paste = KC.M(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL))
macro_run = KC.M(Press(KC.W), Press(KC.space))
macro_stop_run = KC.M(Release(KC.W), Release(KC.space))
direct_pins = (
    board.D5,  
    board.D6,  
    board.D7,  
    board.D8,  
    board.D9,  
    board.D4,  
)
keyboard.matrix = DigitalioPinScanner(
    pins=direct_pins,
    value_when_pressed=False, 
)

keyboard.keymap = [
    [
        macro_copy, macro_paste,  
        macro_run, macro_stop_run,
        KC.N5, KC.N6,  
    ]
]

if __name__ == '__main__':
    keyboard.go()