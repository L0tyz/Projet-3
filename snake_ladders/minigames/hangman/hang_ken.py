"""
    Fichier contenant les membres de ken avec leur translation approprier pour le mini jeu de hangman
    Realiser par Cassey Martin et Jake Chagnon
"""
import pygame
from hang_constantes import hang_constantes
from hang_partie import partie
class ken:
    """
    Entrées: self
    Sorties: Aucune
    But: Créer un objet ken comme partie de group sprite parts
    """
    def __init__(self):
        self.parts = pygame.sprite.Group()

        self.bras_droit = partie(hang_constantes.ken_bras_droit, hang_constantes.ken_scale, hang_constantes.ken_bras_droit_pivot_centre, hang_constantes.ken_bras_droit_position_pivot_init)
        self.bras_gauche = partie(hang_constantes.ken_bras_gauche, hang_constantes.ken_scale, hang_constantes.ken_bras_gauche_pivot_centre, hang_constantes.ken_bras_gauche_position_pivot_init)
        self.jambe_droite = partie(hang_constantes.ken_jambe_droite, hang_constantes.ken_scale, hang_constantes.ken_jambe_droite_pivot_centre, hang_constantes.ken_jambe_droite_position_pivot_init)
        self.jambe_gauche = partie(hang_constantes.ken_jambe_gauche, hang_constantes.ken_scale, hang_constantes.ken_jambe_gauche_pivot_centre, hang_constantes.ken_jambe_droite_position_pivot_init)
        self.tete = partie(hang_constantes.ken_tete, hang_constantes.ken_scale, hang_constantes.ken_tete_pivot_centre, hang_constantes.ken_tete_position_pivot_init)
        self.torse = partie(hang_constantes.ken_torse, hang_constantes.ken_scale, hang_constantes.ken_torse_pivot_centre, hang_constantes.ken_torse_position_pivot_init)

        self.parts.add(self.bras_droit, self.bras_gauche, self.jambe_droite, self.jambe_gauche, self.tete, self.torse)

    """
    Entrées: self
    Sorties: rien
    But: Changer les parametres voulu des images de ken
    """
    def update(self):
        self.swing_arm()
        self.parts.update()
    """
    Entrées: self
    Sorties: rien
    But: Dessiner les parametres voulu de ken
    """
    def draw(self, ecran):
        self.parts.draw(ecran)
    """
    Entrées: self
    Sorties: rien
    But: Tourner bras droit de barbie ctclkwise
    """
    def swing_arm(self):
        self.bras_droit.angle += 1
