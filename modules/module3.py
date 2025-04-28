# Module 3: ""
# Requires the user to hold down the button while completing another part of the bomb
# letting go of the button too early will remove time from the counter
from modules.aModule import aModule


class module3(aModule):
    def __init__(self):
        super().__init__()
        self.name = 'Mine'
        self.time_pressed = 0
        self.start_time = None

    def solve(self):
        if self.time_pressed == 45:
            return True
        return False

    def update(self, switches, button, wires, keypad, timer, gui):
        if self.start_time is None:
            self.start_time = timer.value
        if button.pressed:
            self.time_pressed += 0.1
        else:
            timer.value -= 0.2

        if self.time_pressed >= :
            pass

        # if time is a specific time:
        # while button._pressed == True:
        # solve toggles

