# Macropad-67 Firmware (KMK)

This folder contains the KMK/CircuitPython firmware for the Macropad-67 using a 3x3 keypad on a Seeed Studio XIAO RP2040.

## Files
- `code.py` – main KMK firmware

## Flash Steps
1. Install CircuitPython for **Seeed Studio XIAO RP2040**.
2. Copy the KMK library folder to the device:
   - Place the `kmk/` directory on the CIRCUITPY drive.
3. Copy `code.py` from this folder to the CIRCUITPY drive.
4. Reboot the board.

## Keymap (3x3)
Each key sends Ctrl+Alt+F13..F21 in order.

## Notes
- No LEDs are configured.
- If your wiring or pins differ, update the `pins=[...]` list in `code.py`.
