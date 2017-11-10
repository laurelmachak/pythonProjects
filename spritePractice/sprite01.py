import pygame
import random

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)

class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

pygame.init()

screenSizeW = 700
screenSizeH = 400
screenSize = (screenSizeW, screenSizeH)
screen = pygame.display.set_mode(screenSize)

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
for i in range(50):
	block = Block(BLACK, 20, 15)
	block.rect.x = random.randrange(screenSizeW)
	block.rect.y = random.randrange(screenSizeH)
	block_list.add(block)
	all_sprites_list.add(block)

player = Block(RED, 20, 15)
all_sprites_list.add(player)

pygame.display.set_caption('Sprites')

done = False
clock = pygame.time.Clock()
score = 0
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
	
	pos = pygame.mouse.get_pos()
	player.rect.x = pos[0]
	player.rect.y = pos[1]
	
	blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
	
	for block in blocks_hit_list:
		score += 1
		print(score)
		
	all_sprites_list.draw(screen)
	

	#all code to DRAW should go ABOVE this comment
	
	pygame.display.flip()
	clock.tick(60)


pygame.quit()




