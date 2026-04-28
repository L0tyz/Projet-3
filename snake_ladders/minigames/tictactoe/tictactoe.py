import pygame
import random


# =========================
# INITIALISATION
# =========================
"""
But : Initialisation de Pygame et definir les parametres de la fenetre, les couleurs, la grille logique et les variables de jeu.
"""
def initialiser_jeu():  
    global largeur, hauteur, nombre_colonnes, nombre_lignes, taille_case
    global blanc, noir, rouge, bleu
    global ecran, horloge
    
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

def faire_coup(joueur, ligne, colonne):
    if grille[ligne][colonne] == ' ':
      grille[ligne][colonne] = joueur
      return True
    return False

"""
Entrées: joueur (joueur actuel)
Sorties: Le joueur suivant ('X' ou 'O')
But: Alterner entre les deux joueurs
"""
def changer_joueur( joueur):
    if joueur == 'X':
        return 'O'
    else:
        return 'X'

"""
Entrées: aucune (utilise grille)
Sorties: Tuple (gagnant, perdant) ou None
But: Vérifier s'il y a un gagnant dans la grille
"""
def verifier_gagnant():
    plateau = grille
    
    # Vérification des lignes
    for ligne in plateau:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != ' ':
            gagnant = ligne[0]
            perdant = 'O' if gagnant == 'X' else 'X'
            return gagnant, perdant

    # Vérification des colonnes
    for col in range(3):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] and plateau[0][col] != ' ':
            gagnant = plateau[0][col]
            perdant = 'O' if gagnant == 'X' else 'X'
            return gagnant, perdant

    # Vérification des diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] and plateau[0][0] != ' ':
        gagnant = plateau[0][0]
        perdant = 'O' if gagnant == 'X' else 'X'
        return gagnant, perdant

    if plateau[0][2] == plateau[1][1] == plateau[2][0] and plateau[0][2] != ' ':
        gagnant = plateau[0][2]
        perdant = 'O' if gagnant == 'X' else 'X'
        return gagnant, perdant
    
    return None

"""
Entrées: aucune (utilise grille)
Sorties: True si égalité, sinon False
But: Vérifier si toutes les cases sont remplies sans gagnant
"""
def verifier_egalite():
    return all(cellule != ' ' for ligne in grille for cellule in ligne)

"""
Entrées: aucune (utilise grille)
Sorties: (ligne, colonne) d'un coup valide ou None
But: Choisir aléatoirement une case vide pour l'ordinateur.
"""
def choisir_coup_aleatoire():
     coups_libres = [(l, c) for l in range(3) for c in range(3) if grille[l][c] == ' ']
     return random.choice(coups_libres) if coups_libres else None

# =========================
# DESSIN DE LA GRILLE
# =========================
def dessiner_grille():
    global largeur, hauteur, taille_case, ecran, noir
    for axe_x in range(0, largeur, taille_case):
        pygame.draw.line(ecran, noir, (axe_x, 0), (axe_x, hauteur), 2)

    for axe_y in range(0, hauteur, taille_case):
        pygame.draw.line(ecran, noir, (0, axe_y), (largeur, axe_y), 2)

# =========================
# DESSIN DES SYMBOLES
# =========================
def dessiner_symboles():
    global nombre_lignes, nombre_colonnes, taille_case, grille, ecran, noir
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
    global largeur, hauteur, rouge, bleu, noir, compteur_animation, ecran
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

# =========================
# BOUCLE PRINCIPALE
# =========================
def jouer():
    """
    But: Gérer les événements, la logique du jeu et l'affichage en continu
    """
    global joueur_actuel, game_over, gagnant, compteur_animation, resultat_jeu
    global largeur, hauteur, taille_case, ecran, horloge, blanc, noir, grille
    
    initialiser_jeu()
    
    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False

            # Gestion du clic souris
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and joueur_actuel == 'X':
                x_souris, y_souris = pygame.mouse.get_pos()
                colonne = x_souris // taille_case
                ligne = y_souris // taille_case

                if faire_coup(joueur_actuel, ligne, colonne):
                    # Vérifier s'il y a un gagnant
                    resultat = verifier_gagnant()
                    if resultat:
                        game_over = True
                        gagnant = resultat[0]
                        resultat_jeu = f"{gagnant} gagnant"
                    elif verifier_egalite():
                        game_over = True
                        gagnant = None
                        resultat_jeu = "egalite"
                    else:
                        joueur_actuel = changer_joueur(joueur_actuel)

        # Si c'est le tour de l'ordinateur, jouer automatiquement
        if not game_over and joueur_actuel == 'O':
            coup = choisir_coup_aleatoire()
            if coup:
                ligne, colonne = coup
                faire_coup(joueur_actuel, ligne, colonne)
                resultat = verifier_gagnant()
                if resultat:
                    game_over = True
                    gagnant = resultat[0]
                    resultat_jeu = f"{gagnant} gagnant"
                elif verifier_egalite():
                    game_over = True
                    gagnant = None
                    resultat_jeu = "egalite"
                else:
                    joueur_actuel = changer_joueur(joueur_actuel)

        # Affichage
        ecran.fill(blanc)
        dessiner_grille()
        dessiner_symboles()

        # Afficher le message du gagnant si le jeu est terminé
        if game_over:
            afficher_gagnant(gagnant)
            compteur_animation += 1

        pygame.display.flip()
        horloge.tick(30)

    pygame.quit()

# Lancer le jeu
if __name__ == "__main__":
    jouer()
        

