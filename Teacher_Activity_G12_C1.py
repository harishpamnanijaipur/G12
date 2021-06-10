import pygame

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
player_image = pygame.image.load("player.png").convert_alpha()
enemy_image = pygame.image.load("enemy.png").convert_alpha()

enemy=pygame.Rect(300,300,30,30)

screen.blit(player_image , player)
screen.blit(enemy_image , enemy)
pygame.display.update()



crashed = False


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()

    
pygame.quit()
#quit()    