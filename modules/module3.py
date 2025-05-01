# Module 3: ""
# Requires the user to hold down the button while completing another part of the bomb
# letting go of the button too early will remove time from the counter
from modules.aModule import aModule
import random
from math import floor
from tkinter import Label


class module3(aModule):
    def __init__(self):
        super().__init__()
        self.name = 'Mine'
        self.time_pressed = 0
        self.start_time = None
        self.toggles = None
        self.ticks = 0
        self.booted = False

        # Generate a random target
        self.toggles_target = self.random_target()

    def random_target(self):
        # Ensure the target is not all 0s or all 1s
        while True:
            target = ''.join(random.choice('01') for _ in range(4))
            if '0' in target and '1' in target:  # Must have at least one 0 and one 1
                return target

    def solve(self):
        if self.time_pressed >= 20 and (self.toggles._value == self.toggles_target):
            return True
        return False

    def update(self, switches, button, wires, keypad, timer, screen):
        if self.start_time is None:
            self.start_time = timer._value


        self.toggles = switches

        if button._pressed:
            self.time_pressed += 10

        if floor(self.ticks) == 1:
            self.ticks = 0
            if not button._pressed:
                timer._value -= 2
        else:
            self.ticks += 0.1

        if self.solve():
            self._defused = True


        if not self.booted:
            self.booted = True
            screen.hide_all()

            self.title_Label = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 18),
                                     text="land mine")
            self.title_Label.grid(row=2, column=1, pady=10)

            self.description = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 16),
                                     text="hold the button and dont let go!")
            self.description.grid(row=3, column=1, pady=10)

            self.game_desc = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 16),
                                   text="solve the toggles without blowing up the landmine")
            self.game_desc.grid(row=4, column=1, pady=10)

            self.target_hint = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 14),
                                     text=f"{self.toggles_target}")
            self.target_hint.grid(row=5, column=1, pady=10)

            self.time_held = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 14),
                                   text=f"{self.time_pressed}")
            self.time_held.grid(row=6, column=1, pady=10)


