""" 
Minijeu Snake pour le projet serpent et echelle en programmation 1. 
Auteurs: Elie Thauvette et Tommy Brunelle
date: 5 mai 2026
"""

import pygame

class joueur:
    def __init__(self, screen):
        """
        But: Créer le rectangle du joueur et attribuer sa vitesse de mouvement.
        Entrée: self, ecran.
        Sortie: Aucune.
        """
        # Rectangle de 20 pixels par 80, placé aux coordonnées choisies en x et y.
        self.rect = pygame.Rect(screen.get_width() - 40, 300, 20, 80)
        self.vitesse = 300


    def mouvement(self, dt):
        """
        But: Faire bouger le rectangle joueur lorsqu'on appuie sur les touches UP, DOWN ou w, s.
        Entrée: self, dt.
        Sortie: Aucune.
        """
        touches = pygame.key.get_pressed()

        if touches[pygame.K_w or pygame.K_UP]:

            # Le joueur monte sur l'axe Y selon la vitesse établie plus haut.
            self.rect.y -= self.vitesse * dt

        if touches[pygame.K_s or pygame.K_DOWN]:
            self.rect.y += self.vitesse * dt


    def dessiner(self, screen):
        """
        But: Dessiner le rectangle joueur sur l'ecran de jeu.
        Entrée: self, ecran.
        Sortie: Aucune.
        """
        pygame.draw.rect(screen, "white", self.rect)


    def reinitialiser(self):
        """
        But: Réinitialiser la position du rectangle joueur.
        Entrée: self.
        Sortie: Aucune.
        """
        self.rect = pygame.Rect(self.rect.x, 300, 20, 80)