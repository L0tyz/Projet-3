import pygame
import random

class TicTacToe:
    def __init__(self):
        # =========================
        # INITIALISATION
        # =========================
        """
        But : Initialisation de Pygame et definir les parametres de la fenetre, les couleurs, la grille logique et les variables de jeu.
        """
        pygame.init()

        # Dimensions
        self.largeur = 800
        self.hauteur = 800
        self.nombre_colonnes = 3
        self.nombre_lignes = 3

        self.taille_case = self.largeur // self.nombre_colonnes

        # Couleurs
        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)
        self.rouge = (255, 0, 0)
        self.bleu = (0, 0, 255)

        # Fenêtre
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Tic Tac Toe")

        self.horloge = pygame.time.Clock()

        # =========================
        # JOUEURS
        # =========================

        """
        But : Initialiser les variables de jeu pour suivre le joueur actuel, l'état du jeu, le gagnant et le compteur d'animation.
        """
        self.joueur_actuel = "X"
        self.game_over = False
        self.gagnant = None
        self.compteur_animation = 0
        self.resultat_jeu = None  # Contient "gagnant", "perdant" ou "egalite"

        # =========================
        # GRILLE LOGIQUE
        # =========================
        """
        But : Représente la grille du jeu sous forme de liste 2D
        """
        self.grille = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def faire_coup(self, joueur, ligne, colonne):
        if self.grille[ligne][colonne] == ' ':
            self.grille[ligne][colonne] = joueur
            return True
        return False

    """
    Entrées: joueur (joueur actuel)
    Sorties: Le joueur suivant ('X' ou 'O')
    But: Alterner entre les deux joueurs
    """
    def changer_joueur(self, joueur):
        if joueur == 'X':
            return 'O'
        else:
            return 'X'

    """
    Entrées: aucune (utilise self.grille)
    Sorties: Tuple (gagnant, perdant) ou None
    But: Vérifier s'il y a un gagnant dans la grille
    """
    def verifier_gagnant(self):
        plateau = self.grille
        # verification des lignes
        for ligne in plateau:
            if ligne[0] == ligne[1] == ligne[2] and ligne[0] != ' ':
                gagnant = ligne[0]
                perdant = 'O' if gagnant == 'X' else 'X'
                return gagnant, perdant
        
        # verification des colonnes
        for col in range(3):
            if plateau[0][col] == plateau[1][col] == plateau[2][col] and plateau[0][col] != ' ':
                gagnant = plateau[0][col]
                perdant = 'O' if gagnant == 'X' else 'X'
                return gagnant, perdant
        
        # verification des diagonales   
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
    Entrées: aucune (utilise self.grille)
    Sorties: True si égalité, sinon False
    But: Vérifier si toutes les cases sont remplies sans gagnant
    """
    def verifier_egalite(self):
        return all(cellule != ' ' for ligne in self.grille for cellule in ligne)

    """
    Entrées: aucune (utilise self.grille)
    Sorties: (ligne, colonne) d'un coup valide ou None
    But: Choisir aléatoirement une case vide pour l'ordinateur.
    """
    def choisir_coup_aleatoire(self):
        coups_libres = [(l, c) for l in range(3) for c in range(3) if self.grille[l][c] == ' ']
        return random.choice(coups_libres) if coups_libres else None

    # =========================
    # DESSIN DE LA GRILLE
    # =========================
    def dessiner_grille(self):
        for axe_x in range(0, self.largeur, self.taille_case):
            pygame.draw.line(self.ecran, self.noir, (axe_x, 0), (axe_x, self.hauteur), 2)

        for axe_y in range(0, self.hauteur, self.taille_case):
            pygame.draw.line(self.ecran, self.noir, (0, axe_y), (self.largeur, axe_y), 2)

    # =========================
    # DESSIN DES SYMBOLES
    # =========================
    def dessiner_symboles(self):
        for ligne in range(self.nombre_lignes):
            for colonne in range(self.nombre_colonnes):

                x = colonne * self.taille_case
                y = ligne * self.taille_case

                if self.grille[ligne][colonne] == 'X':
                    pygame.draw.line(self.ecran, self.noir, (x+20, y+20), (x+self.taille_case-20, y+self.taille_case-20), 3)
                    pygame.draw.line(self.ecran, self.noir, (x+self.taille_case-20, y+20), (x+20, y+self.taille_case-20), 3)

                elif self.grille[ligne][colonne] == 'O':
                    pygame.draw.circle(
                        self.ecran,
                        self.noir,
                        (x + self.taille_case//2, y + self.taille_case//2),
                        self.taille_case//2 - 20,
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
    def afficher_gagnant(self, gagnant):
        police = pygame.font.Font(None, 100)
        
        if gagnant:
            texte = police.render(f"{gagnant} a gagné!", True, self.rouge if gagnant == "X" else self.bleu)
        else:
            texte = police.render("C'est une égalité!", True, self.noir)
        
        # Animation d'apparition et de disparition
        alpha = int(255 * abs((self.compteur_animation % 120 - 60) / 60))
        texte.set_alpha(alpha)
        
        rect_texte = texte.get_rect(center=(self.largeur // 2, self.hauteur // 2))
        self.ecran.blit(texte, rect_texte)
        
        self.compteur_animation += 1

    # =========================
    # BOUCLE PRINCIPALE
    # =========================
    def jouer(self):
        en_cours = True
        """
        But: Gérer les événements, la logique du jeu et l'affichage en continu
        """
        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False

                # Gestion du clic souris
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over and self.joueur_actuel == 'X':
                    x_souris, y_souris = pygame.mouse.get_pos()

                    colonne = x_souris // self.taille_case
                    ligne = y_souris // self.taille_case

                    if self.faire_coup(self.joueur_actuel, ligne, colonne):
                        # Vérifier s'il y a un gagnant
                        resultat = self.verifier_gagnant()
                        if resultat:
                            self.game_over = True
                            self.gagnant = resultat[0]
                            self.resultat_jeu = f"{self.gagnant} gagnant"
                        elif self.verifier_egalite():
                            self.game_over = True
                            self.gagnant = None
                            self.resultat_jeu = "egalite"
                        else:
                            self.joueur_actuel = self.changer_joueur(self.joueur_actuel)

            # Si c'est le tour de l'ordinateur, jouer automatiquement
            if not self.game_over and self.joueur_actuel == 'O':
                coup = self.choisir_coup_aleatoire()
                if coup:
                    ligne, colonne = coup
                    self.faire_coup(self.joueur_actuel, ligne, colonne)
                    resultat = self.verifier_gagnant()
                    if resultat:
                        self.game_over = True
                        self.gagnant = resultat[0]
                        self.resultat_jeu = f"{self.gagnant} gagnant"
                    elif self.verifier_egalite():
                        self.game_over = True
                        self.gagnant = None
                        self.resultat_jeu = "egalite"
                    else:
                        self.joueur_actuel = self.changer_joueur(self.joueur_actuel)
            
            # Affichage
            self.ecran.fill(self.blanc)
            self.dessiner_grille()
            self.dessiner_symboles()
            
            # Afficher le message du gagnant si le jeu est terminé
            if self.game_over:
                self.afficher_gagnant(self.gagnant)

            pygame.display.flip()
            self.horloge.tick(30)

        pygame.quit()
        return self.gagnant  # Return winner or None for draw

if __name__ == "__main__":
    jeu = TicTacToe()
    resultat = jeu.jouer()
    print(f"Résultat du jeu: {resultat}")