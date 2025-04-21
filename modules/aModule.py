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
	def update(self, switches, button, wires, keypad, timer):
		"""
		Determines the current inputs on the bomb for later use.
		:param switches:
		:param button:
		:param wires:
		:param keypad:
		:param timer:
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