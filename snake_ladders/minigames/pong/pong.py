import pygame

pygame.init()

# Taille de l'écran de jeu.
ecran = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()

running = True
dt = 0

vitesse = 200

# Informations de la balle.
coordonnee_balle_x = 360 # Position de départ sur l'axe X
coordonnee_balle_y = 360 # Position de départ sur l'axe Y
rayon = 15

# Vitesses pour un mouvement de balle en diagonale en pixels/seconde.
vitesse_x = 250
vitesse_y = 180

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

    # Restreindre la position du joueur dans la taille de l'écran.
    joueur.clamp_ip(ecran.get_rect())

    touches = pygame.key.get_pressed()
    if touches[pygame.K_UP]:
        joueur.y -= 300 * dt
        
    if touches[pygame.K_DOWN]:
        joueur.y += 300 * dt
    
    # Mouvement de la balle (en diagonale).
    coordonnee_balle_x += vitesse_x * dt
    coordonnee_balle_y += vitesse_y * dt

    # Rebond mur du haut.
    if coordonnee_balle_y - rayon <= 0:
        coordonnee_balle_y = rayon
        # Inverse la direction de la balle.
        vitesse_y = -vitesse_y

    # Rebond mur du bas.
    if coordonnee_balle_y + rayon >= 720:
        coordonnee_balle_y = 720 - rayon
        vitesse_y = -vitesse_y

    # Rebond sur joueur.
    if joueur.collidepoint(coordonnee_balle_x + rayon, coordonnee_balle_y):
        coordonnee_balle_x = joueur.left - rayon
        vitesse_x = -vitesse_x

    # Dessiner le rectangle (joueur).
    pygame.draw.rect(ecran, ("white"), joueur)

    # Dessiner le rectangle (adversaire).
    pygame.draw.rect(ecran, ("white"), adversaire)

    # Dessiner la balle.
    pygame.draw.circle(ecran, ("white"), (coordonnee_balle_x, coordonnee_balle_y), rayon)

    pygame.display.flip()
    dt = clock.tick(60) / 1000 #16 msec entre chaque frame

pygame.quit()