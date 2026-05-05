""" 
Minijeu Snake pour le projet serpent et echelle en programmation 1. 
Auteurs Elie Thauvette et Tommy Brunelle
date 5 mai 2026
"""
 
import pygame
from snake_classes import background, pomme, serpent_object

pygame.init()

#Taille ecran de jeu
ecran = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()

menu_start = True
running = False

#Delta time (permet de faire des frame par secondes)
dt = 0

largeur_serpent = 20
couleur_serpent = "black"

score = 0
largeur_pomme = 15

# Mouvement initial
mouvement = pygame.Vector2(0, -1)
prochain_mouvement = pygame.Vector2(0, -1)

vitesse = 200 #pixels/sec
taille_case = 40 #pixels

#creation d'objets
background = background(taille_case)
pomme = pomme(ecran.get_width() // taille_case, ecran.get_height() // taille_case, taille_case, ecran, largeur_pomme)
serpent = serpent_object(taille_case, largeur_serpent, couleur_serpent, vitesse, (340, 340))

while menu_start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_start = False
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu_start = False
            running = True

# Boucle de jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #creation de l'arriere plan, du serpent et de la pomme
    background.generer_background(ecran)
    serpent.creer(ecran)
    pomme.creer(ecran)
   
    # mouvement avec touches
    serpent.ctl_mouvement()
    serpent.marge(dt)
    serpent.animation(dt)

    pygame.display.set_caption(f"score: {score}")

    # collision
    
    if serpent.corp_serpent[0].distance_to(pomme.pos) <= largeur_serpent + largeur_pomme:
        pomme.generer(serpent.corp_serpent, largeur_serpent, largeur_pomme)
        serpent.grandir()
        serpent.vitesse += 5
        score += 1
        if score >= 30:
            running = False
        
    
    # Si le joueur sort de l'ecran, le jeu se termine.
    if serpent.collision_mur(ecran):
        running = False
    
    #collision du serpent avec lui meme ferme le jeu
    if serpent.collision_serpent():
        running = False
    

    pygame.display.flip()
    dt = clock.tick(60) / 1000 #16 msec entre chaque frame

pygame.quit()
