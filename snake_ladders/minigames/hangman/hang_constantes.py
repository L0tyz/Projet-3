import os
from enum import Enum


class hang_constantes:
    #===================== Ecran =====================#
    entete = str("Hangman")
    largeur_ecran = int(1000)
    hauteur_ecran = int(800)

    #===================== Couleurs =====================#
    rgb_blanc = (255, 255, 255) 
    rgb_bleu = (0, 200, 255)
    rgba_bleu = (0, 200, 255, 22)
    rgb_rouge = (255, 0, 0)
    rgba_rouge = (255, 0, 0, 22)
    rgb_noir = (0, 0, 0)
    couleur_fond_ecran = (0, 0, 0, 0)

    #===================== Nom fichier images =====================#
    emplacement_actuel = os.path.dirname(os.path.abspath(__file__))
    emplacement_assets = os.path.join(emplacement_actuel, "Assets")

    ### Not used for now, but may be used later ###
    barbie_hache = os.path.join(emplacement_assets, "BarbieHache.png")
    barbie_marteau = os.path.join(emplacement_assets, "BarbieMarteau.png")
    barbie_tt_seule = os.path.join(emplacement_assets, "BarbieTTSeule.png")

    barbie_bras_droit = os.path.join(emplacement_assets, "Barbie_Bras_Droit.png")
    barbie_bras_gauche = os.path.join(emplacement_assets, "Barbie_Bras_Gauche.png")
    barbie_tronc = os.path.join(emplacement_assets, "Barbie_Tronc.png")

    hache = os.path.join(emplacement_assets, "hache.png")
    hammer = os.path.join(emplacement_assets, "hammer.png")

    ken_bras_droit = os.path.join(emplacement_assets, "Ken_Bras_Droit.png")
    ken_bras_gauche = os.path.join(emplacement_assets, "Ken_Bras_Gauche.png")
    ken_jambe_droite = os.path.join(emplacement_assets, "Ken_Jambe_Droite.png")
    ken_jambe_gauche = os.path.join(emplacement_assets, "Ken_Jambe_Gauche.png")
    ken_tete = os.path.join(emplacement_assets, "Ken_Tete.png")
    ken_torse = os.path.join(emplacement_assets, "Ken_Torse.png")

    #===================== Constantes de barbie =====================#
    barbie_scale = (60, 60) # largeur, grandeur
    barbie_tronc_scale = (150, 150)
    hache_scale_tuple = (70, 70)
    ### Emplacement des jointures de barbie par rapport au centre de cette partie ###
    barbie_bras_droit_pivot_centre = (30, 30) # x,y
    barbie_bras_gauche_pivot_centre = (-30, 30)
    barbie_tronc_pivot_centre = (0, 0)
    hache_pivot_centre = (45, -45)
    ### Emplacement des jointures de barbie ###
    barbie_bras_droit_position_pivot_init = (100, 190)
    barbie_bras_gauche_position_pivot_init = (145, 190)
    barbie_tronc_position_pivot_init = (120, 220)
    hache_position_pivot_init = (120, 220)

    #===================== Constantes de Ken =====================#
    ken_scale = (80, 80) # largeur, grandeur
    ken_torse_scale = (125, 125)
    ken_bras_scale = (60, 60)
    ken_jambes_scale = (40, 40)
    ### Emplacement des jointures de ken par rapport au centre de sa partie ###
    ken_bras_droit_pivot_centre = (30, 30)
    ken_bras_gauche_pivot_centre = (-30, 30)
    ken_jambe_droite_pivot_centre = (0, 0)
    ken_jambe_gauche_pivot_centre = (0, 0)
    ken_tete_pivot_centre = (0, -40)
    ken_torse_pivot_centre = (0, 0)
    ### Emplacement des jointures de ken ###
    ken_bras_droit_position_pivot_init = (460, 145) 
    ken_bras_gauche_position_pivot_init = (345, 145)
    ken_jambe_droite_position_pivot_init = (450, 270)
    ken_jambe_gauche_position_pivot_init = (380, 270)
    ken_tete_position_pivot_init = (400, 150)
    ken_torse_position_pivot_init = (405, 195)

class etat_hangman(Enum):
    # Can acces: etat_jeu.MENU, etat_jeu.JEU, etat_jeu.FIN
    # etat_jeu(1)
    # possible .name et .value
    AUCUN_ECHEC = 0
    UNE_ERREUR = 1
    DEUX_ERREURS = 2
    TROIS_ERREURS = 3
    QUATRE_ERREURS = 4
    CINQ_ERREURS = 5
    SIX_ERREURS = 6

