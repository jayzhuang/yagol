nrow, ncol = 1, 1

def is_black(b, i, j):
	global nrow, ncol #arrr... just to make the parameter list shorter...
	if b[(i+ncol)%ncol][(j+nrow)%nrow][2] == 'b':
		return 1
	return 0

def nneighbors(b, i, j):
	return is_black(b, i-1, j) + is_black(b, i+1, j)\
			 + is_black(b, i, j+1)\
			 + is_black(b, i-1, j+1) + is_black(b, i+1, j+1)\
			 + is_black(b, i, j-1)\
			 + is_black(b, i-1, j-1) + is_black(b, i+1, j-1)

def propagate(b, w, h, tot_b):
	global nrow, ncol #arrr...
	nrow, ncol = h/tot_b, w/tot_b
	next = []
	for i in range(len(b)):
		next_col = []
		for j in range(len(b[0])):
			x, y, c = b[i][j]
			n = nneighbors(b, i, j)
			if c == 'b':
				if n < 2 or n > 3:
					c = 'w'
			else:
				if n == 3:
					c = 'b'
			next_col.append((x, y, c))
		next.append(next_col)
	return next
