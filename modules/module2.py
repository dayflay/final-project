# Module 2: "Trebek"
# Asks the user randomly generated trivia questions
# Correct answers award points. Depending on difficulty,
# different amount of points are required to win
from tkinter import Label

from modules.aModule import aModule
from random import choice, shuffle


class TriviaQuestion:
	def __init__(self, question, answers, correct_answer):
		self.question = question
		self.answers = answers
		shuffle(self.answers) # thanks, ChatGPT
		self.correct_answer = correct_answer

TRIVIA_QUESTIONS = [
	TriviaQuestion("What is the capital of France?", ["Paris", "London", "Rome", "Berlin"], "Paris"),
	TriviaQuestion("Which element has the chemical symbol 'O'?", ["Oxygen", "Gold", "Osmium", "Hydrogen"], "Oxygen"),
	TriviaQuestion("Who wrote 'Romeo and Juliet'?",
				   ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"], "William Shakespeare"),
	TriviaQuestion("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "Mars"),
	TriviaQuestion("What is the largest ocean on Earth?",
				   ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "Pacific Ocean"),
	TriviaQuestion("In which year did the Titanic sink?", ["1912", "1905", "1898", "1923"], "1912"),
	TriviaQuestion("What is the hardest natural substance on Earth?", ["Diamond", "Quartz", "Graphite", "Topaz"],
				   "Diamond"),
	TriviaQuestion("How many continents are there?", ["7", "5", "6", "8"], "7"),
	TriviaQuestion("What is the square root of 64?", ["8", "6", "7", "9"], "8"),
	TriviaQuestion("Which animal is known as the King of the Jungle?", ["Lion", "Tiger", "Elephant", "Gorilla"],
				   "Lion"),
	TriviaQuestion("What is the longest river in the world?", ["Nile", "Amazon", "Yangtze", "Mississippi"], "Nile"),
	TriviaQuestion("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Michelangelo", "Raphael", "Van Gogh"],
				   "Leonardo da Vinci"),
	TriviaQuestion("What gas do plants absorb from the atmosphere?", ["Carbon dioxide", "Oxygen", "Nitrogen", "Helium"],
				   "Carbon dioxide"),
	TriviaQuestion("Who discovered penicillin?", ["Alexander Fleming", "Marie Curie", "Louis Pasteur", "Isaac Newton"],
				   "Alexander Fleming"),
	TriviaQuestion("Which planet is closest to the sun?", ["Mercury", "Venus", "Earth", "Mars"], "Mercury"),
	TriviaQuestion("What is the capital of Japan?", ["Tokyo", "Beijing", "Seoul", "Bangkok"], "Tokyo"),
	TriviaQuestion("Which instrument has 88 keys?", ["Piano", "Guitar", "Harp", "Violin"], "Piano"),
	TriviaQuestion("What is the main ingredient in guacamole?", ["Avocado", "Tomato", "Onion", "Lime"], "Avocado"),
	TriviaQuestion("What is the freezing point of water in Celsius?", ["0", "32", "-1", "100"], "0"),
	TriviaQuestion("Which language is spoken in Brazil?", ["Portuguese", "Spanish", "French", "English"], "Portuguese"),
	TriviaQuestion("What is the chemical symbol for gold?", ["Au", "Ag", "Gd", "Go"], "Au"),
	TriviaQuestion("Who was the first person to walk on the Moon?",
				   ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn"], "Neil Armstrong"),
	TriviaQuestion("How many legs does a spider have?", ["8", "6", "10", "12"], "8"),
	TriviaQuestion("What is the name of the fairy in Peter Pan?",
				   ["Tinker Bell", "Fairy Godmother", "Pixie Dust", "Wendy"], "Tinker Bell"),
	TriviaQuestion("What is the smallest prime number?", ["2", "1", "3", "5"], "2"),
	TriviaQuestion("What is the tallest mountain in the world?", ["Mount Everest", "K2", "Kangchenjunga", "Denali"],
				   "Mount Everest"),
	TriviaQuestion("What is the capital of Australia?", ["Canberra", "Sydney", "Melbourne", "Perth"], "Canberra"),
	TriviaQuestion("Who is known as the 'Father of Computers'?",
				   ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], "Charles Babbage"),
	TriviaQuestion("How many players are on a soccer team on the field?", ["11", "10", "9", "12"], "11"),
	TriviaQuestion("Which country invented pizza?", ["Italy", "Greece", "France", "Spain"], "Italy"),
	TriviaQuestion("What does 'www' stand for?",
				   ["World Wide Web", "World Web Wide", "Web World Wide", "Web Wide World"], "World Wide Web"),
	TriviaQuestion("Which U.S. state is the Grand Canyon in?", ["Arizona", "Nevada", "Utah", "Colorado"], "Arizona"),
	TriviaQuestion("Which bird is known for mimicking sounds?", ["Parrot", "Sparrow", "Penguin", "Eagle"], "Parrot"),
	TriviaQuestion("Who wrote '1984'?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.K. Rowling"],
				   "George Orwell"),
	TriviaQuestion("Which scientist developed the theory of relativity?",
				   ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"], "Albert Einstein"),
	TriviaQuestion("How many bones are in the adult human body?", ["206", "210", "200", "201"], "206"),
	TriviaQuestion("What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Earth", "Neptune"],
				   "Jupiter"),
	TriviaQuestion("In which country were the Olympic Games invented?", ["Greece", "Italy", "France", "China"],
				   "Greece"),
	TriviaQuestion("Which is the fastest land animal?", ["Cheetah", "Lion", "Horse", "Greyhound"], "Cheetah"),
	TriviaQuestion("What is H2O more commonly known as?", ["Water", "Oxygen", "Hydrogen", "Salt"], "Water"),
	TriviaQuestion("What is the main language spoken in Canada?", ["English", "French", "Both", "Spanish"], "Both"),
	TriviaQuestion("How many colors are in a rainbow?", ["7", "6", "5", "8"], "7"),
	TriviaQuestion("What type of animal is a Komodo dragon?", ["Lizard", "Snake", "Dinosaur", "Crocodile"], "Lizard"),
	TriviaQuestion("What is the name of the longest bone in the human body?", ["Femur", "Tibia", "Humerus", "Fibula"],
				   "Femur"),
	TriviaQuestion("Who is the Greek god of the sea?", ["Poseidon", "Zeus", "Hades", "Apollo"], "Poseidon"),
	TriviaQuestion("What currency is used in Japan?", ["Yen", "Won", "Dollar", "Euro"], "Yen"),
	TriviaQuestion("What is the most spoken language in the world?",
				   ["Mandarin Chinese", "English", "Spanish", "Hindi"], "Mandarin Chinese"),
	TriviaQuestion("Which metal is liquid at room temperature?", ["Mercury", "Gold", "Silver", "Iron"], "Mercury"),
	TriviaQuestion("Which famous ship sank in 1912?", ["Titanic", "Lusitania", "Queen Mary", "Bismarck"], "Titanic"),
]

class module2(aModule):
	def __init__(self):
		super().__init__()
		self.name = "Trebek"
		self.questions = TRIVIA_QUESTIONS
		shuffle(self.questions)

		self.stage = 1
		self.timing = 0
		self.points = 0
		self.booted = False
		self.last_question = None

		self.title_label, self.q1, self.q2, self.q3, self.q4 = Label(), Label(), Label(), Label(), Label()


	def get_current_question(self):
		return self.questions[self.stage]


	def solve(self) -> bool:
		if self.points >= 10:
			self.title_label.destroy()
			self.q1.destroy()
			self.q2.destroy()
			self.q3.destroy()
			self.q4.destroy()
			return True


	def update(self, switches, button, wires, keypad, timer, screen):
		if not self.booted:
			self.booted = True
			screen.hide_all()

		current_question = self.get_current_question()

		if current_question != self.last_question:
			#self.title_label.grid_remove()
			self.title_label = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 12),
									 text=f"({self.points}) {current_question.question}")
			self.title_label.grid_forget()
			self.title_label.grid(row=2, column=1, pady=40)

			self.q1.destroy()
			self.q1 = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 18),
									 text=f"1: {current_question.answers[0]}")
			self.q1.grid_forget()
			self.q1.grid(row=3, column=1, pady=40)

			self.q2.destroy()
			self.q2 = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 18),
							text=f"2: {current_question.answers[1]}")
			self.q2.grid_forget()
			self.q2.grid(row=3, column=2, pady=40)

			self.q3.destroy()
			self.q3 = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 18),
							text=f"3: {current_question.answers[2]}")
			self.q3.grid_forget()
			self.q3.grid(row=4, column=1, pady=40)

			self.q4.destroy()
			self.q4 = Label(screen, bg="black", fg="#00ff00", font=("Courier New", 18),
							text=f"4: {current_question.answers[3]}")
			self.q4.grid_forget()
			self.q4.grid(row=4, column=2, pady=40)

			self.last_question = current_question

		self.timing += 1

		if keypad._value != "":
			self.stage += 1
			answer = int(keypad._value) - 1
			keypad._value = ""

			if current_question.answers[answer] == current_question.correct_answer:
				self.points += 1

#test_mod = module2()
