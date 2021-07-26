import math
import random

class Player:
	def __init__(self, side):
		# side is 'x' or 'o'
		pass

	# we want all players to get their next move given in a game
	def get_move(self, game):
		pass

class RandomComputerPlayer(Player):
	def __init__(self, side):
		super().__init__(side)


	def get_move(self, game):
		# Get a random valid spot for our next move
		square = random.choice(game.available_moves())
		return square

class HumanPlayer(Player):
	def __init__(self, side):
		super().__init__(side)


	def get_move(self, game):
		valid_square = False
		val = None
		while not valid_square:
			square = input(self.letter + '\'s turn. Input move (0-9)')
			

			# were going to check if this is a correct value by trying to cast it to an integer, and if it is not we say its invalid 
			# also if the spot is not available we say it is invalid

			try:
				val = int(square)
				if val not in game.available_moves():
					raise ValueError
				valid_square = True  #if these are successful then good if not, we have to go further
			except ValueError:
				print('Invalid square. try again')

		return val
