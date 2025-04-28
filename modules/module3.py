# Module 3: ""
# Requires the user to hold down the button while completing another part of the bomb
# letting go of the button too early will remove time from the counter
from modules.aModule import aModule
from bomb_phases import Toggles
import random

class module3(aModule):
    def __init__(self, toggles_component, toggles_target):
        super().__init__()
        self.name = 'Mine'
        self.time_pressed = 0
        self.start_time = None

        # Generate a random target based on number of toggles
        self.toggles_target = self.random_target(len(toggles_component))

        # create the toggles puzzle
        self.toggles = Toggles(toggles_component, toggles_target)
        self.toggles.start()

    def random_target(self, length):
        # Ensure the target is not all 0s or all 1s
        while True:
            target = ''.join(random.choice('01') for _ in range(length))
            if '0' in target and '1' in target:  # Must have at least one 0 and one 1
                return target

    def solve(self):
        if self.time_pressed >= 45 and self.toggles._defused:
            return True
        return False

    def update(self, switches, button, wires, keypad, timer, gui):
        if self.start_time is None:
            self.start_time = timer.value

        if button.pressed:
            self.time_pressed += 0.1
        else:
            timer.value -= 0.2

        if self.solve():
            self._defused = True






