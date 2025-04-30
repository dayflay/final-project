from modules.aModule import aModule
import random

class module3(aModule):
    def __init__(self):
        super().__init__()
        self.name = 'Mine'
        self.time_pressed = 0
        self.start_time = None
        self.toggles = None
        self._defused = False
        self.last_update_time = None  # Will store the last game timer value

        # Generate a random target (not all 0s or all 1s)
        self.toggles_target = self.random_target()

    def random_target(self):
        while True:
            target = ''.join(random.choice('01') for _ in range(4))
            if '0' in target and '1' in target:
                return target

    def solve(self):
        return self.time_pressed >= 45 and self.toggles._value == self.toggles_target

    def update(self, switches, button, wires, keypad, timer, gui):
        self.toggles = switches

        # Initialize timing on first call
        if self.start_time is None:
            self.start_time = timer._value
            self.last_update_time = timer._value

        # Calculate elapsed in-game time since last update
        elapsed = self.last_update_time - timer._value

        # Run logic only once every 0.1 seconds of game time
        if not self._defused and elapsed >= 0.1:
            self.last_update_time = timer._value  # Update reference point

            if button._pressed:
                self.time_pressed += 1
            else:
                timer._value = max(0, timer._value - 2)  # Penalize only once per 0.1s

        # Check if solved
        if self.solve():
            self._defused = True