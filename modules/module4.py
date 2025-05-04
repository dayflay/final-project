"""
Module that reverses the combination: the displayed values for toggles and wires are inverted relative to actual inputs.
"""
from modules.aModule import aModule
import random
from tkinter import Label

class module4(aModule):
    def __init__(self):
        super().__init__()
        self.name = "Shenanigans"
        self.solve_progress = 0
        self.booted = False


    def solve(self) -> bool:
        if self.solve_progress == 4:
            return True
        else:
            return False

    #invert function changes the 0's and 1's for me
    def invert(self, bits: str) -> str:
        bits = str(bits)
        return ''.join('1' if b == '0' else '0' for b in bits)

    #holds what I want to be the targets
    def Ktarget(self):
        combos =["1234", "9876","6489","0456"]
        self.keypad_target = random.choice(combos)
        return self.keypad_target
    def Wtarget(self):
        combos = ["11100", "10010", "10110", "10001", "00100", "11010", "10101", "11111", "01010"]
        self.wires_target = random.choice(combos)
        return self.wires_target
    def Starget(self):
        combos=["1100","0010","0110","1000","0000","1010","0101"]
        self.switches_target = random.choice(combos)
        return self.switches_target

    def update(self, switches, button, wires, keypad, timer, screen):
        #sets up the screen and makes it so it doesn't keep refreshing with the screen refresh rate
        if not self.booted and not self.solve():
            screen.hide_all()
            screen._ltimer.grid(row=1, column=3, columnspan=1, sticky="E")
            screen._lkeypad.grid(row=2, column=3, columnspan=1, sticky="E")
            screen._lwires.grid(row=3, column=3, columnspan=1, sticky="E")
            screen._lbutton.grid(row=4, column=3, columnspan=1, sticky="E")
            screen._ltoggles.grid(row=5, column=3, columnspan=1, sticky="E")
            self._solve = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 16),text="solve progress")
            self._solve.grid(row=1, column=1, columnspan=1, sticky="W")
            global expected_wires
            global expected_switches
            global expected_keypad
            expected_wires = self.Wtarget()
            expected_switches = self.Starget()
            expected_keypad = self.Ktarget()
            self.booted = True

        # Invert expected target for wires
        if wires._value == expected_wires and not wires._defused:
            self.solve_progress += 1
            wires._defused = True

        # Invert expected target for switches
        if switches._value == expected_switches and not switches._defused:
            self.solve_progress += 1
            switches._defused = True

        # Button logic unchanged
        if button._pressed and not button._defused:
            self.solve_progress += 1
            button._defused = True

        # Keypad logic unchanged
        if keypad._value == expected_keypad and not keypad._defused:
            self.solve_progress += 1
            keypad._defused = True

        #shows the inverted value for wires and toggles while displaying all values constantly
        # tells you the wires is defused
        if wires._defused != True:
            screen._lwires.config(text=f"Wires:{self.invert(wires._value)} (target: {expected_wires})")
        else:
            screen._lwires.config(text="Wires: DEFUSED")

        # tells you the switches are defused
        if switches._defused != True:
            screen._ltoggles.config(text=f"Toggles:{self.invert(switches._value)} (target: {expected_switches})")
        else:
            screen._ltoggles.config(text="Toggles: DEFUSED")

        # tells you the keypad is defused
        if keypad._defused != True:
            screen._lkeypad.config(text=f"Keypad:{keypad._value} (target: {expected_keypad})")
        else:
            screen._lkeypad.config(text="Keypad: DEFUSED")

        #tells you the button is defused
        if button._defused != True:
            screen._lbutton.config(text=f"Button:{'Pressed' if button._pressed else 'Not pressed'}")
        else:
            screen._lbutton.config(text="Button: DEFUSED")
        self._solve.config(text=f"Solve Progress: {self.solve_progress}")

        #once my module is completed run these
        if self.solve():
            self.defused = True
            self._solve.grid_forget()
            screen._ltimer.grid_forget()
            screen.hide_all()
            screen.replace_all()