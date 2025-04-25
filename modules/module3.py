# Module 3: ""
# Requires the user to hold down the button while completing another part of the bomb
# letting go of the button too early will remove time from the counter
from modules.aModule import aModule


class module3(aModule):
    def __init__(self):
        super().__init__()
        self.name = 'Mine'

    def update(self, switches, button, wires, keypad, timer, gui):
        if button.pressed:
            pass

        # if time is a specific time:
        # while button._pressed == True:
        # solve toggles

