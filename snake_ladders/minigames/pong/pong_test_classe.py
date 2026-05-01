import pygame
import random
import mouvement
import rebond
import classe_joueur
import classe_adversaire

pygame.init()

# Taille de l'écran de jeu.
ecran = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()

running = True
dt = 0

score_joueur = 0
score_adversaire = 0 

police = pygame.font.SysFont("consolas", 80, bold=True)

victoire = 5

# Vitesse joueur.
vitesse = 200
vitesse_adversaire = 350

# Informations de la balle.
coordonnee_balle_x = 360 # Position de départ sur l'axe X
coordonnee_balle_y = 360 # Position de départ sur l'axe Y
rayon = 15

# Trajectoire initiale de balle en diagonale.
trajectoire_x = 250
trajectoire_y = 180

# Vitesse initaile de la balle.
vitesse_balle = 300

# Créer le rectangle joueur. Sa position et sa taille.
joueur = classe_joueur.joueur()

# Créer le rectangle adversaire.
adversaire = classe_adversaire.adversaire()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    # Couleur de background.
    ecran.fill("black")

    # Restreindre la position des joueurs dans la taille de l'écran.
    joueur.rect.clamp_ip(ecran.get_rect())
    adversaire.rect.clamp_ip(ecran.get_rect())

    # Mouvement joueur.
    joueur.mouvement(dt)

    # Mouvement adversaire.
    adversaire.mouvement(dt, coordonnee_balle_y)
    
    # Mouvement de la balle (en diagonale).
    coordonnee_balle_x, coordonnee_balle_y = mouvement.balle(
        coordonnee_balle_x, 
        coordonnee_balle_y, 
        trajectoire_x, 
        trajectoire_y, 
        dt
    )
    # Rebonds de la balle.
    coordonnee_balle_x, coordonnee_balle_y, trajectoire_x, trajectoire_y, vitesse_balle = rebond.rebonds(
        coordonnee_balle_y, 
        coordonnee_balle_x,
        rayon,
        trajectoire_y,
        trajectoire_x,
        joueur.rect,
        adversaire.rect,
        vitesse_balle
        )

    # Si la balle sort à droite ou à gauche, on réinitialise la position de la balle et sa trajectoire.
    if coordonnee_balle_x - rayon > ecran.get_width():
        # Perdu.
        coordonnee_balle_x = 360
        coordonnee_balle_y = 360
        trajectoire_x = random.choice([-250, 250])
        trajectoire_y = random.randint(-200,200)
        vitesse_balle = 300
        joueur.reinitialiser()
        adversaire.reinitialiser()
        score_adversaire += 1

        if score_adversaire == victoire:
            running = False

    if coordonnee_balle_x + rayon < 0:
        # gagné.
        coordonnee_balle_x = 360
        coordonnee_balle_y = 360
        trajectoire_x = random.choice([-250, 250])
        trajectoire_y = random.randint(-200,200)
        vitesse_balle = 300
        joueur.reinitialiser()
        adversaire.reinitialiser()
        score_joueur += 1

        if score_joueur == victoire:
            running = False

    # Dessiner le rectangle (joueur).
    joueur.dessiner(ecran)

    # Dessiner le rectangle (adversaire).
    adversaire.dessiner(ecran)

    # Dessiner la balle.
    pygame.draw.circle(ecran, ("white"), (coordonnee_balle_x, coordonnee_balle_y), rayon)

    texte_score = police.render(f"{score_adversaire} - {score_joueur}", False, ("white"))
    centre_score = texte_score.get_rect(center=(360, 50))
    ecran.blit(texte_score, centre_score)

    pygame.display.flip()
    dt = clock.tick(60) / 1000 #16 msec entre chaque frame

pygame.quit()