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

pygame.mouse.set_visible(0)

x_speed=0
y_speed=0

x_coord=10
y_coord=10

while not done:
	#all EVENT PROCESSING should go BELOW this comment
	for event in pygame.event.get(): #check the events list
		if event.type == pygame.QUIT: #if user clicks the X
			done = True
		#user pressed down on a key
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed = -3 
			elif event.key == pygame.K_RIGHT:
				x_speed = 3
			elif event.key == pygame.K_UP:
				y_speed = -3
			elif event.key == pygame.K_DOWN:
				y_speed = 3
		#user let up on a key
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_speed = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				y_speed = 0
			

	#all EVENT PROCESSING should go ABOVE this comment
	#move the object according to the speed vector
	x_coord += x_speed
	y_coord += y_speed
	if x_coord>690:
		x_coord=690
	elif x_coord<0:
		x_coord=0
	elif y_coord>490:
		y_coord=490
	elif y_coord<0:
		y_coord=0
	#all GAME LOGIC should go BELOW this comment
	
	#all GAME LOGIC should go ABOVE this comment	
	
	
	#all code to DRAW should go BELOW this comment

	#first clear the screen to white or your background
	#don't put other drawing commands above background one
	screen.fill(WHITE)
	draw_stick_figure(screen,x_coord,y_coord) 
	

	#all code to DRAW should go ABOVE this comment
	
	pygame.display.flip()
	clock.tick(60)


pygame.quit()
