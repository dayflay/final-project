# Module 3: ""
# Requires the user to hold down the button while completing another part of the bomb
# letting go of the button too early will remove time from the counter
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
        self.last_update_time = None

        # Generate a random target
        self.toggles_target = self.random_target()
        

    def random_target(self):
        # Ensure the target is not all 0s or all 1s
        while True:
            target = ''.join(random.choice('01') for _ in range(4))
            if '0' in target and '1' in target:  # Must have at least one 0 and one 1
                return target

    def solve(self):
        if self.time_pressed >= 45 and (self.toggles._value == self.toggles_target):
            return True
        return False

    def update(self, switches, button, wires, keypad, timer, gui):
        if self.start_time is None:
            self.start_time = timer._value
            self.last_update_time = timer._value
 #           screen.hide_all()
  #      # Visual feedback for button hold duration
   #     gui.draw_text(10, 10, f"Time Held: {self.time_pressed}")

    #    # Visual feedback for toggle status
     #   gui.draw_text(10, 30, f"Toggles: {self.toggles._value}")
      #  gui.draw_text(10, 50, f"Target:  {self.toggles_target}")

        self.toggles = switches

        if not self._defused:
            elapsed = self.last_update_time - timer._value
            if elapsed >= 0.1:
                self.last_update_time = timer._value

            if button._pressed:
                self.time_pressed += 1
            else:
                timer._value = max(0, timer._value - 2)

        if self.solve():
            self._defused = True






