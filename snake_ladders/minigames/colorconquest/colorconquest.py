"""
Rosemarie Dalton

Minijeu de conquête de couleur : une grille de cases colorées, où le joueur doit
remplir toute la grille d'une même couleur en cliquant sur des boutons de palette. 
Chaque clic sur un bouton de couleur change la couleur des cases connectées à la case en bas à gauche. 
Le joueur a un nombre limité de clics pour réussir, sinon il perd.
"""

import pygame
import random
#initialiser pygame et créer la fenêtre de jeu
if not pygame.get_init():
    pygame.init()
if pygame.display.get_surface() is None:
    ecran = pygame.display.set_mode((600, 800))
else:
    ecran = pygame.display.get_surface()
horloge = pygame.time.Clock()
victoire = False
defaite = False


def creer_grille_couleur(rangs, colonnes, palette=None):
    """Créer une grille de couleurs aléatoires ou issues d'une palette.

    But : construire une structure 2D représentant les couleurs des cases.

    Entrées :
      - rangs (int) : nombre de lignes de la grille.
      - colonnes (int) : nombre de colonnes de la grille.
      - palette (iterable[tuple[int,int,int]] | None) : si fourni, les couleurs
        sont choisies aléatoirement parmi cette palette; sinon on génère des
        couleurs vives aléatoires.

    Sortie :
      - list[list[tuple[int,int,int]]] : grille (liste de lignes) où chaque
        élément est un tuple RGB (0..255).
    """
    grille = []
    for r in range(rangs):
        rang = []
        for c in range(colonnes):
            if palette:
                couleur = random.choice(palette)
            else:
                # Génère une couleur aléatoire plutôt vive (évite les teintes trop sombres)
                couleur = (
                    random.randint(80, 255),
                    random.randint(80, 255),
                    random.randint(80, 255),
                )
            rang.append(couleur)
        grille.append(rang)
    return grille


def creer_rectangles_grille(
        surface,
        rangs, 
        colonnes, 
        grandeur_case, 
        grille_couleur=None, 
        couleur_contour=(200, 200, 200)):
    """Dessiner une grille de rectangles sur une surface Pygame.

    But : rendre visuellement la grille et remplir chaque case avec la couleur
    correspondante.

    Entrées :
      - surface (pygame.Surface) : surface cible pour le rendu.
      - rangs (int) : nombre de lignes.
      - colonnes (int) : nombre de colonnes.
      - grandeur_case (int) : taille en pixels d'une case carrée.
      - grille_couleur (list[list[tuple[int,int,int]]] | None) : grille de
        couleurs (mêmes dimensions que rangs x colonnes). Si None, les cases ne
        sont pas remplies avant le tracé du contour.
      - couleur_contour (tuple[int,int,int]) : couleur du contour des cases.

    Sortie : None (opération de rendu directement sur `surface`).
    """
    for row in range(rangs):
        for col in range(colonnes):
            rect = pygame.Rect(col * grandeur_case, row * grandeur_case, grandeur_case, grandeur_case)
            if grille_couleur:
                try:
                    fill_color = grille_couleur[row][col]
                except Exception:
                    fill_color = (0, 0, 0)
                pygame.draw.rect(surface, fill_color, rect)  # filled
            # Dessiner le contour par-dessus pour garder les lignes visibles
            pygame.draw.rect(surface, couleur_contour, rect, 1)


def remplir_region(grille, ligne_depart, colonne_depart, nouvelle_couleur):
    """Remplir une région connectée par flood‑fill (voisins 4‑directions).

    But : remplacer par ``nouvelle_couleur`` toutes les cases connectées (haut,
    bas, gauche, droite) qui ont la même couleur que la case de départ.

    Entrées :
      - grille (list[list[tuple[int,int,int]]]) : grille modifiable (mutée par la fonction).
      - ligne_depart (int) : index de la ligne de la case de départ (0‑based).
      - colonne_depart (int) : index de la colonne de la case de départ.
      - nouvelle_couleur (tuple[int,int,int]) : couleur RGB à appliquer.

    Sorties / effets : Aucun retour (None). La ``grille`` passée en argument est modifiée in‑place.
    """
    lignes = len(grille)
    colonnes = len(grille[0]) if lignes > 0 else 0
    ancienne_couleur = grille[ligne_depart][colonne_depart]
    if ancienne_couleur == nouvelle_couleur:
        return
    pile = [(ligne_depart, colonne_depart)]
    while pile:
        r, c = pile.pop()
        if grille[r][c] != ancienne_couleur:
            continue
        grille[r][c] = nouvelle_couleur
        # voisins : haut, bas, gauche, droite
        if r > 0:
            pile.append((r - 1, c))
        if r < lignes - 1:
            pile.append((r + 1, c))
        if c > 0:
            pile.append((r, c - 1))
        if c < colonnes - 1:
            pile.append((r, c + 1))
def verifier_condition_victoire(grille):
    """Vérifier si la grille est uniformément d'une seule couleur.

    But : parcourir la grille et déterminer si toutes les cases ont la même
    couleur. Met à jour la variable globale ``victoire`` (bool).

    Entrées :
      - grille (list[list[tuple[int,int,int]]]) : grille à tester.

    Sortie / effet : Aucun retour (None). Modifie la variable globale ``victoire`` (True/False).
    """
    global victoire
    premiere_couleur = grille[0][0]
    for ligne in grille:
        for couleur in ligne:
            if couleur != premiere_couleur:
                victoire = False
                return
    victoire = True
    return


# compat snakeladders
def run_minijeu(ecran):
    """Exécuter la boucle principale du mini‑jeu sur une surface Pygame.

    But : lancer le mini‑jeu Color Conquest en utilisant ``ecran`` comme surface
    de rendu et gérer les événements (clics, touches) jusqu'à la fin de la
    partie.

    Entrées :
      - ecran (pygame.Surface) : surface Pygame fournie par le jeu principal
        sur laquelle dessiner et lire les événements.

    Sortie :
      - bool : True si la partie se termine en victoire, False si défaite ou
        fermeture. (Le résultat est retourné au code appelant pour gérer les
        conséquences.)

    Effets secondaires : met à jour occasionnellement les variables globales
    ``victoire`` et ``defaite`` pendant l'exécution.
    """
    global victoire, defaite

    PALETTE_COULEURS = [
        (255, 105, 180),  # rose
        (255, 165, 0),    # orange
        (220, 20, 60),    # rouge
        (255, 215, 0),    # jaune
        (148, 0, 211),    # violet
    ]

    rangs, colonnes, grandeur_case = 10, 10, 60
    NB_MAX_CLICS_PALETTE = 20

    largeur_ecran, hauteur_ecran = ecran.get_size()
    y_zone_bas = rangs * grandeur_case
    hauteur_zone_bas = hauteur_ecran - y_zone_bas
    largeur_bouton, hauteur_bouton = 80, 80
    espacement = 20
    largeur_totale = len(PALETTE_COULEURS) * largeur_bouton + (len(PALETTE_COULEURS) - 1) * espacement
    x_depart = (largeur_ecran - largeur_totale) // 2
    y_bouton = y_zone_bas + (hauteur_zone_bas - hauteur_bouton) // 2

    rects_boutons = [
        pygame.Rect(x_depart + i * (largeur_bouton + espacement), y_bouton, largeur_bouton, hauteur_bouton)
        for i in range(len(PALETTE_COULEURS))
    ]

    police_ecriture = pygame.font.SysFont(None, 20)
    horloge_mini = pygame.time.Clock()

    grille_couleur = creer_grille_couleur(rangs, colonnes, palette=PALETTE_COULEURS)
    index_selectionne = 0
    clics_palette = 0
    defaite_locale = False
    victoire = False

    running = True
    resultat = False

    while running:
        verifier_condition_victoire(grille_couleur)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    grille_couleur = creer_grille_couleur(rangs, colonnes, palette=PALETTE_COULEURS)
                    clics_palette = 0
                    defaite_locale = False
                    index_selectionne = 0
                    victoire = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = event.pos
                    for i, rect in enumerate(rects_boutons):
                        if rect.collidepoint(mx, my):
                            if defaite_locale:
                                break
                            index_selectionne = i
                            clics_palette += 1
                            if clics_palette > NB_MAX_CLICS_PALETTE:
                                defaite_locale = True
                                break
                            # Appliquer automatiquement la couleur sélectionnée à la région
                            remplir_region(grille_couleur, rangs - 1, 0, PALETTE_COULEURS[index_selectionne])
                            break
                    else:
                        # Si le joueur clique manuellement sur la case en bas à gauche
                        if 0 <= mx < colonnes * grandeur_case and 0 <= my < rangs * grandeur_case:
                            col = mx // grandeur_case
                            row = my // grandeur_case
                            if row == rangs - 1 and col == 0:
                                remplir_region(grille_couleur, row, col, PALETTE_COULEURS[index_selectionne])

        # rendu
        ecran.fill((0, 0, 0))
        creer_rectangles_grille(ecran, rangs, colonnes, grandeur_case, grille_couleur=grille_couleur)

        for i, rect in enumerate(rects_boutons):
            pygame.draw.rect(ecran, PALETTE_COULEURS[i], rect)
            couleur_contour = (255, 255, 255) if i == index_selectionne else (200, 200, 200)
            pygame.draw.rect(ecran, couleur_contour, rect, 3 if i == index_selectionne else 1)

        surf_compteur = police_ecriture.render(f'Clics palette : {clics_palette}/{NB_MAX_CLICS_PALETTE}', True, (255, 255, 255))
        ecran.blit(surf_compteur, (10, 10))

        if victoire:
            superposition = pygame.Surface((largeur_ecran, hauteur_ecran), pygame.SRCALPHA)
            superposition.fill((255, 255, 255, 180))
            ecran.blit(superposition, (0, 0))
            texte_victoire = police_ecriture.render('Vous avez gagné ! +4 cases', True, (0, 128, 0))
            tw, th = texte_victoire.get_size()
            ecran.blit(texte_victoire, ((largeur_ecran - tw) // 2, (hauteur_ecran - th) // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            resultat = True
            running = False

        if defaite_locale:
            superposition = pygame.Surface((largeur_ecran, hauteur_ecran), pygame.SRCALPHA)
            superposition.fill((0, 0, 0, 180))
            ecran.blit(superposition, (0, 0))
            texte_defaite = police_ecriture.render('Vous avez perdu ! -4 cases', True, (255, 0, 0))
            tw, th = texte_defaite.get_size()
            ecran.blit(texte_defaite, ((largeur_ecran - tw) // 2, (hauteur_ecran - th) // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            resultat = False
            running = False

        instructions = police_ecriture.render("Faites toute la grille d'une seule couleur !", True, (255, 255, 255))
        ecran.blit(instructions, (10, hauteur_ecran - 30))

        pygame.display.flip()
        horloge_mini.tick(60)

    return resultat