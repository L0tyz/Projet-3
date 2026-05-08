""" 
Minijeu Snake pour le projet serpent et echelle en programmation 1. 
Auteurs: Elie Thauvette et Tommy Brunelle
date: 5 mai 2026
"""

import pygame
import random
import math

class balle:
    def __init__(self):
        """
        But: Indiquer les valeurs de base de la balle.\
             (Sa position, sa taille, sa vitesse et sa trajectoire).
        Entrée: self.
        Sortie: Aucune.
        """
        self.position_x = 360
        self.position_y = 360
        self.rayon = 15
        self.trajectoire_x = 250
        self.trajectoire_y = 180
        self.vitesse = 300


    def mouvement(self, dt):
        """
        But: Modifier la position de la balle selon sa trajectoire et vitesse.
        Entrées: self, dt.
        Sortie: Aucune.
        """
        self.position_x += self.trajectoire_x * dt
        self.position_y += self.trajectoire_y * dt


    def rebonds(self, joueur, adversaire, ecran, son_pong):
        """
        But: Modifier la trajectoire, position et vitesse de la balle\
             selon ce qu'elle touche.
        Entrées: self, joueur, adversaire, ecran, son_pong.
        Sortie: Aucune.
        """

        # Rebond sur le mur du haut.
        if self.position_y - self.rayon <= 0:
            self.position_y = self.rayon
            self.trajectoire_y = -self.trajectoire_y
            son_pong.play()

        # Mur du bas. 720 parce que c'est la taille de l'écran.
        if self.position_y + self.rayon >= ecran.get_height():
            self.position_y = ecran.get_height() - self.rayon
            self.trajectoire_y = -self.trajectoire_y
            son_pong.play()

        # Si une partie de la balle se trouve dans le rectangle joueur: True
        if joueur.rect.collidepoint(self.position_x + self.rayon, self.position_y):

            # Replace la balle sur le coté gauche du joueur.
            self.position_x = joueur.rect.left - self.rayon

            # identifier où a touché la balle sur le joueur.
            endroit_impact = (self.position_y - joueur.rect.centery) / (joueur.rect.height / 2)

            # Limiter à 60 degrés. Plus haut donne trop d'angle. C'est trop facile.
            angle = endroit_impact * math.radians(60)

            # Nouvelle trajectoire et on augmente la vitesse de la balle.
            self.trajectoire_x = -math.cos(angle) * self.vitesse
            self.trajectoire_y = math.sin(angle) * self.vitesse

            self.vitesse *= 1.05
            son_pong.play()

        # Même logique que pour le joueur.
        if adversaire.rect.collidepoint(self.position_x - self.rayon, self.position_y):

            self.position_x = adversaire.rect.right + self.rayon

            endroit_impact = (self.position_y - adversaire.rect.centery) / (adversaire.rect.height / 2)

            angle = endroit_impact * math.radians(60)

            self.trajectoire_x = math.cos(angle) * self.vitesse
            self.trajectoire_y = math.sin(angle) * self.vitesse

            self.vitesse *= 1.05
            son_pong.play()


    def dessiner(self, ecran):
        """
        But: Dessiner la balle au bon endroit sur l'écran de jeu.
        Entrées: self, ecran.
        Sortie: Aucune.
        """
        pygame.draw.circle(ecran, "white", (self.position_x, self.position_y), self.rayon)


    def reinitialiser(self):
        """
        But: Réinitialiser la vitesse, les trajectoires et positions de départ de la balle.
        Entrée: self.
        Sortie: Aucune.
        """
        self.position_x = 360
        self.position_y = 360
        self.vitesse = 300

        # Attribuer une trajectoire aléatoire après chaque point.
        self.trajectoire_x = random.choice([-250, 250])
        self.trajectoire_y = random.randint(-200, 200)