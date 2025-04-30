from modules.aModule import aModule
import random

class module3(aModule):
    def __init__(self):
        super().__init__()
        self.name = 'Mine'
        self.time_pressed = 0.0
        self.start_time = None
        self.toggles = None
        self._defused = False
        self.last_update_time = None
        self.toggles_target = self.random_target()

    def random_target(self):
        while True:
            target = ''.join(random.choice('01') for _ in range(4))
            if '0' in target and '1' in target:
                return target

    def solve(self):
        return self.time_pressed >= 4.5 and self.toggles._value == self.toggles_target

    def update(self, switches, button, wires, keypad, timer, gui):
        self.toggles = switches

        if self.start_time is None:
            self.start_time = timer._value
            self.last_update_time = timer._value

        # Calculate how much time has passed since the last update
        time_passed = self.last_update_time - timer._value  # > 0 if time moved forward

        # Only update logic every 0.1 seconds
        if time_passed >= 0.1:
            self.last_update_time = timer._value  # move forward in time

            if not self._defused:
                if button._pressed:
                    self.time_pressed += 0.1
                else:
                    timer._value = max(0, timer._value - 2)

                if self.solve():
                    self._defused = True