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
        self.penalized = False  # Flag to track if penalty is applied after button release

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

        # Track the change in timer between updates
        time_diff = self.prev_timer_value - timer._value
        self.prev_timer_value = timer._value

        # Ensure we only process updates if time has passed
        if time_diff <= 0 or self._defused:
            return

        # Start penalizing immediately after the module is activated
        if not self.started:
            self.started = True  # The module has started, begin penalty once button is released.

        if button._pressed:
            # Track time held while button is pressed
            self.time_pressed += time_diff
            self.penalized = False  # Reset penalty flag as the button is still held
        else:
            # Apply penalty once the button is released, if not already penalized
            if not self.penalized:
                penalty_time = 2 * time_diff  # Subtract 2 seconds per second
                timer._value = max(0, timer._value - penalty_time)
                self.penalized = True  # Set flag to prevent multiple penalties

        # Check if the module is solved
        if self.solve():
            self._defused = True

        # Debug (remove this once it works)
        print(f"Timer: {timer._value:.2f}, Held: {self.time_pressed:.2f}, Defused: {self._defused}")