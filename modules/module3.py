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
        self.started = False  # Flag to ensure penalty starts immediately

    def random_target(self):
        while True:
            target = ''.join(random.choice('01') for _ in range(4))
            if '0' in target and '1' in target:
                return target

    def solve(self):
        # Solve condition: time held is at least 45 seconds, and toggles match the target.
        return self.time_pressed >= 45 and self.toggles._value == self.toggles_target

    def update(self, switches, button, wires, keypad, timer, gui):
        self.toggles = switches

        # Initialize prev_timer_value if not set
        if self.prev_timer_value is None:
            self.prev_timer_value = timer._value
            return  # Wait for the next frame to proceed

        # Calculate frame time (how much time has passed since the last update)
        frame_elapsed = self.prev_timer_value - timer._value
        self.prev_timer_value = timer._value

        # Don't process if no time has passed (frame_elapsed <= 0) or the module is defused
        if frame_elapsed <= 0 or self._defused:
            return

        # Start penalizing immediately after the module is activated
        if not self.started:
            self.started = True  # Flag to indicate the module has started

        # If button is pressed, accumulate time held
        if button._pressed:
            self.time_pressed += frame_elapsed
        else:
            # If the button is released, start penalizing
            penalty_time = 2 * frame_elapsed  # Penalty is 2 seconds per second
            timer._value = max(0, timer._value - penalty_time)

        # Check if the module is solved
        if self.solve():
            self._defused = True

        # Debug (remove this once it works)
        print(f"Timer: {timer._value:.2f}, Held: {self.time_pressed:.2f}, Defused: {self._defused}")