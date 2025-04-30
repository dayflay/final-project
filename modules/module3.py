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

        # Calculate elapsed time correctly (because timer counts down)
        elapsed_time = self.last_update_time - timer._value  # POSITIVE if time has passed

        if not self._defused and elapsed_time >= 0.1:
            # Update the last checked time
            self.last_update_time = timer._value

            if button._pressed:
                self.time_pressed += 0.1
            else:
                timer._value = max(0, timer._value - 2)

        if self.solve():
            self._defused = True