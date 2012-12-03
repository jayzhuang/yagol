import pygame, sys
from board_helper import *
from propagator import *
from saver import *
from pygame.locals import *

len_b, gap_b = 8, 1
tot_b = len_b + gap_b*2
width, height = 1200, 700
state = 'prep'
fps = 30
GREY = pygame.Color(150, 150, 150)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

board = []
make_board(board, width, height, tot_b)

pygame.init()
fpsClock = pygame.time.Clock()

windowsSurfaceObj = pygame.display.set_mode((width, height))
pygame.display.set_caption('Yet another game of life')

mousex, mousey = 0, 0

while True:
	windowsSurfaceObj.fill(GREY)
	if state == 'go':
		board = propagate(board, width, height, tot_b)
	for col in board:
		for cell in col:
			x, y, c = cell
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
				elif event.key == K_n:
					board = propagate(board, width, height, tot_b)
				elif event.key == K_s:
					save_board(board, "SAVEDATA")
				elif event.key == K_l:
					load_board(board, "SAVEDATA")
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
