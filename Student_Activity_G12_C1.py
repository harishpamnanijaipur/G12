import pygame

#initialising pygame and its functions 
pygame.init()

# creating game window and title
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Space Invaders")

# Display game window 
background_image = pygame.image.load("bg2.jpg").convert()
screen.fill((0,0,0))



#Creating Players 

enemy_image = pygame.image.load("enemy.png").convert_alpha()

enemy=pygame.Rect(300,300,30,30)


screen.blit(enemy_image , enemy)
pygame.display.update()



pygame.quit()
#quit()    
