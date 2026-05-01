""" Minijeu Snake pour le projet serpent et echelle en programmation 1. """
# Auteurs Elie Thauvette et Tommy Brunelle
# Date 

import pygame
from deplacement import deplacements
from background import background, pomme


pygame.init()
#Taille ecran de jeu
ecran = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()



running = True


#Delta time (permet de faire des frame par secondes)
#Temps ecoule depuis la derniere frame
dt = 0


serpent = [pygame.Vector2(340, 340)]
largeur_serpent = 20
couleur_serpent = "black"

score = 0
largeur_pomme = 15

# Mouvement initial
mouvement = pygame.Vector2(0, -1)
prochain_mouvement = pygame.Vector2(0, -1)

vitesse = 200 #pixels/sec
taille_case = 40 #pixels

# position des pommes avec les cases
colonnes = ecran.get_width() // taille_case
lignes = ecran.get_height() // taille_case

#creation d'objets
background = background(taille_case)
pos_pomme = pomme(colonnes, lignes, taille_case, ecran)
control = deplacements(taille_case, vitesse)


# Boucle de jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #creation de l'arriere plan, du serpent et de la pomme
    background.generer_background(ecran)
   
    pygame.draw.circle(ecran, "red", pos_pomme.possition_pomme(), largeur_pomme)
    pygame.display.set_caption(f"score: {score}")

    for segment in serpent:
        pygame.draw.circle(ecran, couleur_serpent, segment, largeur_serpent)

    # mouvement avec touches
    prochain_mouvement = deplacements.ctl_mouvement(prochain_mouvement)
    mouvement = control.marge(serpent, prochain_mouvement, mouvement, dt)

    # La position du joueur + une direction et vitesse de deplacement.
    nouveau_segment = serpent[0] + mouvement * vitesse * dt
    tete_serpent = serpent[0]
    serpent.insert(0, nouveau_segment)
    serpent.pop()

    # collision
    
    if serpent[0].distance_to(pos_pomme.possition_pomme()) <= largeur_serpent + largeur_pomme:
        pos_pomme.generer_pomme(serpent, largeur_serpent, largeur_pomme)
        for i in range(10):
                serpent.append(serpent[-1])
        vitesse += 5
        score += 1
        
    
    # Si le joueur sort de l'ecran, le jeu se termine.
    if serpent[0].x >= ecran.get_width() or serpent[0].x <= 0 or serpent[0].y >= ecran.get_height() or serpent[0].y <= 0:
        running = False
    
    #collision du serpent avec lui meme ferme le jeu
    for segment in serpent[20:]:        
        if tete_serpent.distance_to(segment) < largeur_serpent +5:
            running = False

    pygame.display.flip()
    dt = clock.tick(60) / 1000 #16 msec entre chaque frame
pygame.quit()
