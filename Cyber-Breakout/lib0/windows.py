import pygame, sys, time, random
from pygame.locals import *

pygame.init() #initializes pygame window
pygame.display.set_caption('KeyCast') #titlebar caption

GOSURF=pygame.display.set_mode((600,400),0,32) #sets main surface

gobackground = pygame.image.load('Python\\Cyber-Breakout\\img\\gameover.jpg') #background image for game


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


"""--------------------------------------------------------------------------
le chiamate alle funzioni sono di prova e il while 1 potra essere messo in main.py con al interno le chiamate

"""


while 1:

#funzione per la chiusura del gioco
    def quitgame():
        """exits programme without any errors"""
        for event in pygame.event.get(): #quitting process
            if event.type==QUIT: #if player selects 'exit button' on window
                pygame.quit() #pygame quit
                sys.exit() #system quit
    quitgame()

#funzione per posizione un immagine di background
    def Surface():
        GOSURF.blit(gobackground,(0,0)) #background image

    Surface()

    pygame.display.update()