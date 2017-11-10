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
pygame.display.set_caption('Keyboard Fun!')

done = False #We're not done displaying
clock = pygame.time.Clock()
xSpeed = 0
ySpeed = 0
xCoordinate = 10
yCoordinate = 10
while not done: 
	for event in pygame.event.get( ): #check if the events list
		if event.type == pygame.QUIT: #if the user clicks the X
			done = True #now we're done displaying
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				xSpeed = -3
			elif event.key == pygame.K_RIGHT:
				xSpeed = 3
			elif event.key == pygame.K_UP:
				ySpeed = -3
			elif event.key == pygame.K_DOWN:
				ySpeed = 3
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event. key == pygame.K_RIGHT:
				xSpeed = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				ySpeed = 0
	xCoordinate += xSpeed
	yCoordinate += ySpeed
	if xCoordinate > 350:
		xCoordinate = 350
	elif xCoordinate < 0:
		xCoordinate = 0
	elif yCoordinate > 250:
		yCoordinate = 250
	elif yCoordinate < 0:
		yCoordinate = 0
	screen.fill(VIOLET)

	pygame.draw.rect(screen, PINK, [xCoordinate, yCoordinate, 50, 50], 0)
	
	pygame.display.flip()
	clock.tick(60)


pygame.quit()

