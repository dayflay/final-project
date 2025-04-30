"""
Reverses what the combination is but doesn't show what you put it shows the opposite

"""
from modules.aModule import aModule
from time import sleep

class module4(aModule):
    def __init__(self):
        super().__init__()
        self.name = "Shenanigans"
        self.solve_progress = 0

    def solve(self) -> bool:
        return self.solve_progress==4

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
            if wires._value == wires._target:
                wires._defused = True
                wires._running = False  # stop the loop if defused
            sleep(0.1)  # delay to avoid constant polling

    def update(self, switches, button, wires, keypad, timer, screen):
        if wires._value == "01101" and not wires._defused:
            self.solve_progress += 1
            wires._defused = True

        if switches._value == "1010" and not switches._defused:
            self.solve_progress += 1
            switches._defused = True

        if button._pressed and not button._defused:
            self.solve_progress += 1
            button._defused = True

        if keypad._value == "1234" and not keypad._defused:
            self.solve_progress += 1
            keypad._defused = True