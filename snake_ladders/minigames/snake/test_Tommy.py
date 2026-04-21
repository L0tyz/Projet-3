import pygame
import random
import background

pygame.init()
#Taille ecran de jeu
ecran = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()
running = True

# Delta time (permet de faire des pixels par secondes).
dt = 0

# Position de depart du serpent.
snake = [pygame.Vector2(340, 340)]

# Taille du serpent.
player_radius = 20

# Couleur du serpent.
player_color = "black"

# Score initial.
score = 0

# Taille des pommes.
circle_radius = 20

# Mouvements initiaux.
mouvement = pygame.Vector2(0, -1)
prochain_mouvement = pygame.Vector2(0, -1)

# Vitesse du serpent.
vitesse = 200 

taille_case = 40 # Pixels.

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

    background.generer_background(ecran, taille_case)
   
    pygame.draw.circle(ecran, "red", circle_pos, circle_radius)
    pygame.display.set_caption(f"score: {score}")
    for segment in snake:
        pygame.draw.circle(ecran, player_color, segment, player_radius)

    # mouvement avec touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_w]:
        if prochain_mouvement != pygame.Vector2(0, 1):
            prochain_mouvement = pygame.Vector2(0, -1)
    if touches[pygame.K_s]:
        if prochain_mouvement != pygame.Vector2(0, -1):
            prochain_mouvement = pygame.Vector2(0, 1)
    if touches[pygame.K_a]:
        if prochain_mouvement != pygame.Vector2(1, 0):
            prochain_mouvement = pygame.Vector2(-1, 0)
    if touches[pygame.K_d]:
        if prochain_mouvement != pygame.Vector2(-1, 0):
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
