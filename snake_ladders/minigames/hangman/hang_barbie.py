"""
    Fichier contenant les membres de ken avec leur translations appropriées pour le mini jeu de hangman
    Realisé par Cassey Martin et Jake Chagnon
"""
import pygame
from hang_partie import partie
from hang_constantes import hang_constantes
class barbie:
    """
    Entrées: self, hache, tronc, bras_droit, bras_gauche (Strings représentant l'emplacement des images dans les fichiers)
    Sorties: Aucune
    But: Créer la possibilité de faire un objet barbie
    """
    def __init__(self):
        self.parts = pygame.sprite.Group()

        self.hache = partie(hang_constantes.hache, hang_constantes.hache_scale_tuple, hang_constantes.hache_pivot_centre, hang_constantes.hache_position_pivot_init)
        self.tronc = partie(hang_constantes.barbie_tronc, hang_constantes.barbie_tronc_scale, hang_constantes.barbie_tronc_pivot_centre, hang_constantes.barbie_tronc_position_pivot_init)
        self.bras_droit = partie(hang_constantes.barbie_bras_droit, hang_constantes.barbie_scale, hang_constantes.barbie_bras_droit_pivot_centre, hang_constantes.barbie_bras_droit_position_pivot_init)
        self.bras_gauche = partie(hang_constantes.barbie_bras_gauche, hang_constantes.barbie_scale, hang_constantes.barbie_bras_gauche_pivot_centre, hang_constantes.barbie_bras_gauche_position_pivot_init)

        self.debug = False

        self.parts.add(self.hache, self.tronc, self.bras_droit, self.bras_gauche)

    """
    Entrées: self
    Sorties: rien
    But: Changer les parametres voulu des images de barbie
    """
    def update(self):
        self.swing_arm()
        self.parts.update()
    """
    Entrées: self
    Sorties: rien
    But: Dessiner les parametres voulu de la partie
    """
    def draw(self, ecran):
        self.parts.draw(ecran)
        if self.debug:
            for part in self.parts:
                pygame.draw.circle(ecran, (255, 0, 0), part.emplacement_pivot, 10)
                pygame.draw.line(ecran, (0, 0, 255), part.emplacement_pivot, part.rect.center, 10)
        

    """
    Entrées: self
    Sorties: rien
    But: Tourner bras droit de barbie ctclkwise
    """
    def swing_arm(self):
        self.bras_droit.angle += 1
