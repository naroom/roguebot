import random
import math

D_WAIT = (0, 0)
D_UP_LEFT = (-1, -1)
D_UP = (0, -1)
D_UP_RIGHT = (1, -1)
D_LEFT = (-1, 0)
D_RIGHT = (1, 0)
D_DOWN_LEFT = (-1, 1)
D_DOWN = (0, -1)
D_DOWN_RIGHT = (1, 1)

directions = [
D_WAIT,
D_UP_LEFT,
D_UP,
D_UP_RIGHT,
D_LEFT,
D_RIGHT,
D_DOWN_LEFT,
D_DOWN,
D_DOWN_RIGHT
]

map_str = """
################
#.%............#
#..............#
#######..#######
#..............#
#.@............#
################
"""
map_str = map_str[1:] # strip initial newline
map_width = map_str.find('\n')


def get_pos(char):
	lin_pos = map_str.find(char)
	x = int(lin_pos % map_width)
	y = int(math.floor(lin_pos / map_width))
	return (x, y)

# get player and exit pos
player_pos = get_pos('@')
exit_pos = get_pos('%')

#initialize
moves_made = 0  # penalty function

class Node():
	def __init__(self, n_inputs):
		self.weights = [1.0] * n_inputs

	def compute(self, inputs):
		return tanh(sum(i*w for i, w in zip(inputs, weights)))

	def update_weights(self, nope):
		pass


def get_next_move():
	pass


def make_move():
	moves_made += 1
	if player_pos == exit_pos:
		pass		
		#update_weights()


def main():
	# track moves made before winning on prev iterations
	n_iterations = 100
	results = []

	print "player at", player_pos
	print "exit at", exit_pos

	for i in range(n_iterations):
		pass


if __name__ == '__main__':
	main()
