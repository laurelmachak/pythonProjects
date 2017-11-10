import pygame
#define constants
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (246, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 106, 0)
VIOLET = (128, 80, 175)
GREEN = (26, 114, 35)
PINK = (229, 91, 227)

pygame.init() #start pygame

#create a display screen: 'size' pixels
size = (400, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('game')

done = False #We're not done displaying
clock = pygame.time.Clock()
rect_x = 50
rect_y = 50
rect_change_y = 1
rect_change_x = 1
rect_h = 50
rect_w = 50

while not done: 
	for event in pygame.event.get( ): #check if the events list
		if event.type == pygame.QUIT: #if the user clicks the X
			done = True #now we're done displaying
	screen.fill(WHITE)	
	screen.fill(VIOLET)

	pygame.draw.rect(screen, PINK, [rect_x, rect_y, rect_w, rect_h], 0)	
	rect_x += rect_change_x
	rect_y += rect_change_y
	if rect_y > 300-rect_h or rect_y < 0:
		rect_change_y = rect_change_y * -1
	if rect_x > 400-rect_w or rect_x < 0:
		rect_change_x = rect_change_x * -1
 

	pygame.display.flip()
	clock.tick(60)


pygame.quit()

