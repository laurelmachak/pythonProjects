import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (204,14,4)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

gameExit = False

# lead will be the number 1 block in snake, up front
lead_x = 300
lead_y = 300
lead_x_change = 0

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10

    lead_x += lead_x_change
    
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])



    # using fill to draw rect can be graphics accelerated :
    # gameDisplay.fill(red, rect=[200,200,50,50])
    
    pygame.display.update()




# unitialize pygame
pygame.quit()
quit()
