import pygame

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1+x,y,10,10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK ,[5+x,17+y], [10+x,27+y], 2)
    pygame.draw.line(screen, BLACK, [5+x,17+y], [x,27+y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5+x,17+y], [5+x,7+y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5+x,7+y], [9+x,17+y], 2)
    pygame.draw.line(screen, RED, [5+x,7+y], [1+x,17+y], 2)

pygame.init()

screenSizeW = 700
screenSizeH = 500
screenSize = (screenSizeW, screenSizeH)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption('Noche of Stars')

done = False
clock = pygame.time.Clock()

#hide the mouse cursor
pygame.mouse.set_visible(0) #hides mouse pointer

while not done:
	#all EVENT PROCESSING should go BELOW this comment
	for event in pygame.event.get(): #check the events list
		if event.type == pygame.QUIT: #if user clicks the X
			done = True 
	#all EVENT PROCESSING should go ABOVE this comment
	
	#all GAME LOGIC should go BELOW this comment
	pos = pygame.mouse.get_pos()
	x = pos[0]
	y = pos[1]
	#all GAME LOGIC should go ABOVE this comment	
	
	
	#all code to DRAW should go BELOW this comment

	#first clear the screen to white or your background
	#don't put other drawing commands above background one
	screen.fill(WHITE)
	draw_stick_figure(screen,x,y) #follows mouse pointer
	

	#all code to DRAW should go ABOVE this comment
	
	pygame.display.flip()
	clock.tick(60)


pygame.quit()




