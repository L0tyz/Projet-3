import pygame
import random
#initialiser pygame et créer la fenêtre de jeu
pygame.init()
ecran = pygame.display.set_mode((600, 800))
horloge = pygame.time.Clock()
victoire = False
defaite = False


def creer_grille_couleur(rangs, colonnes, palette=None):
    """Return a rows x cols 2D list of RGB tuples.

    If palette is provided, choose colours from it; otherwise generate random
    bright-ish colours.
    """
    grille = []
    for r in range(rangs):
        rang = []
        for c in range(colonnes):
            if palette:
                couleur = random.choice(palette)
            else:
                # Generate a random bright colour (avoid too dark)
                couleur = (
                    random.randint(80, 255),
                    random.randint(80, 255),
                    random.randint(80, 255),
                )
            rang.append(couleur)
        grille.append(rang)
    return grille


def creer_rectangles_grille(surface, rangs, colonnes, grandeur_case, grille_couleur=None, couleur_contour=(200, 200, 200)):
    """Draw a grid of rectangles. If color_grid is provided it must be a 2D
    list of the same dimensions and will be used to fill each cell before
    drawing the outline."""
    for row in range(rangs):
        for col in range(colonnes):
            rect = pygame.Rect(col * grandeur_case, row * grandeur_case, grandeur_case, grandeur_case)
            if grille_couleur:
                try:
                    fill_color = grille_couleur[row][col]
                except Exception:
                    fill_color = (0, 0, 0)
                pygame.draw.rect(surface, fill_color, rect)  # filled
            # Draw the outline on top so grid lines remain visible
            pygame.draw.rect(surface, couleur_contour, rect, 1)


def remplir_region(grille, ligne_depart, colonne_depart, nouvelle_couleur):
    """Remplit la région contiguë (voisins 4-directionnels) de la case de
    départ avec `nouvelle_couleur`. Utilise une pile pour éviter la
    récursion profonde."""
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
    """Vérifie si toutes les cases de la grille ont la même couleur.
    Met à jour la variable globale `victoire`."""
    global victoire
    premiere_couleur = grille[0][0]
    for ligne in grille:
        for couleur in ligne:
            if couleur != premiere_couleur:
                victoire = False
                return
    victoire = True
    return


def main():
    rangs, colonnes, grandeur_case = 10, 10, 60
    # Palette with only five allowed colours: pink, orange, red, yellow, purple
    PALETTE = [
        (255, 105, 180),  # pink
        (255, 165, 0),    # orange
        (220, 20, 60),    # red
        (255, 215, 0),    # yellow
        (148, 0, 211),    # purple
    ]

    # Crée une grille initiale aléatoire
    grille_couleur = creer_grille_couleur(rangs, colonnes, palette=PALETTE)
    index_selectionne = 0  # index du bouton de palette sélectionné (par défaut 0)
    # Limite de clics sur la palette
    MAX_CLICS_PALETTE = 20
    clics_palette = 0
    defaite_locale = False

    # Compute button layout at bottom of the screen
    largeur_ecran, hauteur_ecran = ecran.get_size()
    y_zone_bas = rangs * grandeur_case
    hauteur_zone_bas = hauteur_ecran - y_zone_bas
    largeur_bouton, hauteur_bouton = 80, 80
    espacement = 20
    largeur_totale = len(PALETTE) * largeur_bouton + (len(PALETTE) - 1) * espacement
    x_depart = (largeur_ecran - largeur_totale) // 2
    y_bouton = y_zone_bas + (hauteur_zone_bas - hauteur_bouton) // 2
    # Pré-calcul des rectangles de boutons
    rects_boutons = []
    for i in range(len(PALETTE)):
        x = x_depart + i * (largeur_bouton + espacement)
        rects_boutons.append(pygame.Rect(x, y_bouton, largeur_bouton, hauteur_bouton))

    # Font for instructions
    try:
        police_ecriture = pygame.font.SysFont(None, 20)
    except Exception:
        police_ecriture = None

    running = True
    while running:
        verifier_condition_victoire(grille_couleur)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Press R to reshuffle the grid colours
                if event.key == pygame.K_r:
                    grille_couleur = creer_grille_couleur(rangs, colonnes, palette=PALETTE)
                    # Réinitialise l'état du jeu au redémarrage
                    clics_palette = 0
                    defaite_locale = False
                    index_selectionne = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click
                    mx, my = event.pos
                    # Check palette button clicks first
                    for i, rect in enumerate(rects_boutons):
                        if rect.collidepoint(mx, my):
                            # Si défaite, on ignore les clics (seulement R redémarre)
                            if defaite_locale:
                                break
                            index_selectionne = i
                            # Compte ce clic et vérifie la limite
                            clics_palette += 1
                            if clics_palette > MAX_CLICS_PALETTE:
                                defaite_locale = True
                                # Ne pas appliquer la couleur — afficher le popup
                                break
                            # Applique immédiatement la couleur sélectionnée à la
                            # région contiguë en bas à gauche.
                            remplir_region(grille_couleur, rangs - 1, 0, PALETTE[index_selectionne])
                            break
                    else:
                        # Si le clic n'était pas sur un bouton, vérifie la grille.
                        # L'utilisateur peut seulement peindre la case en bas à gauche.
                        if 0 <= mx < colonnes * grandeur_case and 0 <= my < rangs * grandeur_case:
                            col = mx // grandeur_case
                            row = my // grandeur_case
                            # Autorise seulement la case en bas à gauche
                            if row == rangs - 1 and col == 0:
                                remplir_region(grille_couleur, row, col, PALETTE[index_selectionne])

        # Efface l'écran chaque frame
        ecran.fill((0, 0, 0))

        # Dessine la grille colorée
        creer_rectangles_grille(ecran, rangs, colonnes, grandeur_case, grille_couleur=grille_couleur)

        # Dessine les boutons de la palette
        for i, rect in enumerate(rects_boutons):
            pygame.draw.rect(ecran, PALETTE[i], rect)
            # Contour
            couleur_contour = (255, 255, 255) if i == index_selectionne else (200, 200, 200)
            pygame.draw.rect(ecran, couleur_contour, rect, 3 if i == index_selectionne else 1)

        # Affiche le compteur de clics
        if police_ecriture:
            click_counter = police_ecriture.render(f'Clics palette : {clics_palette}/{MAX_CLICS_PALETTE}', True, (255, 255, 255))
            ecran.blit(click_counter, (10, 10))

        if victoire:
            # semi-transparent overlay
            overlay = pygame.Surface((largeur_ecran, hauteur_ecran), pygame.SRCALPHA)
            overlay.fill((255, 255, 255, 180))
            ecran.blit(overlay, (0, 0))
            if police_ecriture:
                win_text = police_ecriture.render('Vous avez gagné ! Appuyez sur R pour recommencer.', True, (0, 128, 0))
                tw, th = win_text.get_size()
                ecran.blit(win_text, ((largeur_ecran - tw) // 2, (hauteur_ecran - th) // 2))
        # Si défaite, affiche un popup
        if defaite_locale:
            overlay = pygame.Surface((largeur_ecran, hauteur_ecran), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            ecran.blit(overlay, (0, 0))
            if police_ecriture:
                lose_text = police_ecriture.render('Vous avez perdu ! Appuyez sur R pour recommencer.', True, (255, 0, 0))
                tw, th = lose_text.get_size()
                ecran.blit(lose_text, ((largeur_ecran - tw) // 2, (hauteur_ecran - th) // 2))

        # Affiche les instructions
        if police_ecriture:
            instructions = police_ecriture.render("Faites toute la grille d'une seule couleur ! Cliquez sur une couleur de la palette pour changer la couleur de la case en bas à gauche et conquérir le plateau !", True, (255, 255, 255))
            ecran.blit(instructions, (10, hauteur_ecran - 30))

        # logique de jeu & rendu ici (ajoutez l'interface utilisateur, le score, etc.)

        pygame.display.flip()  # Update screen
        horloge.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
