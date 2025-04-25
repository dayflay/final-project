# Module 1: "The Dead Man's Hand"
# Requires the user to avoid pressing certain buttons
# which will remove time from the counter
from modules.aModule import aModule


class module1(aModule):
	def __init__(self):
		super().__init__()
		self.name = "The Dead Man's Hand"
		self.points = 0

	def solve(self) -> bool:
		if self.points >= 10: return True
		return False

	def update(self, switches, button, wires, keypad, timer):
		if switches == "0101":
			self.points += 1

		self.solve()