# test example module

from modules.aModule import aModule


class module0(aModule):
	def __init__(self):
		super().__init__()
		self.name = "Example Module"
		self.solved = False
		self.active_phases = 4
		self.strikes_left = 5

	def solve(self) -> bool:
		if self.activePhases > 0: return False
		return True

	def update(self, switches, button, wires, keypad, timer, gui):
		toggles = switches
		# check the keypad
		if (keypad._running):
			# update the GUI
			gui._lkeypad["text"] = f"Combination: {keypad._value}"
		# the phase is defused -> stop the thread
		# if (keypad._defused):
		#     keypad._running = False
		#     active_phases -= 1
		# # the phase has failed -> strike
		# elif (keypad._failed):
		#     strike()
		#     # reset the keypad
		#     keypad._failed = False
		#     keypad._value = ""
		# check the wires
		if (wires._running):
			# update the GUI
			gui._lwires["text"] = f"Wires: {wires}"
			# the phase is defused -> stop the thread
			if (wires._defused):
				wires._running = False
				self.active_phases -= 1
			# the phase has failed -> strike
			elif (wires._failed):
				self.strike()
				# reset the wires
				wires._failed = False
		# check the button
		if (button._running):
			# update the GUI
			gui._lbutton["text"] = f"Button: {button}"
			# the phase is defused -> stop the thread
			if (button._defused):
				button._running = False
				self.active_phases -= 1
			# the phase has failed -> strike
			elif (button._failed):
				self.strike()
				# reset the button
				button._failed = False
		# check the toggles
		if (toggles._running):
			# update the GUI
			gui._ltoggles["text"] = f"Toggles: {toggles}"
			# the phase is defused -> stop the thread
			if (toggles._defused):
				toggles._running = False
				self.active_phases -= 1
			# the phase has failed -> strike
			elif (toggles._failed):
				self.strike()
				# reset the toggles
				toggles._failed = False

		# note the strikes on the GUI
		gui._lstrikes["text"] = f"Strikes left: {self.strikes_left}"
		# too many strikes -> explode!
		if (self.strikes_left == 0):
			# turn off the bomb and render the conclusion GUI
			#turn_off()
			gui.after(1000, gui.conclusion, False)
			# stop checking phases
			return

		# # the bomb has been successfully defused!
		# if (active_phases == 0):
		# 	# turn off the bomb and render the conclusion GUI
		# 	turn_off()
		# 	gui.after(100, gui.conclusion, True)
		# 	# stop checking phases
		# 	return

		self.solve()

	def strike(self):
		self.strikes_left -= 1