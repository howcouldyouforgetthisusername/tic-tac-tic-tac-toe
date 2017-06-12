"""
This file intended to become a two-human-player, ASCII art game of
tic-tac-tic-tac-toe.
"""

class SmallBoard:
	"""
	A class representing a 3x3 grid of cells that can either be filled with an
	'X', an 'O', or be empty.
	"""
	def __init__(self):
		# Initially, each board is empty.
		self.board = [['', '', ''], ['', '', ''], ['', '', '']]

	def is_occupied(row, col):
		"""
		Returns True if the given cell is occupied, False otherwise.
		"""
		return

class BigBoard:
	"""
	A class representing a 3x3 grid of cells that can either be filled with an
	'X', an 'O', or a SmallBoard.
	"""

	def __init__(self):
		# TODO: Make SmallBoard's.



if __name__ == "__main__":
	while not done:
		move = input("Enter your move: ")
		if is_valid_move(move):
			board.update(move)
		else:
			print("Invalid move!")
			continue
		print(board)
	print(board.endMessage)
