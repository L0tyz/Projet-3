import pygame,sys

pygame.init(

#Créer la fenêtre du jeu (x,y)
screen = pygame.display.set_mode((300,600)))
pygame.display.set_caption("Tetris")

#Pour le "frame rate" du jeu
clock = pygame.time.Clock()

while True: 
    
    for event in pygame.event.get():
        #Por fermer le jeu
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)




