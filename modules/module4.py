"""
Reverses what the combination is but doesn't show what you put it shows the opposite

"""
from modules.aModule import aModule
from time import sleep

global solveProgress
class module4(aModule):
    def __init__(self):
        super().__init__()
        self.name = "Shenanigans"

    def solve(self) -> bool:
        if solveProgress==4:
            return True
        else:
            return False

    def nfuncwires(self,wires):
        wires._running = True
        while wires._running:
            # Read the state of each pin (HIGH or LOW) and build a binary string
            wires._value = ""
            for pin in wires._component:
                if pin.value:  # True means HIGH
                    wires._value += "0"
                else:
                    wires._value += "1"
                # Check if it matches the target
            if wires_value == wires._target:
                wires._defused = True
                wires._running = False  # stop the loop if defused
            sleep(0.1)  # delay to avoid constant polling

    def update(self, switches, button, wires, keypad, timer, screen):
        if wires == "01101":
            solveProgress += 1
            wires = "DEFUSED"

        if switches == "1010":
            solveProgress += 1
            switches = "DEFUSED"

        if button == button._pressed():
            solveProgress += 1
            button = "DEFUSED"

        if keypad == "1234":
            solveProgress += 1
            keypad = "DEFUSED"