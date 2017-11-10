import pygame

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (246, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 106, 0)
VIOLET = (128, 80, 175)
GREEN = (26, 114, 35)
PINK = (229, 91, 227)
color1 = (255, 0, 255)
pygame.init()
size = [500, 500]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

while not done: 
	for event in pygame.event.get( ):
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill(color1)
	pygame.draw.rect(screen, BLACK, [0, 50, 50, 50], 0)
	
	pygame.draw.circle(screen, BLUE, [60, 250], 100)
	clock.tick(60)
	pygame.display.flip()
pygame.quit()
