#################################
# CSC 102 Defuse the Bomb Project
# Main program
# Team: 
#################################

# import the configs
from bomb_configs import *
from modules import *
# import the phases
from bomb_phases import *
# randomization library
from random import shuffle

from win import win_screen


###########
# functions
##########
# generates the bootup sequence on the LCD
def bootup(n=0):
    # if we're not animating (or we're at the end of the bootup text)
    if (not ANIMATE or n == len(boot_text)):
        # if we're not animating, render the entire text at once (and don't process \x00)
        if (not ANIMATE):
            gui._lscroll["text"] = boot_text.replace("\x00", "")
        # configure the remaining GUI widgets
        gui.setup()
        # setup the phase threads, execute them, and check their statuses
        if (RPi):
            setup_phases()
            check_phases()
    # if we're animating
    else:
        # add the next character (but don't render \x00 since it specifies a longer pause)
        if (boot_text[n] != "\x00"):
            gui._lscroll["text"] += boot_text[n]

        # scroll the next character after a slight delay (\x00 is a longer delay)
        gui.after(25 if boot_text[n] != "\x00" else 750, bootup, n + 1)

    gui._lscroll.grid_forget()

def select_difficulty(value):
    global difficulty
    difficulty = int(value)

def quit_window(target_window: Tk):
    target_window.destroy()

# sets up the phase threads
def setup_phases():
    global timer, keypad, wires, button, toggles, queue, current_module
    
    # setup the timer thread
    timer = Timer(component_7seg, COUNTDOWN)
    # bind the 7-segment display to the LCD GUI so that it can be paused/unpaused from the GUI
    gui.setTimer(timer)
    # setup the keypad thread
    keypad = Keypad(component_keypad, keypad_target)
    # setup the jumper wires thread
    wires = Wires(component_wires, wires_target)
    # setup the pushbutton thread
    button = ButtonPhase(component_button_state, component_button_RGB, button_target, button_color, timer)
    # bind the pushbutton to the LCD GUI so that its LED can be turned off when we quit
    gui.setButton(button)
    # setup the toggle switches thread
    toggles = Toggles(component_toggles, toggles_target)

    # create a queue for the modules to work upon
    queue = []
    possible_mods = ALL_MODULES
    shuffle(possible_mods)

    for i in range(0, difficulty):
        queue.append(choice([module1(), module2(), module3(), module4(), module5(), module6()]))

    #queue = [module1(), module2(), module3(), module4(), module5(), module6()]

    global current_module
    current_module = 0

    for item in queue:
        print(item.name)

    # start the phase threads
    timer.start()
    keypad.start()
    wires.start()
    button.start()
    toggles.start()


# checks the phase threads
def check_phases():
    global active_phases, current_module, queue
    
    # check the timer
    if (timer._running):
        # update the GUI
        gui._ltimer["text"] = f"Time left: {timer}"
    else:
        # the countdown has expired -> explode!
        # turn off the bomb and render the conclusion GUI
        turn_off()
        gui.after(100, gui.conclusion, False)
        # don't check any more phases
        return

    print(queue[current_module].name)
    queue[current_module].update(toggles, button, wires, keypad, timer, gui)

    if queue[current_module].solve():
        print("MODULE SOLVED!")
        if current_module == (len(queue) - 1): # final module
            pass # YOU WIN!!!
            win_screen()
            turn_off()

        else:
            current_module += 1

    # check the phases again after a slight delay
    gui.after(100, check_phases)

# turns off the bomb
def turn_off():
    # stop all threads
    timer._running = False
    keypad._running = False
    wires._running = False
    button._running = False
    toggles._running = False

    # turn off the 7-segment display
    component_7seg.blink_rate = 0
    component_7seg.fill(0)
    # turn off the pushbutton's LED
    for pin in button._rgb:
        pin.value = True

######
# MAIN
######

# config difficulty
global difficulty

difficulty_selection_window = Tk()
difficulty_selection_window.attributes("-fullscreen", True)

difficulty_selector = Scale(difficulty_selection_window,
                            from_=0, to=10,
                            orient=HORIZONTAL,
                            resolution=1,
                            command=select_difficulty,
                            label="Pick Difficulty")
difficulty_selector.pack(padx=60, pady=20)

continue_button = Button(difficulty_selection_window,
                              text="Play",
                              command=lambda: quit_window(difficulty_selection_window))
continue_button.pack(padx=20, pady=20)

difficulty_selection_window.mainloop()

# initialize the LCD GUI
window = Tk()
gui = Lcd(window)

# initialize the bomb strikes and active phases (i.e., not yet defused)
strikes_left = NUM_STRIKES
active_phases = NUM_PHASES

# "boot" the bomb
gui.after(1000, bootup)

# display the LCD GUI
window.mainloop()
