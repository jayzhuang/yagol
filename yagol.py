import pygame, sys
from pygame.locals import *

# defs
len_b, gap_b = 18, 1
tot_b = len_b + gap_b*2
width, height = 800, 600
state = 'prep'
fps = 30

# helpers
def flip(c):
	return {'w':'b', 'b':'w'}[c]

def make_board(b, x, y, len, gap):
	for i in range(x):
		for j in range(y):
			b.append((i*tot_b, j*tot_b, 'w'))

def clear_board(b):
	cb = []
	for i in b:
		x, y, ignored = i
		cb.append((x, y, 'w'))
	return cb

def get_index(b, x, y, t):
	for i in b:
		bx, by, ignored = i
		if x in range(bx, bx+t+1) and y in range(by, by+t+1):
			return b.index(i)

def flip_block(b, x, y):
	i = get_index(b, x, y, tot_b)
	clr = flip(b[i][2])
	bx, by, ignored = b[i]
	b[i] = (bx, by, clr)

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

def propagate(b):
	next = []
	nrow = height / tot_b
	i = 0
	for block in b:
		x, y, c = block
		n = nneighbors(b, nrow, i)
		if n > 0:
			print i, block, n
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

board = []
make_board(board, width/tot_b, height/tot_b, len_b, gap_b)

# pygame starts
pygame.init()
fpsClock = pygame.time.Clock()

windowsSurfaceObj = pygame.display.set_mode((width, height))
pygame.display.set_caption('Yet another game of life')

GREY = pygame.Color(150, 150, 150)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
mousex, mousey = 0, 0

fontObj = pygame.font.Font('freesansbold.ttf', 32)

while True:
	windowsSurfaceObj.fill(GREY)
	if state == 'go':
		board = propagate(board)
	for i in board:
		x, y, c = i
		clr = {'w':WHITE, 'b':BLACK}[c]
		pygame.draw.rect(windowsSurfaceObj, clr, (x, y, len_b, len_b))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONUP:
			mousex, mousey = event.pos
			if(state == 'prep'):
				flip_block(board, mousex, mousey)
		elif event.type == KEYDOWN:
			if event.key == K_c:
				if state == 'prep':
					board = clear_board(board)
			if event.key == K_s:
				if state == 'prep':
					state = 'go'
					fps = 5
				else:
					state = 'prep'
					fps = 30
				print state
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
	pygame.display.update()
	fpsClock.tick(fps)
