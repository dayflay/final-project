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
        self.prev_timer_value = None
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

        if self.prev_timer_value is None:
            self.prev_timer_value = timer._value
            return  # wait for next frame

        # Time since last update
        frame_elapsed = self.prev_timer_value - timer._value
        self.prev_timer_value = timer._value

        if frame_elapsed <= 0 or self._defused:
            return

        if button._pressed:
            self.time_pressed += frame_elapsed
        else:
            timer._value = max(0, timer._value - (2 * frame_elapsed))  # subtract 2s per sec

        if self.solve():
            self._defused = True

        # Debug (remove later)
        print(f"Timer: {timer._value:.2f}, Held: {self.time_pressed:.2f}, Defused: {self._defused}")