import pygame
from math import pi

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)

pygame.init()

size = (600,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Noche of Stars') 

done = False
clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get(): #check the events list
		if event.type == pygame.QUIT: #if user clicks the X
			done = True 
	screen.fill(WHITE)
	screen.fill((47, 43, 89))
	pygame.draw.rect(screen,(WHITE),[100,200,50,70],0)
	pygame.display.update()


pygame.quit()



