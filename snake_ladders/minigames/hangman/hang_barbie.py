"""
    Realisé par Cassey Martin
    But: Créer et contrôler les membres de la barbie pour le mini jeu hangmanan
"""
import pygame
from hang_partie import partie
from hang_constantes import hang_constantes
from hang_constantes import etat_hangman
class barbie:
    """
    Entrées: self
    Sorties: Aucune (None par défaut, ce que python s'attend)
    But: Créer un objet barbie comme partie de group sprite parts
    """
    def __init__(self):
        self.parts = pygame.sprite.Group()

        self.hache = partie(hang_constantes.hache, hang_constantes.hache_scale_tuple, hang_constantes.hache_pivot_centre, hang_constantes.hache_position_pivot_init)
        self.tronc = partie(hang_constantes.barbie_tronc, hang_constantes.barbie_tronc_scale, hang_constantes.barbie_tronc_pivot_centre, hang_constantes.barbie_tronc_position_pivot_init)
        self.bras_droit = partie(hang_constantes.barbie_bras_droit, hang_constantes.barbie_scale, hang_constantes.barbie_bras_droit_pivot_centre, hang_constantes.barbie_bras_droit_position_pivot_init)
        self.bras_gauche = partie(hang_constantes.barbie_bras_gauche, hang_constantes.barbie_scale, hang_constantes.barbie_bras_gauche_pivot_centre, hang_constantes.barbie_bras_gauche_position_pivot_init)

        self.debug = False

        self.parts.add(self.hache, self.tronc, self.bras_droit, self.bras_gauche)

        self.etat = etat_hangman.AUCUN_ECHEC
        self.aller = False
        self.end = False

    """
    Entrées: self, etat
    Sorties: Boolean représentant si le jeu roule encore
    But: Mettre à jour les parametres des parties de barbie en fonction de l'etat
    """
    def mettre_a_jour(self, etat):
        if not etat is self.etat:
            self.aller = True
            self.etat = etat

        ### Déplacement de barbie et inclinaison de son hache en fonction de l'état ###
        if self.aller:
            x_finale = self.x_finale()
            angle_souhaiter_hache = self.angle_souhaiter_hache()
            ### Angler adequatement hache ###
            if self.hache.angle > angle_souhaiter_hache:
                self.hache.angle -= min(5, self.hache.angle - angle_souhaiter_hache) # Limiter le ghosting
            elif self.hache.angle < angle_souhaiter_hache:
                self.hache.angle += min(5, angle_souhaiter_hache - self.hache.angle)
            else:
                self.hache.angle = angle_souhaiter_hache
            ### Bouger barbie ###
            x_actuel = int(self.tronc.emplacement_pivot.x)
            vecteur_commun = pygame.math.Vector2(1, 0)
            if x_actuel > x_finale:
                self.hache.emplacement_pivot -= vecteur_commun
                self.tronc.emplacement_pivot -= vecteur_commun
                self.bras_droit.emplacement_pivot -= vecteur_commun
                self.bras_gauche.emplacement_pivot -= vecteur_commun
            elif x_actuel < x_finale:
                self.hache.emplacement_pivot += vecteur_commun
                self.tronc.emplacement_pivot += vecteur_commun
                self.bras_droit.emplacement_pivot += vecteur_commun
                self.bras_gauche.emplacement_pivot += vecteur_commun
            else:
                if self.aller: # Seulement mettre a False lorsque vrai
                    self.aller = not self.aller
        else:
            ### Bouger barbie ###
            x_actuel = int(self.tronc.emplacement_pivot.x)
            x_finale = hang_constantes.barbie_tronc_position_pivot_init[0]
            vecteur_commun = pygame.math.Vector2(1, 0)
            if x_actuel > x_finale:
                self.hache.emplacement_pivot -= vecteur_commun
                self.tronc.emplacement_pivot -= vecteur_commun
                self.bras_droit.emplacement_pivot -= vecteur_commun
                self.bras_gauche.emplacement_pivot -= vecteur_commun
            elif x_actuel < x_finale:
                self.hache.emplacement_pivot += vecteur_commun
                self.tronc.emplacement_pivot += vecteur_commun
                self.bras_droit.emplacement_pivot += vecteur_commun
                self.bras_gauche.emplacement_pivot += vecteur_commun
            else:
                pass

        self.end = bool(self.hache.angle == 60 and 
                    self.tronc.emplacement_pivot == hang_constantes.barbie_tronc_position_pivot_init and 
                    etat == etat_hangman.SIX_ERREURS) # Mettre a jour self.end

        self.parts.update()
        return not self.end

    """
    Entrées: self, ecran
    Sorties: Listes des parties dessiner de barbie
    But: Dessiner barbie à l'écran
    """
    def dessiner(self, ecran):
        if self.debug:
            for part in self.parts:
                pygame.draw.circle(ecran, (255, 0, 0), part.emplacement_pivot, 10)
                pygame.draw.line(ecran, (0, 0, 255), part.emplacement_pivot, part.rect.center, 10)
        return self.parts.draw(ecran)

    """
    Entrées: self
    Sorties: int représentant l'angle souhaiter de la hache
    But: Chercher l'angle souhaiter de la hache en fonciton de l'état de barbie
    """
    def angle_souhaiter_hache(self):
        match self.etat:
            case etat_hangman.AUCUN_ECHEC:
                return self.hache.angle
            case etat_hangman.UNE_ERREUR:
                return 45
            case etat_hangman.DEUX_ERREURS:
                return 45
            case etat_hangman.TROIS_ERREURS:
                return -60
            case etat_hangman.QUATRE_ERREURS:
                return -60
            case etat_hangman.CINQ_ERREURS:
                return 45
            case etat_hangman.SIX_ERREURS:
                return 60
            case __:
                return self.hache.angle

    """
    Entrées: self
    Sorties: int représentant l'emplacement souhaiter de barbie
    But: Chercher l'emplacement souhaiter de la barbie en fonciton de son état
    """
    def x_finale(self):
        match self.etat:
            case etat_hangman.AUCUN_ECHEC:
                return self.tronc.emplacement_pivot.x
            case etat_hangman.UNE_ERREUR:
                return 200
            case etat_hangman.DEUX_ERREURS:
                return 220
            case etat_hangman.TROIS_ERREURS:
                return 240
            case etat_hangman.QUATRE_ERREURS:
                return 280
            case etat_hangman.CINQ_ERREURS:
                return 300
            case etat_hangman.SIX_ERREURS:
                return 400
            case __:
                return self.tronc.emplacement_pivot.x