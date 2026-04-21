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
rouge = (255, 0, 0)
vert = (0, 255, 0)
bleu = (0, 0, 255)

#Création de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("tic tac toe") 
horloge = pygame.time.Clock()

#joueur
joueur = "X"
fin_jeu = False
gagnant = None
compteur_animation = 0


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

#Fonction pour vérifier s'il y a un gagnant
def verifier_gagnant():
    # Vérifier les lignes
    for ligne in grille:
        if ligne[0] == ligne[1] == ligne[2] != "":
            return ligne[0]
    
    # Vérifier les colonnes
    for colonne in range(nombre_colonnes):
        if grille[0][colonne] == grille[1][colonne] == grille[2][colonne] != "":
            return grille[0][colonne]
    
    # Vérifier les diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] != "":
        return grille[0][0]
    
    if grille[0][2] == grille[1][1] == grille[2][0] != "":
        return grille[0][2]
    
    return None

#Fonction pour vérifier s'il y a une égalité
def verifier_egalite():
    for ligne in grille:
        for case in ligne:
            if case == "":
                return False
    return True

#Fonction pour afficher le message du gagnant avec animation
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

#Boucle principale du jeu
en_cours = True             
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not fin_jeu:
            x, y = event.pos
            colonne = x // taille_case
            ligne = y // taille_case

            if grille[ligne][colonne] == "":
                grille[ligne][colonne] = joueur
                
                # Vérifier s'il y a un gagnant
                gagnant_temporaire = verifier_gagnant()
                if gagnant_temporaire:
                    fin_jeu = True
                    gagnant = gagnant_temporaire
                elif verifier_egalite():
                    fin_jeu = True
                    gagnant = None
                else:
                    joueur = "O" if joueur == "X" else "X"
    
    ecran.fill(blanc)
    dessiner_grille()   
    dessiner_symboles()
    
    # Afficher le message du gagnant si le jeu est terminé
    if fin_jeu:
        afficher_gagnant(gagnant)
    
    pygame.display.flip()   
    horloge.tick(60)    
pygame.quit()       

