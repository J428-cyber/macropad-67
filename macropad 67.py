import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros,Press,Release,Tap

#67

k=KMKKeyboard()
m=Macros()
k.modules.append(m)

k.matrix=KeysScanner(
pins=[board.D10,board.D11,board.D12,board.D13,board.D14,board.D15,board.D18,board.D16,board.D17],
value_when_pressed=False,
)

k.keymap=[[
KC.MACRO(Press(KC.LCTL),Press(KC.LALT),Tap(KC.F13),Release(KC.LALT),Release(KC.LCTL)),
KC.MACRO(Press(KC.LCTL),Press(KC.LALT),Tap(KC.F14),Release(KC.LALT),Release(KC.LCTL)),
KC.MACRO(Press(KC.LCTL),Press(KC.LALT),Tap(KC.F15),Release(KC.LALT),Release(KC.LCTL)),
KC.MACRO(Press(KC.LCTL),Press(KC.LALT),Tap(KC.F16),Release(KC.LALT),Release(KC.LCTL)),
KC.MACRO(Press(KC.LCTL),Press(KC.LALT),Tap(KC.F17),Release(KC.LALT),Release(KC.LCTL)),
KC.MACRO(Press(KC.LCTL),Press(KC.LALT),Tap(KC.F18),Release(KC.LALT),Release(KC.LCTL)),
KC.MACRO(Press(KC.LCTL),Press(KC.LALT),Tap(KC.F19),Release(KC.LALT),Release(KC.LCTL)),
KC.MACRO(Press(KC.LCTL),Press(KC.LALT),Tap(KC.F20),Release(KC.LALT),Release(KC.LCTL)),
KC.MACRO(Press(KC.LCTL),Press(KC.LALT),Tap(KC.F21),Release(KC.LALT),Release(KC.LCTL))
]]
