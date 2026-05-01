"""
    Fichier contenant les membres de ken avec leur translation approprier pour le mini jeu de hangman
    Realiser par Cassey Martin et Jake Chagnon
"""
import pygame
from hang_constantes import hang_constantes
from hang_partie import partie
from hang_constantes import etat_hangman
class ken:
    """
    Entrées: self
    Sorties: Aucune
    But: Créer un objet ken comme partie de group sprite parts
    """
    def __init__(self):
        self.parts = pygame.sprite.Group()

        self.bras_droit = partie(hang_constantes.ken_bras_droit, hang_constantes.ken_bras_scale, hang_constantes.ken_bras_droit_pivot_centre, hang_constantes.ken_bras_droit_position_pivot_init)
        self.bras_gauche = partie(hang_constantes.ken_bras_gauche, hang_constantes.ken_bras_scale, hang_constantes.ken_bras_gauche_pivot_centre, hang_constantes.ken_bras_gauche_position_pivot_init)
        self.jambe_droite = partie(hang_constantes.ken_jambe_droite, hang_constantes.ken_jambes_scale, hang_constantes.ken_jambe_droite_pivot_centre, hang_constantes.ken_jambe_droite_position_pivot_init)
        self.jambe_gauche = partie(hang_constantes.ken_jambe_gauche, hang_constantes.ken_jambes_scale, hang_constantes.ken_jambe_gauche_pivot_centre, hang_constantes.ken_jambe_gauche_position_pivot_init)
        self.tete = partie(hang_constantes.ken_tete, hang_constantes.ken_scale, hang_constantes.ken_tete_pivot_centre, hang_constantes.ken_tete_position_pivot_init)
        self.torse = partie(hang_constantes.ken_torse, hang_constantes.ken_torse_scale, hang_constantes.ken_torse_pivot_centre, hang_constantes.ken_torse_position_pivot_init)

        self.debug = False

        self.parts.add(self.bras_droit, self.bras_gauche, self.jambe_droite, self.jambe_gauche, self.tete, self.torse)

    """
    Entrées: self
    Sorties: rien
    But: Changer les parametres voulu des images de ken
    """
    def mettre_a_jour(self, etat, partie_frapper):
        match etat:
            case etat_hangman.AUCUN_ECHEC:
                #self.swing_arm()
                pass
            case etat_hangman.UNE_ERREUR:
                if partie_frapper:
                    self.parts.remove_internal(partie_frapper)
            case etat_hangman.DEUX_ERREURS:
                if partie_frapper:
                    self.parts.remove_internal(partie_frapper)
            case etat_hangman.TROIS_ERREURS:
                if partie_frapper:
                    self.parts.remove_internal(partie_frapper)
            case etat_hangman.QUATRE_ERREURS:
                if partie_frapper:
                    self.parts.remove_internal(partie_frapper)
            case etat_hangman.CINQ_ERREURS:
                if partie_frapper:
                    self.parts.remove_internal(partie_frapper)
            case etat_hangman.SIX_ERREURS:
                if partie_frapper:
                    self.parts.remove_internal(partie_frapper)
            case __:
                pass
        self.parts.update()
    """
    Entrées: self, ecran
    Sorties: rien
    But: Dessiner ken a lecran
    """
    def dessiner(self, ecran):
        self.parts.draw(ecran)
        if self.debug:
            for part in self.parts:
                pygame.draw.circle(ecran, (255, 0, 0), part.emplacement_pivot, 10)
                pygame.draw.line(ecran, (0, 0, 255), part.emplacement_pivot, part.rect.center, 10)
