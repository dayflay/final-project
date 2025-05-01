"""
Module that reverses the combination: the displayed values for toggles and wires are inverted relative to actual inputs.
"""
from modules.aModule import aModule
from bomb_phases import *
from bomb_configs import *




class Lcd(Frame):
    def __init__(self, window):
        super().__init__(window, bg="black")
        # make the GUI fullscreen
        window.attributes("-fullscreen", True)
        # we need to know about the timer (7-segment display) to be able to pause/unpause it
        self._timer = None
        # we need to know about the pushbutton to turn off its LED when the program exits
        self._button = None
        # setup the initial "boot" GUI
        self.setupBoot()

    # sets up the LCD "boot" GUI
    def setupBoot(self):
        # set column weights
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        # the scrolling informative "boot" text
        self._lscroll = Label(self, bg="black", fg="white", font=("Courier New", 14), text="", justify=RIGHT)
        self._lscroll.grid(row=0, column=0, columnspan=3, sticky=E)
        self.pack(fill=BOTH, expand=True)

    # sets up the LCD GUI
    def setup(self):
        # Ensure all columns are configured to expand
        for i in range(6):
            self.columnconfigure(i, weight=1)

        # the timer
        self._ltimer = Label(self, bg="black", fg="#00ff00", font=("Courier New", 18), text="Time left: ", anchor=E,
                             justify=RIGHT)
        self._ltimer.grid(row=1, column=3, columnspan=3, sticky=E)

        # the keypad passphrase
        self._lkeypad = Label(self, bg="black", fg="#00ff00", font=("Courier New", 18), text="Keypad phase: ", anchor=E,
                              justify=RIGHT)
        self._lkeypad.grid(row=2, column=3, columnspan=3, sticky=E)

        # the jumper wires status
        self._lwires = Label(self, bg="black", fg="#00ff00", font=("Courier New", 18), text="Wires phase: ", anchor=E,
                             justify=RIGHT)
        self._lwires.grid(row=3, column=3, columnspan=3, sticky=E)

        # the pushbutton status
        self._lbutton = Label(self, bg="black", fg="#00ff00", font=("Courier New", 18), text="Button phase: ", anchor=E,
                              justify=RIGHT)
        self._lbutton.grid(row=4, column=3, columnspan=3, sticky=E)

        # the toggle switches status
        self._ltoggles = Label(self, bg="black", fg="#00ff00", font=("Courier New", 18), text="Toggles phase: ",
                               anchor=E, justify=RIGHT)
        self._ltoggles.grid(row=5, column=2, columnspan=2, sticky=E)

        # the strikes left
        self._lstrikes = Label(self, bg="black", fg="#00ff00", font=("Courier New", 18), text="Strikes left: ",
                               anchor=E, justify=RIGHT)
        self._lstrikes.grid(row=5, column=3, sticky=E)

        if (SHOW_BUTTONS):
            # the pause button (right-aligned text, right side of window)
            self._bpause = tkinter.Button(self, bg="red", fg="white", font=("Courier New", 18), text="Pause", anchor=E,
                                          width=10, command=self.pause)
            self._bpause.grid(row=6, column=4, pady=40, sticky=E)

            # the quit button (right-aligned text, right side of window)
            self._bquit = tkinter.Button(self, bg="red", fg="white", font=("Courier New", 18), text="Quit", anchor=E,
                                         width=10, command=self.quit)
            self._bquit.grid(row=6, column=5, pady=40, sticky=E)


class module4(aModule):
    def __init__(self):
        super().__init__()
        self.name = "Shenanigans"
        self.solve_progress = 0

    def solve(self) -> bool:
        return self.solve_progress == 4

    # invert function changes the 0's and 1's for me
    def invert(self, bits: str) -> str:
        bits = str(bits)
        return ''.join('1' if b == '0' else '0' for b in bits)

    def update(self, switches, button, wires, keypad, timer, screen):
        # Invert expected target for wires
        expected_wires = self.invert(wires._target)
        if wires._value == expected_wires and not wires._defused:
            self.solve_progress += 1
            wires._defused = True

        # Invert expected target for switches
        expected_switches = self.invert(switches._target)
        if switches._value == expected_switches and not switches._defused:
            self.solve_progress += 1
            switches._defused = True

        # Button logic unchanged
        if button._pressed and not button._defused:
            self.solve_progress += 1
            button._defused = True

        # Keypad logic unchanged
        if keypad._value == keypad._target and not keypad._defused:
            self.solve_progress += 1
            keypad._defused = True

        #if self.solve():
