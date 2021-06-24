# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:03:03 2021

@author: dell
"""

import pygame
#initialising pygame and its functions 
pygame.init()
# creating game window and title
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Rectangle Creation")
# Display game window 
background_image = pygame.image.load("bg2.jpg").convert()
#.blit() is how you copy the contents of one screen to another.
screen.blit(background_image,[0,0])
pygame.display.update()


#Color or rectangle
BLUE=(0,0,255)

player=player=pygame.Rect(200,200,30,30)

#Draw Rectangle of blue color [left, top, width, height]

pygame.draw.rect(screen,BLUE,player)

#Update the screen after pasting rectangle on it
pygame.display.update()


#Draw WHITE Rectangle on given coordinates
WHITE=(255,255,255)

enemy=pygame.Rect(200,230,30,30)

pygame.draw.rect(screen,WHITE,enemy)

pygame.display.update()

Green=(255,0,255)

player=player=pygame.Rect(200,260,30,30)
pygame.draw.rect(screen,Green,player)
pygame.display.update()

