# Minijeu Snake pour le projet serpent et echelle en programmation 1. 
# Auteurs Elie Thauvette et Tommy Brunelle
# Date 

import pygame
import deplacement
import background


pygame.init()
#Taille ecran de jeu
ecran = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()

running = True


#Delta time (permet de faire des frame par secondes)
#Temps ecoule depuis la derniere frame
dt = 0

#Position de depart du serpent.
serpent = [pygame.Vector2(340, 340)]
#Taille du cercle noir
largeur_serpent = 20
#Couleur du cercle
couleur_serpent = "black"
#Score initial
score = 0

#Taille des pommes en frames
largeur_pomme = 15

# Mouvement initial
mouvement = pygame.Vector2(0, -1)
prochain_mouvement = pygame.Vector2(0, -1)

vitesse = 200 #pixels/sec

taille_case = 40 #pixels

# position des pommes avec les cases
colonnes = ecran.get_width() // taille_case
lignes = ecran.get_height() // taille_case

pos_pomme = background.pomme(colonnes, lignes, taille_case)



# Boucle de jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #creation de l'arriere plan, du serpent et de la pomme
    background.generer_background(ecran, taille_case)
   
    pygame.draw.circle(ecran, "red", pos_pomme, largeur_pomme)
    pygame.display.set_caption(f"score: {score}")
    for segment in serpent:
        pygame.draw.circle(ecran, couleur_serpent, segment, largeur_serpent)

    # mouvement avec touches
    prochain_mouvement = deplacement.ctl_mouvement(prochain_mouvement)
    mouvement = deplacement.marge(serpent, taille_case, vitesse, dt, prochain_mouvement, mouvement)

    # La position du joueur + une direction et vitesse de deplacement.
    nouveau_segment = serpent[0] + mouvement * vitesse * dt
    tete_serpent = serpent[0]
    serpent.insert(0, nouveau_segment)
    serpent.pop()

    # collision
    distance = serpent[0].distance_to(pos_pomme)
    if distance <= largeur_serpent + largeur_pomme:
        while True:
            
            pos_pomme = background.pomme(colonnes, lignes, taille_case)

            # Assurer que la pomme n'apparaisse pas sur le serpent.
            if pos_pomme.distance_to(segment) > largeur_serpent:
                break
       
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
