import pygame

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)

pygame.init()

screenSizeW = 255
screenSizeH = 255
screenSize = (screenSizeW, screenSizeH)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption('Noche of Stars')

done = False
clock = pygame.time.Clock()

width = 20
height = 20
margin = 5

grid = []
for row in range (10):
	grid.append([])
	for column in range (10):
		grid[row].append(0)
grid[1][5] = 1

def drawSquare (x,y):
	pygame.draw.rect(screen, WHITE, [x, y, width, height], 0)

while not done:
	#all EVENT PROCESSING should go BELOW this comment
	for event in pygame.event.get(): #check the events list
		if event.type == pygame.QUIT: #if user clicks the X
			done = True 
		elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
			pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
			column = pos[0] // (width + margin)
			row = pos[1] // (height + margin)
            # Set that location to one
			grid[row][column] = 1
			print("Click ", pos, "Grid coordinates: ", row, column)
	#all EVENT PROCESSING should go ABOVE this comment
	
	#all GAME LOGIC should go BELOW this comment
	
	#all GAME LOGIC should go ABOVE this comment	
	
	
	#all code to DRAW should go BELOW this comment

	#first clear the screen to white or your background
	#don't put other drawing commands above background one
	screen.fill(BLACK)
	for row in range (10):
		for column in range (10):
			drawSquare((width+margin)*column+margin,(height+margin)*row+margin)
		
		
	

	#all code to DRAW should go ABOVE this comment
	
	pygame.display.flip()
	clock.tick(60)


pygame.quit()




