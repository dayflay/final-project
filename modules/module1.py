# Module 1: "The Dead Man's Hand"
# Requires the user to avoid pressing certain buttons
# which will remove time from the counter
from modules.aModule import aModule


class module1(aModule):
	def __init__(self):
		super().__init__()
		self.name = "The Dead Man's Hand"

	def solve(self) -> bool:
		return True

	def update(self, switches, button, wires, keypad, timer):
		pass