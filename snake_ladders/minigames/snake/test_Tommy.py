import pygame
import random

pygame.init()
#Taille ecran de jeu
ecran = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()
running = True

#Delta time (permet de faire des frame par secondes)
#Temps ecoule depuis la derniere frame
dt = 0

#Position de depart en frames.
snake = [pygame.Vector2(340, 340)]
#Taille du cercle noir
player_radius = 20
#Couleur du cercle
player_color = "black"
#Score initial
score = 0

#Taille des pommes en frames
circle_radius = 20

# Mouvement initial
mouvement = pygame.Vector2(0, -1)
prochain_mouvement = pygame.Vector2(0, -1)

vitesse = 200 #pixels/sec

taille_case = 40 #pixels

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

    #couleur de fond avant ajout de quadrillé.
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
        prochain_mouvement = pygame.Vector2(0, -1)
    if touches[pygame.K_s]:
        prochain_mouvement = pygame.Vector2(0, 1)
    if touches[pygame.K_a]:
        prochain_mouvement = pygame.Vector2(-1, 0)
    if touches[pygame.K_d]:
        prochain_mouvement = pygame.Vector2(1, 0)

    #Serpent avance de 3,2 pixels par frame(image) et ca va à 60 images par secondes.
    #pour déterminer la marge de tolerance pour tourner pcq à 60 fps, ca se peut qu'on skip le centre.
    marge_centre_max = vitesse * dt - 1 #Peut pas descendre plus bas que moins 1 sans affecter le gameplay.
    #               x     -        20,    modulo    40
    position_x = (snake[0].x - taille_case / 2) % taille_case #Si on est au centre = 0
    #               y     -        20,    modulo    40
    position_y = (snake[0].y - taille_case / 2) % taille_case

    #marge_x est TRUE si position_x est <= a notre marge_max OU si >= 40 - marge_max
    # marge_x est TRUE si ca vaut 0,1,2 ou 37, 38, 39
    marge_x = position_x <= marge_centre_max or position_x >= taille_case - marge_centre_max
    marge_y = position_y <= marge_centre_max or position_y >= taille_case - marge_centre_max
    
    # Si marge_x et marge_y sont TRUE
    if marge_x and marge_y:
        #change la direction du snake
        mouvement = prochain_mouvement

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
       
        for i in range(10):
                snake.append(snake[-1])
        vitesse += 10
        score += 1
        
    
    # Si le joueur sort de l'ecran, le jeu se termine.
    if snake[0].x >= ecran.get_width() or snake[0].x <= 0 or snake[0].y >= ecran.get_height() or snake[0].y <= 0:
        running = False

    
    pygame.display.flip()
    dt = clock.tick(60) / 1000 #16 msec entre chaque frame

pygame.quit()
