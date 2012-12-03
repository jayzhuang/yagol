import random

def flip(c):
	return {'w':'b', 'b':'w'}[c]

def make_board(b, w, h, tot_b):
	for i in range(w/tot_b):
		col = []
		for j in range(h/tot_b):
			col.append((i*tot_b, j*tot_b, 'w'))
		b.append(col)

def clear_board(b):
	for i in range(len(b)):
		for j in range(len(b[0])):
			x, y, ignored = b[i][j]
			b[i][j] = (x, y, 'w')

def rand_board(b):
	for i in range(len(b)):
		for j in range(len(b[0])):
			if random.randint(1, 10) == 1:
				x, y, ignored = b[i][j]
				b[i][j] = (x, y, 'b')

def get_index(x, y, t):
	return x/t, y/t

def flip_block(b, x, y, tot_b):
	i, j = get_index(x, y, tot_b)
	bx, by, clr = b[i][j]
	b[i][j] = (bx, by, flip(clr))
