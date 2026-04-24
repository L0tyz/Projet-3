import pygame
import random
import math

pygame.init()

# Taille de l'écran de jeu.
ecran = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()

running = True
dt = 0

# Vitesse joueur.
vitesse = 200
vitesse_adversaire = 350

# Informations de la balle.
coordonnee_balle_x = 360 # Position de départ sur l'axe X
coordonnee_balle_y = 360 # Position de départ sur l'axe Y
rayon = 15

# trajectoire initiale de balle en diagonale.
trajectoire_x = 250
trajectoire_y = 180

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
    touches = pygame.key.get_pressed()
    if touches[pygame.K_w]:
        joueur.y -= 300 * dt
        
    if touches[pygame.K_s]:
        joueur.y += 300 * dt
    
    # Mouvement de la balle (en diagonale).
    coordonnee_balle_x += trajectoire_x * dt
    coordonnee_balle_y += trajectoire_y * dt

    # Rebond mur du haut.
    if coordonnee_balle_y - rayon <= 0:
        coordonnee_balle_y = rayon
        # Inverse la direction de la balle.
        trajectoire_y = -trajectoire_y

    # Rebond mur du bas.
    if coordonnee_balle_y + rayon >= 720:
        coordonnee_balle_y = 720 - rayon
        trajectoire_y = -trajectoire_y

    # Rebond sur joueur.
    if joueur.collidepoint(coordonnee_balle_x + rayon, coordonnee_balle_y):
        coordonnee_balle_x = joueur.left - rayon

        # calcul impact: Y balle - Y centre joueur = endroit sur rectangle.
        # Endroit sur rectangle equivaut combien en % sur rectangle? divise par 2 pour que l'echelle 40 à -40 soit de 1 à -1 et non 0.5 à -0.5.
        endroit_impact = (coordonnee_balle_y - joueur.centery) / (joueur.height / 2)

        # angle max 60 degrés. Testé plus haut et c'était trop facile.
        angle = endroit_impact * math.radians(60)

        # Nouvelle trajectoire selon endroit de rebond.
        trajectoire_x = -math.cos(angle) * vitesse_balle
        trajectoire_y = math.sin(angle) * vitesse_balle

        # Accélération de la balle à chaque impact.
        vitesse_balle *= 1.1

    # Rebond sur adversaire.
    if adversaire.collidepoint(coordonnee_balle_x - rayon, coordonnee_balle_y):
        coordonnee_balle_x = adversaire.right + rayon

        endroit_impact = (coordonnee_balle_y - adversaire.centery) / (adversaire.height / 2)

        angle = endroit_impact * math.radians(60)

        trajectoire_x = math.cos(angle) * vitesse_balle
        trajectoire_y = math.sin(angle) * vitesse_balle

        vitesse_balle *= 1.03

    # Mouvement adversaire.
    if adversaire.centery < coordonnee_balle_y:
        adversaire.y += vitesse_adversaire * dt
    
    # Si le Y du centre du rectangle est > que le Y de la balle: TRUE.
    if adversaire.centery > coordonnee_balle_y:
        # Adversaire monte.
        adversaire.y -= vitesse_adversaire * dt
    # Si la balle sort à droite ou à gauche, on réinitialise la position de la balle et sa trajectoire.
    if coordonnee_balle_x - rayon > ecran.get_width():
        # Perdu.
        coordonnee_balle_x = 360
        coordonnee_balle_y = 360
        trajectoire_x = random.choice([-250, 250])
        trajectoire_y = random.randint(-200,200)
        vitesse_balle = 300 

    if coordonnee_balle_x + rayon < 0:
        # gagné.
        coordonnee_balle_x = 360
        coordonnee_balle_y = 360
        trajectoire_x = random.choice([-250, 250])
        trajectoire_y = random.randint(-200,200)
        vitesse_balle = 300

    # Dessiner le rectangle (joueur).
    pygame.draw.rect(ecran, ("white"), joueur)

    # Dessiner le rectangle (adversaire).
    pygame.draw.rect(ecran, ("white"), adversaire)

    # Dessiner la balle.
    pygame.draw.circle(ecran, ("white"), (coordonnee_balle_x, coordonnee_balle_y), rayon)

    pygame.display.flip()
    dt = clock.tick(60) / 1000 #16 msec entre chaque frame

pygame.quit()