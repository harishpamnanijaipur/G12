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


SAFRON=(255, 153, 51)
safron_rect=pygame.Rect(50,100,200,30)

pygame.draw.rect(screen,SAFRON,safron_rect)

#Draw WHITE Rectangle on given coordinates
WHITE=(255,255,255)

white_rect=pygame.Rect(50,125,200,30)

pygame.draw.rect(screen,WHITE,white_rect)


#Draw Green Rectangle
Green=(34, 139, 34)
green_rect=pygame.Rect(50,150,200,30)

pygame.draw.rect(screen,Green,green_rect)
pygame.display.update()



