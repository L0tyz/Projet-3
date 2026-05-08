""" 
Minijeu Snake pour le projet serpent et echelle en programmation 1. 
Auteurs: Elie Thauvette et Tommy Brunelle
date: 5 mai 2026
"""
 
import pygame
from snake_classes import background, pomme, serpent_object

def run_minijeu(screen, infinite=False):

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.pause()  # Arrête la musique de fond du jeu principal


    son_pomme = pygame.mixer.Sound("snake_ladders/minigames/snake/assets/pomme.mp3")
    son_pomme.set_volume(0.3)
    musique_fond = pygame.mixer.Sound("snake_ladders/minigames/snake/assets/Snake_Eater.mp3")
    musique_fond.set_volume(0.5)
    musique_fond.play(-1)  # Joue la musique en boucle
    # Taille de l'écran de jeu.
    ecran = pygame.display.set_mode((1000,800))

    clock = pygame.time.Clock()
    dt = 0
    running = True
    largeur_serpent = 20
    couleur_serpent = "black"
    score = 0
    largeur_pomme = 15
    vitesse = 200 # Pixels/sec.
    taille_case = 40 # Pixels.
    SCORE_VICTOIRE = 30

    # Création d'objets.
    background_obj = background(taille_case)
    pomme_obj = pomme(ecran.get_width() // taille_case, ecran.get_height() // taille_case, taille_case, ecran, largeur_pomme)
    serpent_obj = serpent_object(taille_case, largeur_serpent, couleur_serpent, vitesse, (340, 340))

    # Police d'écriture pour le score.
    police = pygame.font.SysFont(None, 32)

    # Boucle de jeu.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Création de l'arrière plan, du serpent et de la pomme.
        background_obj.generer_background(ecran)
        serpent_obj.creer(ecran)
        pomme_obj.creer(ecran)
    
        # Mouvement.
        serpent_obj.ctl_mouvement()
        serpent_obj.marge(dt)
        serpent_obj.animation(dt)
        # Affichage en premier plan du score.
        surf = police.render(f"Score: {score}/{SCORE_VICTOIRE}", True, (255, 255, 255))
        ecran.blit(surf, (10, 10))

        # Collisions.
        if serpent_obj.corp_serpent[0].distance_to(pomme_obj.pos) <= largeur_serpent + largeur_pomme:
            pomme_obj.generer(serpent_obj.corp_serpent, largeur_serpent, largeur_pomme)
            serpent_obj.grandir()
            serpent_obj.vitesse += 5
            score += 1
            son_pomme.play()  # Lecture du son lorsqu'une pomme est mangée
            if score >= SCORE_VICTOIRE:
                running = False
                musique_fond.stop()
                pygame.mixer.music.unpause()  # Joue la musique du menu principal en boucle
            
        
        # Si le joueur sort de l'écran, le jeu se termine.
        if serpent_obj.collision_mur(ecran):
            running = False
            musique_fond.stop()
            pygame.mixer.music.unpause()  # Joue la musique du menu principal en boucle
            
        
        # Si il y a collision du serpent avec lui-même: ferme le jeu.
        if serpent_obj.collision_serpent():
            running = False
            musique_fond.stop()  # Arrête la musique de fond lorsque le jeu se termine
            pygame.mixer.music.unpause()  # Joue la musique du menu principal en boucle
        

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    return SCORE_VICTOIRE >= score



   
