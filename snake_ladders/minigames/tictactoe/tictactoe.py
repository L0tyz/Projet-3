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
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# =========================
# FONCTIONS LOGIQUES
# =========================
def make_move(board, player, row, col):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            winner = row[0]
            loser = 'O' if winner == 'X' else 'X'
            return winner, loser
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            winner = board[0][col]
            loser = 'O' if winner == 'X' else 'X'
            return winner, loser
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        winner = board[0][0]
        loser = 'O' if winner == 'X' else 'X'
        return winner, loser
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        winner = board[0][2]
        loser = 'O' if winner == 'X' else 'X'
        return winner, loser
    
    return None

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

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
# BOUCLE PRINCIPALE
# =========================
en_cours = True
game_over = False

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        # Gestion du clic souris
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_souris, y_souris = pygame.mouse.get_pos()

            colonne = x_souris // taille_case
            ligne = y_souris // taille_case

            if make_move(grille, joueur_actuel, ligne, colonne):
                joueur_actuel = switch_player(joueur_actuel)

                # Vérifier si quelqu'un a gagné
                result = check_winner(grille)
                if result:
                    winner, loser = result
                    print(f"{winner} wins! {loser} loses.")
                    game_over = True
                elif check_draw(grille):
                    print("It's a draw!")
                    game_over = True

    # Affichage
    ecran.fill(blanc)
    dessiner_grille()
    dessiner_symboles()

    pygame.display.flip()
    horloge.tick(60)

pygame.quit()