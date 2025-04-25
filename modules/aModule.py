from abc import ABC, abstractmethod

class aModule(ABC):
	"""
	Abstract class for creating other modules
	"""

	def __init__(self):
		self.name = ""

	def __str__(self):
		return self.name

	@abstractmethod
	def update(self, switches, button, wires, keypad, timer, screen):
		"""
		Determines the current inputs on the bomb for later use.
		:param switches: the state of the switches
		:param button: the state of the button
		:param wires: the state of the wires
		:param keypad: the combo of the keypad
		:param timer: the current time
		:param screen: the screen object
		:return:
		"""

	@abstractmethod
	def solve(self) -> bool:
		"""
		A function to detect whether the module has been solved.
		Returns true if the bomb module has been solved.
		Returns false otherwise.
		:return:
		"""

		return False