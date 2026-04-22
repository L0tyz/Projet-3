import os


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
    blanc_tolerance = 245

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
    barbie_scale = (100, 100) # largeur, grandeur
    hache_scale_tuple = (100, 100)
    hache_scale = 100 
    hammer_scale = 100
    ### Emplacement des jointures de barbie par rapport au centre de cette partie ###
    barbie_bras_droit_pivot_centre = (10, 10) # x,y
    barbie_bras_gauche_pivot_centre = (10, 10)
    barbie_tronc_pivot_centre = (0, 0)
    hache_pivot_centre = (0, 0)
    ### Emplacement des jointures de barbie ###
    barbie_bras_droit_position_pivot_init = (0, 10)
    barbie_bras_gauche_position_pivot_init = (200, 10)
    barbie_tronc_position_pivot_init = (100, 10)
    hache_position_pivot_init = (0, 100)

    #===================== Constantes de Ken =====================#
    ken_scale = (100, 100) # largeur, grandeur
    ### Emplacement des jointures de ken par rapport au centre de sa partie ###
    ken_bras_droit_pivot_centre = (-10, 10)
    ken_bras_gauche_pivot_centre = (10, 10)
    ken_jambe_droite_pivot_centre = (0, -10)
    ken_jambe_gauche_pivot_centre = (0, -10)
    ken_tete_pivot_centre = (0, 10)
    ken_torse_pivot_centre = (0, 0)
    ### Emplacement des jointures de ken ###
    ken_bras_droit_position_pivot_init = (500, 100) 
    ken_bras_gauche_position_pivot_init = (500, 100)
    ken_jambe_droite_position_pivot_init = (700, -100)
    ken_jambe_gauche_position_pivot_init = (700, -10)
    ken_tete_position_pivot_init = (400, 100)
    ken_torse_position_pivot_init = (200, 100)


