from modules.aModule import aModule
import random
import time

class module3(aModule):
    def __init__(self):
        super().__init__()
        self.name = 'Mine'
        self.time_pressed = 0
        self.start_time = None
        self.toggles = None
        self._defused = False
        self.last_update_time = time.time()  # Real-world timer

        # Generate a random target
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

        current_time = time.time()
        elapsed = current_time - self.last_update_time

        # Only execute logic every 0.1 seconds
        if not self._defused and elapsed >= 0.1:
            self.last_update_time = current_time  # Reset clock

            if button._pressed:
                self.time_pressed += 1
            else:
                timer._value = max(0, timer._value - 2)  # Subtract only once per 0.1s

        if self.solve():
            self._defused = True