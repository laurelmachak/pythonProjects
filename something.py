import pygame

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)

pygame.init()

screenSizeW = 900
screenSizeH = 700
screenSize = (screenSizeW, screenSizeH)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption('Something')

done = False
clock = pygame.time.Clock()

background_image = pygame.image.load("galaxy.jpg").convert()
player_image = pygame.image.load("assets/moon_full.png").convert()
player_image.set_colorkey(BLACK) #makes player background transparent


pygame.mouse.set_visible(False)

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
	screen.blit(background_image, [0, 0])

	player_position = pygame.mouse.get_pos()
	x=player_position[0]
	y=player_position[1]
	screen.blit(player_image, [x,y])
	#all code to DRAW should go ABOVE this comment
	
	pygame.display.flip()
	clock.tick(60)


pygame.quit()




