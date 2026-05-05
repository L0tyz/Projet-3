"""
    Realisé par Cassey Martin
    But: Créer des parties pour membres de barbie et ken faisant partie de l'interface sprite
"""
import pygame

class partie(pygame.sprite.Sprite):

    """
    Entrées: self, emplacement_image, scale, pivot_du_centre, position_pivot_initiale
    Sorties: Aucune (None par défaut, ce que python s'attend)
    But: Créer une partie de corps en image qui applique l'interface Sprite
    """
    def __init__(self, emplacement_image, scale, pivot_du_centre, position_pivot_initiale):
        super().__init__()

        self.image_originale = pygame.image.load(emplacement_image).convert_alpha()
        self.image_originale = pygame.transform.smoothscale(self.image_originale, scale)

        self.image = self.image_originale
        self.rect = self.image.get_rect()

        self.emplacement_pivot = pygame.math.Vector2(position_pivot_initiale) # Position pivot(epaule, genou, +)
        self.pivot_du_centre = pygame.math.Vector2(pivot_du_centre)

        self.angle = 0 # Angle de rotation absolue

    """
    Entrées: self
    Sorties: Aucune (Bonne pratique avec l'interface Sprite puisque servirait à rien dans le programme si était quelque chose)
    But: Mettre a jour les parametres voulu de la partie
    NOTE: Appeler automatiquement par Sprite(Elle DOIT s'appeler update())
    """
    def update(self):
        tourner = self.pivot_du_centre.rotate(-self.angle) # Tourner les composantes vectorielles representant le pivot
        nouveau_centre  = self.emplacement_pivot + tourner # Trouver nouveau centre (Positionnement image)
        self.image = pygame.transform.rotate(self.image_originale, self.angle) # Tourner image, creer par défaut nouveau rectangle
        self.rect = self.image.get_rect(center=nouveau_centre) # Positionnement adequat image en fonctio de son nouveau centre(rectangle)




