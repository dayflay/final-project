# Module 1: "The Dead Man's Hand"
# Requires the user to spam the buttons
from modules.aModule import aModule
from tkinter import Label


class module1(aModule):
	def __init__(self):
		super().__init__()
		self.name = "The Dead Man's Hand"
		self.points = 0
		self.last_points = -1
		self.last_status = None
		self.title_label = None

	def solve(self) -> bool:
		if self.points >= 10:
			#self.title_label.grid_remove()
			return True
		return False

	def update(self, switches, button, wires, keypad, timer, screen):
		if self.last_status == None:
			screen.hide_all()

		#self.title_label = Label(screen, text=f"Points: {self.points}", font=("Courier New", 18), bg="black", fg="white")

		# if (self.points != self.last_points) and (self.points < 10):
		# 	self.title_label.grid_forget()
		# 	self.title_label.grid(column=1, row=1)

		if button._pressed != self.last_status:
			self.last_status = button._pressed
			self.points += 1