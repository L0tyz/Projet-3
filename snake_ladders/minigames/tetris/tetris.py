import pygame,sys
from grid import Grid 
from blocks import *

pygame.init()
dark_blue = (44, 44, 127)

#Créer la fenêtre du jeu 
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")

#Pour le "frame rate" du jeu
clock = pygame.time.Clock()

game_grid = Grid()

block = LBlock()

#Boucle permettant d'exécuter et fermer le jeu 
while True: 
    
    for event in pygame.event.get():
        #Pour fermer le jeu
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Couleur
    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)
    
    pygame.display.update()
    clock.tick(60)




