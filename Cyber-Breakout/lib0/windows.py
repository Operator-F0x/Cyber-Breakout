import pygame, sys, time, random
from pygame.locals import *

pygame.init() #initializes pygame window
pygame.display.set_caption('KeyCast') #titlebar caption

GOSURF=pygame.display.set_mode((1800,1000),0,32) #sets main surface

gobackground = pygame.image.load('Python\\Cyber-Breakout\\img\\gameover.jpg') #background image for game

"""--------------------------------------------------------------------------"""
while True:

    def writetext():

    def quitgame():
        """exits programme without any errors"""
        for event in pygame.event.get(): #quitting process
            if event.type==QUIT: #if player selects 'exit button' on window
                pygame.quit() #pygame quit
                sys.exit() #system quit
    quitgame()

    def Surface():
        GOSURF.blit(gobackground,(0,0)) #background image

    Surface()

    pygame.display.update()