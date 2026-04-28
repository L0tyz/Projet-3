# Fonctions pour le deplacement du serpent dans le minijeu snake.
# Auteurs Elie Thauvette et Tommy Brunelle
# Date

import pygame
class deplacements:

    def __init__(self, taille_case, vitesse):
        self.taille_case = taille_case
        self.vitesse = vitesse
        

# Fonction pour controler le mouvement du serpent et pour eviter que le serpent puisse faire demi tour sur lui meme.
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

        prochain_mouve = prochain_mouvement
        return prochain_mouve

    # Fontion pour que le serpent suivent le centre des case avec un marge de tolerance pour le changement de direction.
    def marge(self, snake, prochain_mouvement, mouvement, dt):     
        #Serpent avance de 3,2 pixels par frame(image) et ca va à 60 images par secondes.
        #pour déterminer la marge de tolerance pour tourner pcq à 60 fps, ca se peut qu'on skip le centre.
        marge_centre_max = self.vitesse * dt - 1 #Peut pas descendre plus bas que moins 1 sans affecter le gameplay.
        #               x     -        20,    modulo    40
        position_x = (snake[0].x - self.taille_case / 2) % self.taille_case #Si on est au centre = 0
        #               y     -        20,    modulo    40
        position_y = (snake[0].y - self.taille_case / 2) % self.taille_case

        #marge_x est TRUE si position_x est <= a notre marge_max OU si >= 40 - marge_max
        # marge_x est TRUE si ca vaut 0,1,2 ou 37, 38, 39
        marge_x = position_x <= marge_centre_max or position_x >= self.taille_case - marge_centre_max
        marge_y = position_y <= marge_centre_max or position_y >= self.taille_case - marge_centre_max
        

        if marge_x and marge_y: 
        
            if prochain_mouvement + mouvement != pygame.Vector2(0, 0):
                mouvement = prochain_mouvement
            

        return mouvement

