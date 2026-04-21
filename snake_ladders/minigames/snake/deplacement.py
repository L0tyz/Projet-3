import pygame


def ctl_mouvement(prochain_mouvement):
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
    
    return prochain_mouvement

def marge(snake, taille_case, vitesse, dt, prochain_mouvement, mouvement):     
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
    

    if marge_x and marge_y: 
        mouvement = prochain_mouvement

    return mouvement

