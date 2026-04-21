import pygame
import random
def generer_background(ecran, taille_case):

    # La couleur de fond avant d'ajouter le quadrillé.
    ecran.fill((75, 154, 76))

    # Pour chaque pixel de 0 à la largeur de l'écran, on a un marqueur aux 40 pixels.
    for x in range(0, ecran.get_width(), taille_case):
        for y in range(0, ecran.get_height(), taille_case):

            # Si le pixel X/40 + le pixel Y/40 modulo 2 est égal à 0, cest pair, nn colore.
            if (x // taille_case + y // taille_case) % 2 == 0:

                # Dessine un carré sur l'écran, de la couleur voulue.
                # Taille X de 40 pixels et taille Y de 40 pixels.
                pygame.draw.rect(ecran, (67, 138, 69), (x, y, taille_case, taille_case))

def pomme(colonnes, lignes, taille_case):
    pomme_col = random.randint(0, colonnes - 1)
    pomme_ligne = random.randint(0, lignes - 1)

    pomme_x = pomme_col * taille_case + taille_case / 2
    pomme_y = pomme_ligne * taille_case + taille_case / 2

    return pygame.Vector2(pomme_x, pomme_y)