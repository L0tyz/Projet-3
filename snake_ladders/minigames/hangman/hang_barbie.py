"""
    Fichier contenant les membres de ken avec leur translations appropriées pour le mini jeu de hangman
    Realisé par Cassey Martin et Jake Chagnon
"""
import pygame
from hang_partie import partie
from hang_constantes import hang_constantes
from hang_constantes import etat_hangman
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

        self.aller = True

    """
    Entrées: self
    Sorties: rien
    But: Changer les parametres voulu des images de barbie
    """
    def update(self, etat):
        self.swing_arm()
        self.hache_position(etat)
        match etat:
            case etat_hangman.AUCUN_ECHEC:
                self.swing_arm()
            case etat_hangman.UNE_ERREUR:
                self.swing_arm()
            case etat_hangman.DEUX_ERREURS:
                self.swing_arm()
            case etat_hangman.TROIS_ERREURS:
                self.swing_arm()
            case etat_hangman.QUATRE_ERREURS:
                self.swing_arm()
            case etat_hangman.CINQ_ERREURS:
                self.swing_arm()
            case etat_hangman.SIX_ERREURS:
                self.swing_arm()
            case __:
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

    def hache_position(self, etat):
        match etat:
            case etat_hangman.AUCUN_ECHEC:
                self.hache.angle +=1    
            case etat_hangman.UNE_ERREUR:
                if self.aller:
                    self.bouger_hache_relative_a((460, 145))
                else:
                    self.bouger_hache_relative_a(hang_constantes.hache_position_pivot_init)
            case etat_hangman.DEUX_ERREURS:
                if self.aller:
                    self.bouger_hache_relative_a((345, 145))
                else:
                    self.bouger_hache_relative_a(hang_constantes.hache_position_pivot_init)
            case etat_hangman.TROIS_ERREURS:
                if self.aller:
                    self.bouger_hache_relative_a((450, 270))
                else:
                    self.bouger_hache_relative_a(hang_constantes.hache_position_pivot_init)
            case etat_hangman.QUATRE_ERREURS:
                if self.aller:
                    self.bouger_hache_relative_a((380, 270))
                else:
                    self.bouger_hache_relative_a(hang_constantes.hache_position_pivot_init)
            case etat_hangman.CINQ_ERREURS:
                if self.aller:
                    self.bouger_hache_relative_a((400, 150))
                else:
                    self.bouger_hache_relative_a((hang_constantes.hache_position_pivot_init))
            case etat_hangman.SIX_ERREURS:
                if self.aller:
                    self.bouger_hache_relative_a((405, 195))
                else:
                    self.bouger_hache_relative_a((hang_constantes.hache_position_pivot_init))
            case __:
                self.hache.angle +=1
    
    def bouger_hache_relative_a(self, coordonner_souhaiter):
            x_souhaiter = int(coordonner_souhaiter[0])
            x_actuel = self.hache.emplacement_pivot.x
            if x_actuel > x_souhaiter:
                self.hache.emplacement_pivot -= pygame.math.Vector2(10, 0)
                
            elif x_actuel < x_souhaiter:
                self.hache.emplacement_pivot += pygame.math.Vector2(10, 0)
            else:
                self.aller = not self.aller # Attention quand utilisateur nattendera pas pour taper et le retour que barbie fera