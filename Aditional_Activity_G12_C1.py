# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:03:03 2021

@author: dell
"""

import pygame, sys, math,random

#initialising pygame and its functions 
pygame.init()

# creating game window and title
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Space Invaders")

# Display game window 
background_image = pygame.image.load("bg2.jpg").convert()
screen.fill((0,0,0))
screen.blit(background_image,[0,0])


#Creating Players 
player=pygame.Rect(200,200,30,30)
player_image = pygame.image.load("enemy.png").convert_alpha()
screen.blit(player_image , player)
pygame.display.update()