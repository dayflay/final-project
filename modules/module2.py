# Module 2: "Trebek"
# Asks the user randomly generated trivia questions
# Correct answers award points. Depending on difficulty,
# different amount of points are required to win

from modules.aModule import aModule


class module2(aModule):
	def __init__(self):
		super().__init__()
		self.name = "Trebek"

	def solve(self) -> bool:
		return True

	def update(self, switches, button, wires, keypad, timer, screen):
		pass