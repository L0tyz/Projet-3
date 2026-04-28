import pygame

class interfaceTicTacToe:    
    
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()

        # Dimenssion de la grille
        self.largeur = 800
        self.hauteur = 800
        self.nombre_colonnes = 3
        self.nombre_lignes = 3

        # Taille de chaque case
        self.taille_case = self.largeur // self.nombre_colonnes

        # couleurs
        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)
        self.rouge = (255, 0, 0)
        self.vert = (0, 255, 0)
        self.bleu = (0, 0, 255)

        # Création de la fenêtre
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("tic tac toe") 
        self.horloge = pygame.time.Clock()

        # joueur
        self.joueur = "X"
        self.fin_jeu = False
        self.gagnant = None
        self.compteur_animation = 0

        # Grille logique
        self.grille = [  
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def dessiner_grille(self):
        """Fonction pour dessiner la grille"""
        for axe_x in range(0, self.largeur, self.taille_case):
            pygame.draw.line(self.ecran, self.noir, (axe_x, 0), (axe_x, self.hauteur), 2)

        for axe_y in range(0, self.hauteur, self.taille_case):
            pygame.draw.line(self.ecran, self.noir, (0, axe_y), (self.largeur, axe_y), 2)  

    def dessiner_symboles(self):
        """Fonction pour dessiner les symboles"""
        for ligne in range(self.nombre_lignes):
            for colonne in range(self.nombre_colonnes):

                x = colonne * self.taille_case
                y = ligne * self.taille_case

                if self.grille[ligne][colonne] == "X":
                    pygame.draw.line(self.ecran, self.noir, (x + 20, y + 20), (x + self.taille_case - 20, y + self.taille_case - 20), 2)
                    pygame.draw.line(self.ecran, self.noir, (x + self.taille_case - 20, y + 20), (x + 20, y + self.taille_case - 20), 2)
                elif self.grille[ligne][colonne] == "O":
                    pygame.draw.circle(self.ecran, self.noir, (x + self.taille_case // 2, y + self.taille_case // 2), self.taille_case // 2 - 20, 2)

    def verifier_gagnant(self):
        """Fonction pour vérifier s'il y a un gagnant"""
        # Vérifier les lignes
        for ligne in self.grille:
            if ligne[0] == ligne[1] == ligne[2] != "":
                return ligne[0]
        
        # Vérifier les colonnes
        for colonne in range(self.nombre_colonnes):
            if self.grille[0][colonne] == self.grille[1][colonne] == self.grille[2][colonne] != "":
                return self.grille[0][colonne]
        
        # Vérifier les diagonales
        if self.grille[0][0] == self.grille[1][1] == self.grille[2][2] != "":
            return self.grille[0][0]
        
        if self.grille[0][2] == self.grille[1][1] == self.grille[2][0] != "":
            return self.grille[0][2]
        
        return None

    def verifier_egalite(self):
        """Fonction pour vérifier s'il y a une égalité"""
        for ligne in self.grille:
            for case in ligne:
                if case == "":
                    return False
        return True

    def afficher_gagnant(self):
        """Fonction pour afficher le message du gagnant avec animation"""
        police = pygame.font.Font(None, 100)
        
        if self.gagnant:
            texte = police.render(f"{self.gagnant} a gagné!", True, self.rouge if self.gagnant == "X" else self.bleu)
        else:
            texte = police.render("C'est une égalité!", True, self.noir)
        
        # Animation d'apparition et de disparition
        alpha = int(255 * abs((self.compteur_animation % 120 - 60) / 60))
        texte.set_alpha(alpha)
        
        rect_texte = texte.get_rect(center=(self.largeur // 2, self.hauteur // 2))
        self.ecran.blit(texte, rect_texte)
        
        self.compteur_animation += 1

    def run(self):
        """Boucle principale du jeu"""
        en_cours = True             
        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.fin_jeu:
                    x, y = event.pos
                    colonne = x // self.taille_case
                    ligne = y // self.taille_case

                    if self.grille[ligne][colonne] == "":
                        self.grille[ligne][colonne] = self.joueur
                        
                        # Vérifier s'il y a un gagnant
                        gagnant_temporaire = self.verifier_gagnant()
                        if gagnant_temporaire:
                            self.fin_jeu = True
                            self.gagnant = gagnant_temporaire
                        elif self.verifier_egalite():
                            self.fin_jeu = True
                            self.gagnant = None
                        else:
                            self.joueur = "O" if self.joueur == "X" else "X"
            
            self.ecran.fill(self.blanc)
            self.dessiner_grille()   
            self.dessiner_symboles()
            
            # Afficher le message du gagnant si le jeu est terminé
            if self.fin_jeu:
                self.afficher_gagnant()
            
            pygame.display.flip()   
            self.horloge.tick(60)    
        pygame.quit()


if __name__ == "__main__":
    jeu = interfaceTicTacToe()
    jeu.run()       

