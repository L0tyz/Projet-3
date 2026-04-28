import pygame
import random

# =========================
# INITIALISATION
# =========================
"""
But : Initialisation de Pygame et definir les parametres de la fenetre, les couleurs, la grille logique et les variables de jeu.
"""
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
rouge = (255, 0, 0)
bleu = (0, 0, 255)

# Fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Tic Tac Toe")

horloge = pygame.time.Clock()

# =========================
# JOUEURS
# =========================

"""
But : Initialiser les variables de jeu pour suivre le joueur actuel, l'état du jeu, le gagnant et le compteur d'animation.
"""
joueur_actuel = "X"
game_over = False
gagnant = None
compteur_animation = 0
resultat_jeu = None  # Contient "gagnant", "perdant" ou "egalite"

# =========================
# GRILLE LOGIQUE
# =========================
"""
But : Représente la grille du jeu sous forme de liste 2D
"""
grille = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# =========================
# FONCTIONS LOGIQUES
# =========================
"""
Entrées: board (grille), player (joueur), row (ligne), col (colonne)
Sorties: True si le coup est valide, sinon False
But: Placer un symbole dans la grille si la case est vide
"""
def make_move(board, player, row, col):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

"""
Entrées: player (joueur actuel)
Sorties: Le joueur suivant ('X' ou 'O')
But: Alterner entre les deux joueurs
"""
def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

"""
Entrées: board (grille)
Sorties: Tuple (gagnant, perdant) ou None
But: Vérifier s'il y a un gagnant dans la grille
"""
def check_winner(board):
    # verification des lignes
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            winner = row[0]
            loser = 'O' if winner == 'X' else 'X'
            return winner, loser
    
    # verification des colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            winner = board[0][col]
            loser = 'O' if winner == 'X' else 'X'
            return winner, loser
    
    # verification des diagonales   
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        winner = board[0][0]
        loser = 'O' if winner == 'X' else 'X'
        return winner, loser
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        winner = board[0][2]
        loser = 'O' if winner == 'X' else 'X'
        return winner, loser
    
    return None

"""
Entrées: board (grille)
Sorties: True si égalité, sinon False
But: Vérifier si toutes les cases sont remplies sans gagnant
"""
def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

"""
Entrées: board (grille)
Sorties: (ligne, colonne) d'un coup valide ou None
But: Choisir aléatoirement une case vide pour l'ordinateur.
"""
def choisir_coup_aleatoire(board):
    coups_libres = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(coups_libres) if coups_libres else None

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

            if grille[ligne][colonne] == 'X':
                pygame.draw.line(ecran, noir, (x+20, y+20), (x+taille_case-20, y+taille_case-20), 3)
                pygame.draw.line(ecran, noir, (x+taille_case-20, y+20), (x+20, y+taille_case-20), 3)

            elif grille[ligne][colonne] == 'O':
                pygame.draw.circle(
                    ecran,
                    noir,
                    (x + taille_case//2, y + taille_case//2),
                    taille_case//2 - 20,
                    3
                )

# =========================
# AFFICHER LE GAGNANT AVEC ANIMATION
# =========================
"""
Entrées: gagnant (str ou None)
Sorties: aucune
But: Afficher le message de fin avec une animation (clignotement)
"""
def afficher_gagnant(gagnant):
    global compteur_animation
    
    police = pygame.font.Font(None, 100)
    
    if gagnant:
        texte = police.render(f"{gagnant} a gagné!", True, rouge if gagnant == "X" else bleu)
    else:
        texte = police.render("C'est une égalité!", True, noir)
    
    # Animation d'apparition et de disparition
    alpha = int(255 * abs((compteur_animation % 120 - 60) / 60))
    texte.set_alpha(alpha)
    
    rect_texte = texte.get_rect(center=(largeur // 2, hauteur // 2))
    ecran.blit(texte, rect_texte)
    
    compteur_animation += 1

# =========================
# BOUCLE PRINCIPALE
# =========================
en_cours = True
"""
But: Gérer les événements, la logique du jeu et l'affichage en continu
"""
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        # Gestion du clic souris
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and joueur_actuel == 'X':
            x_souris, y_souris = pygame.mouse.get_pos()

            colonne = x_souris // taille_case
            ligne = y_souris // taille_case

            if make_move(grille, joueur_actuel, ligne, colonne):
                # Vérifier s'il y a un gagnant
                result = check_winner(grille)
                if result:
                    game_over = True
                    gagnant = result[0]
                    resultat_jeu = f"{gagnant} gagnant"
                elif check_draw(grille):
                    game_over = True
                    gagnant = None
                    resultat_jeu = "egalite"
                else:
                    joueur_actuel = switch_player(joueur_actuel)

    # Si c'est le tour de l'ordinateur, jouer automatiquement
    if not game_over and joueur_actuel == 'O':
        coup = choisir_coup_aleatoire(grille)
        if coup:
            ligne, colonne = coup
            make_move(grille, joueur_actuel, ligne, colonne)
            result = check_winner(grille)
            if result:
                game_over = True
                gagnant = result[0]
                resultat_jeu = f"{gagnant} gagnant"
            elif check_draw(grille):
                game_over = True
                gagnant = None
                resultat_jeu = "egalite"
            else:
                joueur_actuel = switch_player(joueur_actuel)
    
    # Affichage
    ecran.fill(blanc)
    dessiner_grille()
    dessiner_symboles()
    
    # Afficher le message du gagnant si le jeu est terminé
    if game_over:
        afficher_gagnant(gagnant)

    pygame.display.flip()
    horloge.tick(30)

pygame.quit()