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

running = True

dt = 0
largeur_serpent = 20
couleur_serpent = "black"
score = 0
largeur_pomme = 15
mouvement = pygame.Vector2(0, -1)
prochain_mouvement = pygame.Vector2(0, -1)
vitesse = 200 #pixels/sec
taille_case = 40 #pixels
SCORE_VICTOIRE = 30

#creation d'objets
background_obj = background(taille_case)
pomme_obj = pomme(ecran.get_width() // taille_case, ecran.get_height() // taille_case, taille_case, ecran, largeur_pomme)
serpent_obj = serpent_object(taille_case, largeur_serpent, couleur_serpent, vitesse, (340, 340))

font = pygame.font.SysFont(None, 32)

# Boucle de jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #creation de l'arriere plan, du serpent et de la pomme
    background_obj.generer_background(ecran)
    serpent_obj.creer(ecran)
    pomme_obj.creer(ecran)
   
    # mouvement avec touches
    serpent_obj.ctl_mouvement()
    serpent_obj.marge(dt)
    serpent_obj.animation(dt)

    surf = font.render(f"Score: {score}/{SCORE_VICTOIRE}", True, (255, 255, 255))
    ecran.blit(surf, (10, 10))

    # collision
    
    if serpent_obj.corp_serpent[0].distance_to(pomme_obj.pos) <= largeur_serpent + largeur_pomme:
        pomme_obj.generer(serpent_obj.corp_serpent, largeur_serpent, largeur_pomme)
        serpent_obj.grandir()
        serpent_obj.vitesse += 5
        score += 1
        if score >= SCORE_VICTOIRE:
            running = False
        
    
    # Si le joueur sort de l'ecran, le jeu se termine.
    if serpent_obj.collision_mur(ecran):
        running = False
    
    #collision du serpent avec lui meme ferme le jeu
    if serpent_obj.collision_serpent():
        running = False
    

    pygame.display.flip()
    dt = clock.tick(60) / 1000 #16 msec entre chaque frame

pygame.quit()
