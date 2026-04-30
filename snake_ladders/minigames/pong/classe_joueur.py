import pygame

class joueur:
    def __init__(self):
        """
        But: Créer le rectangle du joueur et attribuer sa vitesse de mouvement.
        Entrée: self.
        Sortie: Aucune.
        """
        # Rectangle de 20 pixels par 80, placé aux coordonnées 680(x) et 300(y).
        self.rect = pygame.Rect(680, 300, 20, 80)
        self.vitesse = 300


    def mouvement(self, dt):
        """
        But: Faire bouger le rectangle joueur lorsqu'on appuie\
             sur les touches w ou s.
        Entrée: self, dt.
        Sortie: Aucune.
        """
        touches = pygame.key.get_pressed()

        if touches[pygame.K_w]:

            # Le joueur monte sur l'axe Y selon la vitesse établie plus haut.
            self.rect.y -= self.vitesse * dt

        if touches[pygame.K_s]:
            self.rect.y += self.vitesse * dt


    def dessiner(self, ecran):
        """
        But: Dessiner le rectangle joueur sur l'ecran de jeu.
        Entrée: self, ecran.
        Sortie: Aucune.
        """
        pygame.draw.rect(ecran, "white", self.rect)


    def reinitialiser(self):
        """
        But: Réinitialiser la position du rectangle joueur.
        Entrée: self.
        Sortie: Aucune.
        """
        self.rect = pygame.Rect(680, 300, 20, 80)