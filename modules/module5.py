from abc import ABC, abstractmethod
import random

from modules.aModule import aModule


class module5(aModule):
    def __init__(self):
        super().__init__()
        self.name = "Unlock Manifolds"
        self.yes = 0
        self.booted = False



    def solve(self)-> bool:
        if self.yes == 1:
            return True
        else:
            return False

    # holds what I want to be the targets
    def K_target(self):
        combos = ["1234","9876","6489","0456","0000","1111","3333","2222","4444","5555","6666","7777","8888","9999","99999","4729","9816", "4290","8012","5243","8320", "921000","56382"]
        self.keypad_target = random.choice(combos)
        return self.keypad_target

    def update(self, switches, button, wires, keypad, timer, screen):
        if not self.booted and not self.solve():
            screen._lkeypad.grid(row=2, column=1, columnspan=3, sticky="W")
            global expected_k
            expected_k = self.K_target()
            self.booted =True

        if keypad._defused != True:
            screen._lkeypad.config(text=f"Keypad:{keypad._value} (target: {expected_k})")
        else:
            screen._lkeypad.config(text="Keypad: DEFUSED")

        # Keypad logic unchanged
        if keypad._value == expected_k and not keypad._defused:
            self.yes +=1
            keypad._defused = True
        # tells you the keypad is defused



        # once my module is completed run these
        if self.solve():
            self.defused = True