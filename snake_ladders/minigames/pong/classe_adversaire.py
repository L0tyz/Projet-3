import pygame

class adversaire:
    def __init__(self):
        """
        But: Créer le rectangle de l'adversaire et attribuer sa vitesse de mouvement.
        Entrée: self.
        Sortie: Aucune.
        """
        self.rect = pygame.Rect(20, 300, 20, 80)

        # Niveau de difficulté de l'adversaire.
        self.vitesse = 350


    def mouvement(self, dt, balle_y):
        """
        But: Créer le rectangle du joueur et attribuer sa vitesse de mouvement.
        Entrées: self, dt, balle_y
        Sortie: Aucune.
        """
        # Si le Y central de l'adversaire est plus petit que la position Y de la balle:
        if self.rect.centery < balle_y:

            # L'adversaire descend.
            self.rect.y += self.vitesse * dt

        if self.rect.centery > balle_y:
            self.rect.y -= self.vitesse * dt


    def dessiner(self, ecran):
        """
        But: Dessiner le rectangle adversaire sur l'écran.
        Entrées: self, ecran.
        Sortie: Aucune.
        """
        pygame.draw.rect(ecran, "white", self.rect)


    def reinitialiser(self):
        """
        But: Réinitialiser la position du rectangle adversaire.
        Entrée: self.
        Sortie: Aucune.
        """
        self.rect = pygame.Rect(20, 300, 20, 80)