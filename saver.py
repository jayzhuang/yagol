from board_helper import *

def index_to_int(i, j):
	return i * 1000 + j

def int_to_index(n):
	return n / 1000, n % 1000

def save_board(b, filename):
	f = open(filename, 'w')
	for i in range(len(b)):
		for j in range(len(b[0])):
			if b[i][j][2] == 'b':
				f.write(str(index_to_int(i, j)) + " ")
	f.close()

def load_board(b, filename):
	clear_board(b)
	f = open(filename, 'r')
	data = f.read().split()
	for s in data:
		i, j = int_to_index(int(s))
		x, y, c = b[i][j]
		b[i][j] = (x, y, 'b')