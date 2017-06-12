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
		self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

	def is_occupied(self, row, col):
		"""
		Returns True if the given cell is occupied, False otherwise.
		"""
		return self.board[row][col] != ' '

	def set_cell(self, row, col, val):
		"""
		Sets the cell indicated by row, col to be val.
		"""
		# TODO: Add exception handling.
		self.board[row][col] = val

	def full(self):
		"""
		Returns True if the board is full, False otherwise.
		"""
		for 

	def find_winner(self):
		"""
		Searches for a winner. Returns either "X", "O", "Cat's Game", or "Not Filled"
		"""
		if not self.full():
			return "Not Filled"

	def __str__(self):
		"""
		ASCII art version of the board.
		"""
		return \
			self.board[0][0] + '|' + self.board[0][1] + '|' + self.board[0][2] + '\n' + \
			'-----\n' + \
			self.board[1][0] + '|' + self.board[1][1] + '|' + self.board[1][2] + '\n' + \
			'-----\n' + \
			self.board[2][0] + '|' + self.board[2][1] + '|' + self.board[2][2] + '\n'



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
