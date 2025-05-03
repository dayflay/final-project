# Module 1: "The Dead Man's Hand"
# Requires the user to avoid pressing certain buttons
# which will remove time from the counter
from modules.aModule import aModule


class module1(aModule):
	def __init__(self):
		super().__init__()
		self.name = "The Dead Man's Hand"
		self.points = 0
		self.last_status = None

	def solve(self) -> bool:
		if self.points >= 10: return True
		return False

	def update(self, switches, button, wires, keypad, timer, screen):
		if button._pressed != self.last_status:
			self.last_status = button._pressed
			self.points += 1