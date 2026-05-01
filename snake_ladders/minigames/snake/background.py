# Fonction for faire l'arriere plan du minijeu snake, et pour generer la position de la pomme.
# Auteurs Elie Thauvette et Tommy Brunelle
# Date 

import pygame
import random

class background:
    def __init__(self, taille_case):
        self.taille_case = taille_case
    def generer_background(self, ecran):

        # La couleur de fond avant d'ajouter le quadrillé.
        ecran.fill((75, 154, 76))

        # Pour chaque pixel de 0 à la largeur de l'écran, on a un marqueur aux 40 pixels.
        for x in range(0, ecran.get_width(), self.taille_case):
            for y in range(0, ecran.get_height(), self.taille_case):

                # Si le pixel X/40 + le pixel Y/40 modulo 2 est égal à 0, cest pair, nn colore.
                if (x // self.taille_case + y // self.taille_case) % 2 == 0:

                    # Dessine un carré sur l'écran, de la couleur voulue.
                    # Taille X de 40 pixels et taille Y de 40 pixels.
                    pygame.draw.rect(ecran, (67, 138, 69), (x, y, self.taille_case, self.taille_case))

# Fonction pour generer la position de la pomme.
class pomme:

    def __init__(self, colonnes, lignes, taille_case, ecran):
        self.colonnes = colonnes
        self.lignes = lignes
        self.taille_case = taille_case
        self.ecran = ecran

    def possition_pomme(self):
        pomme_col = random.randint(0, self.colonnes - 1)
        pomme_ligne = random.randint(0, self.lignes - 1)

        pomme_x = pomme_col * self.taille_case + self.taille_case / 2
        pomme_y = pomme_ligne * self.taille_case + self.taille_case / 2

        return pygame.Vector2(pomme_x, pomme_y)

    def generer_pomme(self, serpent, largeur_serpent, largeur_pomme):
        # Tant que la position de la pomme est sur le serpent, on regénère une nouvelle position.
        while True:
            self.pos = self.possition_pomme()
            collision = False
            for segment in serpent: 
                if self.pos.distance_to(segment) < largeur_serpent + largeur_pomme:
                    collision = True
                    break
            if not collision:   
                break

        # Dessine la pomme sur l'écran à la position générée.
        pygame.draw.circle(self.ecran, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), largeur_pomme // 2)

        return self.pos