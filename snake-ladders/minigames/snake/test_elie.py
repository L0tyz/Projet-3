import pygame
import random

pygame.init()
#Taille ecran de jeu
ecran = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()
running = True

#Delta time (permet de faire des frame par secondes)
dt = 0

#Position de depart.
player_pos = pygame.Vector2(ecran.get_width() / 2, ecran.get_height() / 2)
#Taille du cercle noir
player_radius = 10
#Couleur du cercle
player_color = "black"
score = 0

#Taille des pommes
circle_radius = 20
# SPawn de pommes random sur le fond.
circle_pos = pygame.Vector2(
    random.randint(0, ecran.get_width()),
    random.randint(0, ecran.get_height())
)
# Mouvement initial
mouvement = pygame.Vector2(0, -1)

vitesse = 120 #frames

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    ecran.fill((75, 154, 76))

    taille_case = 40

    #Tracer quadrillé
    #Pour chaque pixel de 0 à la largeur de l'ecran, a chaque 40 pixels y se passe ce quil y a dans le for loop.
    for x in range(0, ecran.get_width(), taille_case):
        for y in range(0, ecran.get_height(), taille_case):
            # Si le pixel x/40 + pixel y/40, modulo 2 = 0, cest pair. On colore.
            if (x // taille_case + y // taille_case) % 2 == 0:
                # Fait un carree sur ecran, couleur, x est 40 pixels, y est 40 pixels.
                pygame.draw.rect(ecran, (67, 138, 69), (x, y, taille_case, taille_case))
   
    pygame.draw.circle(ecran, player_color, player_pos, player_radius)
    pygame.draw.circle(ecran, "red", circle_pos, circle_radius)
    pygame.display.set_caption(f"score: {score}")


    # mouvement avec touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_w]:
        mouvement = pygame.Vector2(0, -1)
    if touches[pygame.K_s]:
        mouvement = pygame.Vector2(0, 1)
    if touches[pygame.K_a]:
        mouvement = pygame.Vector2(-1, 0)
    if touches[pygame.K_d]:
        mouvement = pygame.Vector2(1, 0)

    # La position du joueur + une direction et vitesse de deplacement.
    player_pos += mouvement * vitesse * dt

    # collision
    distance = player_pos.distance_to(circle_pos)
    if distance <= player_radius + circle_radius:
        
        circle_pos = pygame.Vector2(
            random.randint(0, ecran.get_width()),
            random.randint(0, ecran.get_height())
        )
        player_radius += 10
        score += 1
        
    if player_pos.x >= ecran.get_width() or player_pos.x <= 0 or player_pos.y >= ecran.get_height() or player_pos.y <= 0:
        running = False
        
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
