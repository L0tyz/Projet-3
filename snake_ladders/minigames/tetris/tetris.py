import pygame,sys
from game import Game

pygame.init()
dark_blue = (44, 44, 127)

#Créer la fenêtre du jeu 
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")

#Pour le "frame rate" du jeu
clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)


#Boucle permettant d'exécuter et fermer le jeu 
while True: 
    
    for event in pygame.event.get():
        #Pour fermer le jeu
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()
        if event.type == GAME_UPDATE:
            game.move_down()

    
    #Couleur
    screen.fill(dark_blue)
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)




