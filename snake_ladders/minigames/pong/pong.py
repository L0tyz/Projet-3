import pygame
import random
import mouvement
import rebond

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
joueur = pygame.Rect(680, 300, 20, 80)

# Créer le rectangle adversaire.
adversaire = pygame.Rect(20, 300, 20, 80)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    # Couleur de background.
    ecran.fill("black")

    # Restreindre la position des joueurs dans la taille de l'écran.
    joueur.clamp_ip(ecran.get_rect())
    adversaire.clamp_ip(ecran.get_rect())

    # Mouvement joueur.
    mouvement.joueur(joueur, dt)

    # Mouvement adversaire.
    mouvement.adversaire(adversaire, dt, coordonnee_balle_y, vitesse_adversaire)
    
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
        joueur,
        adversaire,
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
        joueur = pygame.Rect(680, 300, 20, 80)
        adversaire = pygame.Rect(20, 300, 20, 80)
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
        joueur = pygame.Rect(680, 300, 20, 80)
        adversaire = pygame.Rect(20, 300, 20, 80)
        score_joueur += 1

        if score_joueur == victoire:
            running = False

    # Dessiner le rectangle (joueur).
    pygame.draw.rect(ecran, ("white"), joueur)

    # Dessiner le rectangle (adversaire).
    pygame.draw.rect(ecran, ("white"), adversaire)

    # Dessiner la balle.
    pygame.draw.circle(ecran, ("white"), (coordonnee_balle_x, coordonnee_balle_y), rayon)

    texte_score = police.render(f"{score_adversaire} - {score_joueur}", False, ("white"))
    centre_score = texte_score.get_rect(center=(360, 50))
    ecran.blit(texte_score, centre_score)

    pygame.display.flip()
    dt = clock.tick(60) / 1000 #16 msec entre chaque frame

pygame.quit()