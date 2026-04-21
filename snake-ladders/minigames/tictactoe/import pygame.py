import pygame

# =========================
# INITIALISATION
# =========================
pygame.init()

# Dimensions
largeur = 800
hauteur = 800
nombre_colonnes = 3
nombre_lignes = 3

taille_case = largeur // nombre_colonnes

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Morpion")

horloge = pygame.time.Clock()

# =========================
# JOUEURS
# =========================
joueur_actuel = "X"

# =========================
# GRILLE LOGIQUE
# =========================
grille = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

# =========================
# DESSIN DE LA GRILLE
# =========================
def dessiner_grille():
    for axe_x in range(0, largeur, taille_case):
        pygame.draw.line(ecran, noir, (axe_x, 0), (axe_x, hauteur), 2)

    for axe_y in range(0, hauteur, taille_case):
        pygame.draw.line(ecran, noir, (0, axe_y), (largeur, axe_y), 2)

# =========================
# DESSIN DES SYMBOLES
# =========================
def dessiner_symboles():
    for ligne in range(nombre_lignes):
        for colonne in range(nombre_colonnes):

            x = colonne * taille_case
            y = ligne * taille_case

            if grille[ligne][colonne] == "X":
                pygame.draw.line(ecran, noir, (x+20, y+20), (x+taille_case-20, y+taille_case-20), 3)
                pygame.draw.line(ecran, noir, (x+taille_case-20, y+20), (x+20, y+taille_case-20), 3)

            elif grille[ligne][colonne] == "O":
                pygame.draw.circle(
                    ecran,
                    noir,
                    (x + taille_case//2, y + taille_case//2),
                    taille_case//2 - 20,
                    3
                )

# =========================
# BOUCLE PRINCIPALE
# =========================
en_cours = True

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        # Gestion du clic souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_souris, y_souris = pygame.mouse.get_pos()

            colonne = x_souris // taille_case
            ligne = y_souris // taille_case

            # Vérifie si la case est vide
            if grille[ligne][colonne] == "":
                grille[ligne][colonne] = joueur_actuel

                # Changer de joueur
                if joueur_actuel == "X":
                    joueur_actuel = "O"
                else:
                    joueur_actuel = "X"

    # Affichage
    ecran.fill(blanc)
    dessiner_grille()
    dessiner_symboles()

    pygame.display.flip()
    horloge.tick(60)

pygame.quit()