"""
Module that reverses the combination: the displayed values for toggles and wires are inverted relative to actual inputs.
"""
from modules.aModule import aModule

class module4(aModule):
    def __init__(self):
        super().__init__()
        self.name = "Shenanigans"
        self.solve_progress = 0

    def solve(self) -> bool:
        return self.solve_progress == 4

    # invert function changes the 0's and 1's for me
    def invert(self, bits: str) -> str:
        bits = str(bits)
        return ''.join('1' if b == '0' else '0' for b in bits)

    def update(self, switches, button, wires, keypad, timer, screen):
        """if not screen.booted:
			screen.booted = True
			screen.hide_all()
            screen._ltimer = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 18), text="Time left: ")
            screen._ltimer.grid(row=1, column=2, columnspan=3, sticky=E)
            # the keypad passphrase
            screen._lkeypad = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 18), text="Keypad phase: ")
            screen._lkeypad.grid(row=2, column=2, columnspan=3, sticky=E)
            # the jumper wires status
            screen._lwires = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 18), text="Wires phase: ")
            screen._lwires.grid(row=3, column=2, columnspan=3, sticky=E)
            # the pushbutton status
            screen._lbutton = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 18), text="Button phase: ")
            screen._lbutton.grid(row=4, column=2, columnspan=3, sticky=E)
            # the toggle switches status
            screen._ltoggles = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 18), text="Toggles phase: ")
            screen._ltoggles.grid(row=5, column=2, columnspan=2, sticky=E)
            # the strikes left
            screen._lstrikes = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 18), text="Strikes left: ")
            screen._lstrikes.grid(row=5, column=2, sticky=E)"""

        # Invert expected target for wires
        expected_wires = self.invert(wires._target)
        if wires._value == expected_wires and not wires._defused:
            self.solve_progress += 1
            wires._defused = True

        # Invert expected target for switches
        expected_switches = self.invert(switches._target)
        if switches._value == expected_switches and not switches._defused:
            self.solve_progress += 1
            switches._defused = True

        # Button logic unchanged
        if button._pressed and not button._defused:
            self.solve_progress += 1
            button._defused = True

        # Keypad logic unchanged
        if keypad._value == keypad._target and not keypad._defused:
            self.solve_progress += 1
            keypad._defused = True

