"""
Reverses what the combination is but doesn't show what you put it shows the opposite

"""
from modules.aModule import aModule

global solveProgress

class Module4(aModule):
    def __init__(self):
        super().__init__()
        self.name = "Shenanigans"

    def solve(self) -> bool:
        if solveProgress==4:
            return True
        else:
            return False
    def update(self, switches, button, wires, keypad, timer, screen):
        if wires == "01101":
            solveProgress += 1
        else:
            return False
        if switches == "1010":
            solveProgress += 1
        else:
            return False
        if button == button._pressed():
            solveProgress += 1
        else:
            return False
        if keypad == "1234":
            solveProgress += 1
        else:
            return False