""" Minijeu Snake pour le projet serpent et echelle en programmation 1. """
"""Auteurs Elie Thauvette et Tommy Brunelle"""

import pygame
from snake_classes import background, pomme, serpent_object


def run_minijeu(screen):
    clock = pygame.time.Clock()
    dt = 0

    largeur_serpent = 20
    couleur_serpent = "black"
    score = 0
    largeur_pomme = 15
    mouvement = pygame.Vector2(0, -1)
    vitesse = 200
    taille_case = 40
    SCORE_VICTOIRE = 5

    background_obj = background(taille_case)
    pomme_obj = pomme(screen.get_width() // taille_case, screen.get_height() // taille_case, taille_case, screen, largeur_pomme)
    serpent = serpent_object(taille_case, largeur_serpent, couleur_serpent, vitesse, (screen.get_width() // 2, screen.get_height() // 2))

    font = pygame.font.SysFont(None, 32)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        background_obj.generer_background(screen)
        serpent.creer(screen)
        pomme_obj.creer(screen)

        serpent.ctl_mouvement()
        serpent.marge(dt)
        serpent.animation(dt)

        # Score affiché
        surf = font.render(f"Score : {score}/{SCORE_VICTOIRE}", True, (255, 255, 255))
        screen.blit(surf, (10, 10))

        if serpent.corp_serpent[0].distance_to(pomme_obj.pos) <= largeur_serpent + largeur_pomme:
            pomme_obj.generer(serpent.corp_serpent, largeur_serpent, largeur_pomme)
            serpent.grandir()
            serpent.vitesse += 5
            score += 1
            if score >= SCORE_VICTOIRE:
                running = False

        if serpent.collision_mur(screen):
            running = False

        if serpent.collision_serpent():
            running = False

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    return score >= SCORE_VICTOIRE


if __name__ == "__main__":
    pygame.init()
    ecran = pygame.display.set_mode((720, 720))
    run_minijeu(ecran)
    pygame.quit()