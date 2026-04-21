import os
from pathlib import Path


class hang_constantes:
    ### Ecran ###
    entete = str("Hangman")
    largeur_ecran = int(1000)
    hauteur_ecran = int(800)

    ### Couleurs ###
    rgb_blanc = (255, 255, 255) 
    rgb_bleu = (0, 200, 255)
    rgba_bleu = (0, 200, 255, 22)
    rgb_rouge = (255, 0, 0)
    rgba_rouge = (255, 0, 0, 22)
    rgb_noir = (0, 0, 0) 

    ### Nom fichier images ###
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

    ### Constantes de barbie ###
    barbie_scale = (100, 100) # largeur, grandeur
    hache_scale_tuple = (100, 100)
    hache_scale = 100 
    hammer_scale = 100

    ### Constantes de Ken ###
    ken_grandeur = 100
    ken_largeur = 100

