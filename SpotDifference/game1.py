import pygame
from pygame.locals import*
from time import sleep
from random import randrange

pygame.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height), FULLSCREEN)

difference = pygame.image.load('/home/devil/Desktop/SpotDifference/squidwardSpotDifference.jpg')
difference = pygame.transform.scale(difference, (width, height))

scary = pygame.image.load('/home/devil/Desktop/SpotDifference/hilaryScary.jpg')
scary = pygame.transform.scale(scary, (width, height))

scream = pygame.mixer.Sound('/home/devil/Desktop/SpotDifference/scream.wav')

screen.blit(difference, (0, 0))
pygame.display.update()
sleep(randrange(3,7))
scream.play()
screen.blit(scary, (0, 0))
pygame.display.update()
sleep(3)
scream.stop()
pygame.quit()
