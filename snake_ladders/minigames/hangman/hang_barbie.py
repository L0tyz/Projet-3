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

        self.debug = True

        self.parts.add(self.hache, self.tronc, self.bras_droit, self.bras_gauche)

        self.etat = None
        self.aller = True
        self.retour = True

    """
    Entrées: self, etat
    Sorties: Aucune
    But: Mettre a jour les parametres des parties de barbie en fonction de letat
    """
    # NOTE:Attention quand utilisateur nattendera pas pour taper et le retour que barbie fera
    def mettre_a_jour(self, etat):
        if not etat is self.etat:
            self.aller = True
            self.retour = True
            self.etat = etat

        match etat: # Translation de barbie en fonction de l'état
            case etat_hangman.AUCUN_ECHEC:
                pass
                #self.mettre_barbie_immobile()
            case etat_hangman.UNE_ERREUR:
                self.etat_emplacement(x_finale=200, angle_hache=45)
            case etat_hangman.DEUX_ERREURS:
                self.etat_emplacement(x_finale=190, angle_hache=-95)
            case etat_hangman.TROIS_ERREURS:
                self.etat_emplacement(x_finale=220, angle_hache=-60)
            case etat_hangman.QUATRE_ERREURS:
                self.etat_emplacement(x_finale=260, angle_hache=-60)
            case etat_hangman.CINQ_ERREURS:
                self.etat_emplacement(x_finale=260, angle_hache=45)
            case etat_hangman.SIX_ERREURS:
                self.etat_emplacement(x_finale=400, angle_hache=60)
            case __:
                self.mettre_barbie_immobile()
        self.parts.update()

    
    """
    Entrées: self, ecran
    Sorties: Aucune
    But: Dessiner barbie a lecran
    """
    def dessiner(self, ecran):
        self.parts.draw(ecran)
        if self.debug:
            for part in self.parts:
                pygame.draw.circle(ecran, (255, 0, 0), part.emplacement_pivot, 10)
                pygame.draw.line(ecran, (0, 0, 255), part.emplacement_pivot, part.rect.center, 10)
        

    """
    Entrées: self, x_finale, angle_hache
    Sorties: Aucune
    But: Tourner et deplacer barbie en fonction de son emplacement voulu, de linclinaison de la hache et de la situation du programme
    """
    def etat_emplacement(self, x_finale, angle_hache):
        if self.aller: # elif essentielle vu que ne veut pas les deux
            self.bouger_barbie_x(x_finale, True)
            self.angler_hache(angle_hache)
        elif self.retour:
            self.bouger_barbie_x((hang_constantes.barbie_tronc_position_pivot_init[0]), False)
        else:
            pass

    """
    Entrées: self, angle_souhaiter
    Sorties: Aucune
    But: Incliner lhache en fonction de linclinaison voulu(angle_souhaiter)
    """
    def angler_hache(self, angle_souhaiter):
            if self.hache.angle > angle_souhaiter:
                self.hache.angle -= min(5, self.hache.angle - angle_souhaiter) # Limiter le ghosting
            elif self.hache.angle < angle_souhaiter:
                self.hache.angle += min(5, angle_souhaiter - self.hache.angle)
            else:
                self.hache.angle = angle_souhaiter

    """
    Entrées: self, x_finale, aller
    Sorties: Aucune
    But: Deplacer toutes les parties de barbie en fonction de la position voulu
    """
    def bouger_barbie_x(self, x_finale, aller):
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
            if aller:
                self.aller = not self.aller
            else:
                self.retour = not self.retour
