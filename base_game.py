"""
This file intended to become a two-human-player, ASCII art game of
tic-tac-tic-tac-toe.
"""


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
