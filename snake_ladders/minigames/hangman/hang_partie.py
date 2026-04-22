"""
    Fichier contenant linterface sprite pour les membres de ken et barbie
    Realisé par Cassey Martin et Jake Chagnon
"""
import pygame
from hang_constantes import hang_constantes

class partie(pygame.sprite.Sprite):

    """
    Entrées: self, hache, tronc, bras_droit, bras_gauche (Strings représentant l'emplacement des images dans les fichiers)
    Sorties: Aucune
    But: Créer la possibilité de faire un objet barbie
    """
    # Emplacement pivot affecte lemplacement de la partie au complet
    # Angle affecte la rotation de la partie au complet
    def __init__(self, emplacement_image, scale, pivot_du_centre, position_pivot_initiale):
        super().__init__()

        self.image_originale = pygame.image.load(emplacement_image).convert_alpha()
        self.image_originale = pygame.transform.smoothscale(self.image_originale, scale)

        self.image = self.image_originale
        self.rect = self.image.get_rect()

        self.emplacement_pivot = pygame.math.Vector2(position_pivot_initiale) # Position pivot(epaule, genou, +), ce point ne bouge pas en rotation:(x,y)
        self.pivot_du_centre = pygame.math.Vector2(pivot_du_centre)

        self.angle = 0

    """
    Entrées: self
    Sorties: rien
    But: Mettre a jour les parametres voulu de la partie
    """
    def update(self):
        # Tourner les composantes VECTORIELLES representant le pivot
        tourner = self.pivot_du_centre.rotate(-self.angle)
        # Trouver nouveau centre (Positionnement image)
        nouveau_centre  = self.emplacement_pivot + tourner
        # Tourner image
        # Creer par defaut nouveau rectangle
        self.image = pygame.transform.rotate(self.image_originale, self.angle)
        # Recalibrer image en fonction de son nouveau centre(rectangle)
        # Positionner adequatement limage
        self.rect = self.image.get_rect(center=nouveau_centre)




