import pygame

# Initialisation de Pygame
pygame.init()

#Dimenssion de la grille
largeur = 800
hauteur = 800
nombre_colonnes = 3
nombre_lignes = 3

#Taille de chaque case
taille_case = largeur // nombre_colonnes

#couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

#Création de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Morpion")#Horloge pour contrôler le taux de rafraîchissement    
horloge = pygame.time.Clock()

#joueur
joueur = "X"


#Grille logique
grille = [  
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
#Fonction pour dessiner la grille
def dessiner_grille():
    for axe_x in range(0, largeur, taille_case):
        pygame.draw.line(ecran, noir, (axe_x, 0), (axe_x, hauteur), 2)

    for axe_y in range(0, hauteur, taille_case):
        pygame.draw.line(ecran, noir, (0, axe_y), (largeur, axe_y), 2)  
#Fonction pour dessiner les symboles
def dessiner_symboles():
    for ligne in range(nombre_lignes):
        for colonne in range(nombre_colonnes):

            x = colonne * taille_case
            y = ligne * taille_case

            if grille[ligne][colonne] == "X":
                pygame.draw.line(ecran, noir, (x + 20, y + 20), (x + taille_case - 20, y + taille_case - 20), 2)
                pygame.draw.line(ecran, noir, (x + taille_case - 20, y + 20), (x + 20, y + taille_case - 20), 2)
            elif grille[ligne][colonne] == "O":
                pygame.draw.circle(ecran, noir, (x + taille_case // 2, y + taille_case // 2), taille_case // 2 - 20, 2)

#Boucle principale du jeu
en_cours = True             
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            colonne = x // taille_case
            ligne = y // taille_case

            if grille[ligne][colonne] == "":
                grille[ligne][colonne] = joueur
                joueur = "O" if joueur  == "X" else "X"
    ecran.fill(blanc)
    dessiner_grille()   
    dessiner_symboles()
    pygame.display.flip()   
    horloge.tick(60)    
pygame.quit()       

