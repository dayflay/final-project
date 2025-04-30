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
        self.started = False  # True once the module is active and ready to penalize

    def random_target(self):
        while True:
            target = ''.join(random.choice('01') for _ in range(4))
            if '0' in target and '1' in target:
                return target

    def solve(self):
        # Game is solved when time pressed >= 45 and toggles match the target
        return self.time_pressed >= 45 and self.toggles._value == self.toggles_target

    def update(self, switches, button, wires, keypad, timer, gui):
        self.toggles = switches

        # Wait for the module to be activated before starting the timer.
        if self.prev_timer_value is None:
            self.prev_timer_value = timer._value
            return

        # Calculate the time elapsed since the last update (frame time)
        frame_elapsed = self.prev_timer_value - timer._value
        self.prev_timer_value = timer._value

        # Ignore frames where time hasn't passed
        if frame_elapsed <= 0 or self._defused:
            return

        # Module is active and ready to penalize once it starts.
        if not self.started:
            self.started = True  # The module has started, begin penalty.

        # Track time held while the button is pressed
        if button._pressed:
            self.time_pressed += frame_elapsed
        else:
            # Subtract 2 seconds for each second the button is released
            penalty_time = 2 * frame_elapsed  # 2 seconds per second
            timer._value = max(0, timer._value - penalty_time)

        # Check if the module is solved
        if self.solve():
            self._defused = True

        # Debug (you can remove this once it's working)
        print(f"Timer: {timer._value:.2f}, Held: {self.time_pressed:.2f}, Defused: {self._defused}")