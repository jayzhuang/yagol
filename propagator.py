
def is_black(b, i):
	if i >= 0 and i < len(b) and b[i][2] == 'b':
		return 1
	return 0

def nneighbors(b, nrow, i):
	ret = is_black(b, i+nrow) + is_black(b, i-nrow)
	if i % nrow != 0:
		ret += is_black(b, i-1) + is_black(b, i+nrow-1) \
				 + is_black(b, i-nrow-1)
	if (i+1) % nrow != 0:
		ret += is_black(b, i+1) + is_black(b, i+nrow+1) \
				 + is_black(b, i-nrow+1)
	return ret

def propagate(b, height, tot_b):
	next = []
	nrow = height / tot_b
	i = 0
	for block in b:
		x, y, c = block
		n = nneighbors(b, nrow, i)
		# rules
		if c == 'b':
			if n < 2 or n > 3:
				c = 'w'
		else:
			if n == 3:
				c = 'b'
		next.append((x, y, c))
		i += 1
	return next