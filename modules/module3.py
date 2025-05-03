# Module 3: "land mine"
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
        # creates a collection of letters that are assigned to 1
        one_letters = ['A', 'C', 'F', 'G', 'I', 'L', 'M', 'O']
        # creates a collection of letters that are assigned to 0
        zero_letters = ['B', 'D', 'E', 'H', 'J', 'K', 'N', 'P']

        # gets random string of 0s and 1s
        # Ensure the target is not all 0s or all 1s
        while True:
            target = ''.join(random.choice('01') for _ in range(4))
            if '0' in target and '1' in target:  # Must have at least one 0 and one 1
                #assigns each 0 and 1 to a random letter from the key in order to give a hint
                self.letter_hint = ''.join(
                    random.choice(one_letters) if bit == '1' else random.choice(zero_letters)
                    for bit in target
                )
                return target

    def solve(self):
        if self.time_pressed >= 40 and (self.toggles._value == self.toggles_target):
            return True
        return False

    def update(self, switches, button, wires, keypad, timer, screen):
        if self.start_time is None:
            self.start_time = timer._value

        self.toggles = switches

        if button._pressed:
            self.time_pressed += 0.25

        #reduces the timer faster if the button isnt held
        if floor(self.ticks) == 1:
            self.ticks = 0
            if not button._pressed:
                timer._value -= 2
        else:
            self.ticks += 0.1

        #set custom gui for module
        if not self.booted and not self.solve():
            self.booted = True
            screen.hide_all()
            #these values are in an if statement because they don't need to be refreshed.
            # constant refreshing causes the screen to flicker
            self.title = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 20),
                                     text="land mine")
            self.title.grid(row=2, column=1, pady=10)

            self.description = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 16),
                                     text="hold the button and dont let go!")
            self.description.grid(row=3, column=1, pady=10)

            self.game_desc = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 16),
                                   text="solve the toggles without blowing up the landmine")
            self.game_desc.grid(row=4, column=1, pady=10)

            self.target_hint = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 14),
                                     text=f"Target code: {self.letter_hint}")
            self.target_hint.grid(row=5, column=1, pady=10)

        #these values are outside the if statement as they need to be refreshed to constantly update the time.
        self.time_held = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 14),
                                   text=f"time held: {self.time_pressed}")
        self.time_held.grid(row=6, column=1, pady=10)


        #resets the gui to the regular bomb gui once the module is solved
        if self.solve():
            screen.hide_all()
            screen.replace_all()
            self.time_held.destroy()
            self.game_desc.grid_remove()
            self.description.grid_remove()
            self.title.grid_remove()
            self.target_hint.grid_remove()