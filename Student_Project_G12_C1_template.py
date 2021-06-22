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
pygame.display.set_caption("Asteroid")
# Display game window 
background_image = pygame.image.load("bg2.jpg").convert()
#.blit() is how you copy the contents of one screen to another.
screen.blit(background_image,[0,0])
pygame.display.update()



#Draw WHITE Rectangle on given coordinates
WHITE=(255,255,255)

white_rect=pygame.Rect(100,100,30,30)

pygame.draw.rect(screen,WHITE,white_rect)

#Color or rectangle
BLUE=(0,0,255)

# Write Code here

#Draw Rectangle of blue color [left, top, width, height]

# Write code here

#Update the screen after pasting rectangle on it
pygame.display.update()
#Draw Green Rectangle
Green=(34, 139, 34)

#write code here

pygame.draw.rect(screen,Green,green_rect)
pygame.display.update()



