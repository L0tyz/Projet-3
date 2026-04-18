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
snake = [pygame.Vector2(ecran.get_width() / 2, ecran.get_height() / 2)]
#Taille du cercle noir
player_radius = 20
#Couleur du cercle
player_color = "black"

score = 0

#Taille des pommes
circle_radius = 20
# SPawn de pommes random sur le fond.

# Mouvement initial
mouvement = pygame.Vector2(0, -1)

vitesse = 120 #frames

taille_case = 40

# position des pommes avec les cases
colonnes = ecran.get_width() // taille_case
lignes = ecran.get_height() // taille_case

pomme_col = random.randint(0, colonnes - 1)
pomme_ligne = random.randint(0, lignes - 1)

pomme_x = pomme_col * taille_case + taille_case / 2
pomme_y = pomme_ligne * taille_case + taille_case / 2

circle_pos = pygame.Vector2(pomme_x, pomme_y)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    ecran.fill((75, 154, 76))

    

    #Tracer quadrillé
    #Pour chaque pixel de 0 à la largeur de l'ecran, a chaque 40 pixels y se passe ce quil y a dans le for loop.
    for x in range(0, ecran.get_width(), taille_case):
        for y in range(0, ecran.get_height(), taille_case):
            # Si le pixel x/40 + pixel y/40, modulo 2 = 0, cest pair. On colore.
            if (x // taille_case + y // taille_case) % 2 == 0:
                # Fait un carree sur ecran, couleur, x est 40 pixels, y est 40 pixels.
                pygame.draw.rect(ecran, (67, 138, 69), (x, y, taille_case, taille_case))
   
    pygame.draw.circle(ecran, "red", circle_pos, circle_radius)
    pygame.display.set_caption(f"score: {score}")
    for segment in snake:
        pygame.draw.circle(ecran, player_color, segment, player_radius)

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
    new_head = snake[0] + mouvement * vitesse * dt
    snake.insert(0, new_head)
    snake.pop()

    # collision
    distance = snake[0].distance_to(circle_pos)
    if distance <= player_radius + circle_radius:
        
        pomme_col = random.randint(0, colonnes - 1)
        pomme_ligne = random.randint(0, lignes - 1)

        pomme_x = pomme_col * taille_case + taille_case / 2
        pomme_y = pomme_ligne * taille_case + taille_case / 2

        circle_pos = pygame.Vector2(pomme_x, pomme_y)
       
        for i in range(3):
                snake.append(snake[-1])
        vitesse += 10
        score += 1
        
    
    # Si le joueur sort de l'ecran, le jeu se termine.
    if snake[0].x >= ecran.get_width() or snake[0].x <= 0 or snake[0].y >= ecran.get_height() or snake[0].y <= 0:
        running = False

    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
