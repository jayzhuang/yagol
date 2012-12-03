import random

def flip(c):
	return {'w':'b', 'b':'w'}[c]

def make_board(b, x, y, tot_b):
	for i in range(x):
		for j in range(y):
			b.append((i*tot_b, j*tot_b, 'w'))

def clear_board(b):
	for i in range(len(b)):
		x, y, ignored = b[i]
		b[i] = (x, y, 'w')

def rand_board(b):
	for i in range(len(b)):
		if random.randint(1, 10) == 1:
			x, y, ignored = b[i]
			b[i] = (x, y, 'b')

def get_index(b, x, y, t):
	for i in range(len(b)):
		bx, by, ignored = b[i]
		if x in range(bx, bx+t+1) and y in range(by, by+t+1):
			return i

def flip_block(b, x, y, tot_b):
	i = get_index(b, x, y, tot_b)
	clr = flip(b[i][2])
	bx, by, ignored = b[i]
	b[i] = (bx, by, clr)
