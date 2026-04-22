import pygame
import random
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

#Position de depart en frames.
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




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background.generer_background(ecran, taille_case)
   
   
    pygame.draw.circle(ecran, "red", pos_pomme, largeur_pomme)
    pygame.display.set_caption(f"score: {score}")
    for segment in serpent:
        pygame.draw.circle(ecran, couleur_serpent, segment, largeur_serpent)

    # mouvement avec touches
    prochain_mouvement = deplacement.ctl_mouvement(prochain_mouvement)
    mouvement = deplacement.marge(serpent, taille_case, vitesse, dt, prochain_mouvement, mouvement)

    # La position du joueur + une direction et vitesse de deplacement.
    new_head = serpent[0] + mouvement * vitesse * dt
    serpent.insert(0, new_head)
    serpent.pop()

    # collision
    distance = serpent[0].distance_to(pos_pomme)
    if distance <= largeur_serpent + largeur_pomme:
        while True:
            
            pos_pomme = background.pomme(colonnes, lignes, taille_case)
            if pos_pomme not in serpent:
                break
       
        for i in range(10):
                serpent.append(serpent[-1])
        vitesse += 10
        score += 1
        
    
    # Si le joueur sort de l'ecran, le jeu se termine.
    if serpent[0].x >= ecran.get_width() or serpent[0].x <= 0 or serpent[0].y >= ecran.get_height() or serpent[0].y <= 0:
        running = False
    
    tete_serpent = serpent[0]
    for segment in serpent[11:]:        
        if tete_serpent.distance_to(segment) < largeur_serpent:
            running = False

    pygame.display.flip()
    dt = clock.tick(60) / 1000 #16 msec entre chaque frame
pygame.quit()
