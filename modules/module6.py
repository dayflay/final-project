# Module 6: "binary addition"
# complete binary addition with the 2 strings generated


from modules.aModule import aModule
import random
from tkinter import Label


class module6(aModule):
    def __init__(self):
        super().__init__()
        self.name = 'binary addition'
        self.toggles = None
        self.booted = False


    def random_string_1(self):
        self._a = random.randint(0, 15)
        return format(self._a, "04b")

    def random_string_2(self):
        max_b = 15 - self._a  # Ensure a + b < 16
        self._b = random.randint(0, max_b)
        return format(self._b, "04b")

    def toggle_solution(self):
        result = self._a + self._b
        return format(result, "04b")

    def solve(self):
        if self.toggles._value == self.toggle_solution:
            return True
        return False

    def update(self, switches, button, wires, keypad, timer, screen):
        self.toggles = switches

        if not self.booted and not self.solve():
            self.booted = True
            screen.hide_all()
            #these values are in an if statement because they don't need to be refreshed.
            # constant refreshing causes the screen to flicker
            self.game_name = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 20),
                                     text="Binary Addition")
            self.game_name.grid(row=2, column=1, pady=5)

            self.desc = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 16),
                                     text="solve the binary addition to get the answer to the toggles")
            self.desc.grid(row=3, column=1)

            self.str1 = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 16),
                                   text=f"string 1: {self.random_string_1()}")
            self.str1.grid(row=4, column=1)

            self.str2 = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 16),
                                   text=f"string 2: {self.random_string_2()}")
            self.str2.grid(row=5, column=1)


        # resets the gui to the regular bomb gui once the module is solved
        if self.solve():
            screen.hide_all()
            screen.replace_all()
            self.game_name.grid_remove()
            self.desc.grid_remove()
            self.str1.grid_remove()
            self.str2.grid_remove()