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

def drawStickFigure(screen, x, y):
	#parts to make stick figure
	pygame.draw.circle(screen, ORANGE, [x, y], 10)#head
	pygame.draw.line(screen, RED, [x, y+10], [x,y+50], 6)#shirt
	pygame.draw.line(screen, ORANGE, [x, y+10], [x-20,y+30], 2)#left arm
	pygame.draw.line(screen, ORANGE, [x,y+10], [x+20,y+30], 2)#right arm
	pygame.draw.line(screen, ORANGE, [x,y+50], [x-20,y+70], 2)#left leg
	pygame.draw.line(screen, ORANGE, [x,y+50], [x+20,y+70], 2)#right leg
	

pygame.init()

size = [500, 500]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

while not done: 
	for event in pygame.event.get( ):
		if event.type == pygame.QUIT:
			done = True
	screen.fill(BLUE)
	
	drawStickFigure(screen, 34, 23)
	
	clock.tick(60)
	pygame.display.flip()
pygame.quit()
