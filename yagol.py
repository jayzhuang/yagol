import pygame, sys, random, os
from board_helpers import *
from propagator import *
from pygame.locals import *

# defs
len_b, gap_b = 8, 1
tot_b = len_b + gap_b*2
width, height = 800, 600
state = 'prep'
fps = 30

board = []
make_board(board, width/tot_b, height/tot_b, tot_b)

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
		board = propagate(board, height, tot_b)
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
				flip_block(board, mousex, mousey, tot_b)
		elif event.type == KEYDOWN:
			if state == 'prep':
				if event.key == K_c:
					clear_board(board)
				elif event.key == K_r:
					rand_board(board)
				elif event.key == K_SPACE:
					state = 'go'
					fps = 10
			elif state == 'go':
				if event.key == K_SPACE:
					state = 'prep'
					fps = 30
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
	pygame.display.update()
	fpsClock.tick(fps)
