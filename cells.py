import pygame

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)

pygame.init()

screenSizeW = 400
screenSizeH = 400
screenSize = (screenSizeW, screenSizeH)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption('Noche of Stars')

done = False
clock = pygame.time.Clock()
while not done:
	#all EVENT PROCESSING should go BELOW this comment
	for event in pygame.event.get(): #check the events list
		if event.type == pygame.QUIT: #if user clicks the X
			done = True 
	#all EVENT PROCESSING should go ABOVE this comment
	
	#all GAME LOGIC should go BELOW this comment
	
	#all GAME LOGIC should go ABOVE this comment	
	
	
	#all code to DRAW should go BELOW this comment

	#first clear the screen to white or your background
	#don't put other drawing commands above background one
	screen.fill(WHITE)
	pygame.draw.ellipse(screen, BLACK, [225, 10, 100, 100], 2)
	

	#all code to DRAW should go ABOVE this comment
	
	pygame.display.flip()
	clock.tick(60)


pygame.quit()




