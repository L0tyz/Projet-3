"""
classes pour le mini jeu snake 
Auteurs Elie Thauvette et Tommy Brunelle
date 5 mai 2026
"""


import pygame
import random

"""
classes background pour le jeu du serpent
entrees: taille des case et de l'ecran
sorties: background: un background avec un quadrille de 40 pixels
"""
class background:
    def __init__(self, taille_case):
        self.taille_case = taille_case

        """
        
        """
    def generer_background(self, ecran):

        # La couleur de fond avant d'ajouter le quadrillé.
        ecran.fill((75, 154, 76))

        # Pour chaque pixel de 0 à la largeur de l'écran, on a un marqueur aux 40 pixels.
        for x in range(0, ecran.get_width(), self.taille_case):
            for y in range(0, ecran.get_height(), self.taille_case):

                # Si le pixel X/40 + le pixel Y/40 modulo 2 est égal à 0, cest pair, nn colore.
                if (x // self.taille_case + y // self.taille_case) % 2 == 0:

                    # Dessine un carré sur l'écran, de la couleur voulue.
                    # Taille X de 40 pixels et taille Y de 40 pixels.
                    pygame.draw.rect(ecran, (67, 138, 69), (x, y, self.taille_case, self.taille_case))

"""
classe pour la pomme du jeu du serpent
entrees: nombre de colonnes et de lignes, taille des cases, de l'ecran et de la pomme
sorties: une pomme qui se génère à une position aléatoire sur l'écran, mais pas sur le serpent
"""
class pomme:

    def __init__(self, colonnes, lignes, taille_case, ecran, largeur_pomme ):
        self.colonnes = colonnes
        self.lignes = lignes
        self.taille_case = taille_case
        self.ecran = ecran
        self.largeur_pomme = largeur_pomme
        self.pos = self.possition()


    def possition(self):
        pomme_col = random.randint(0, self.colonnes - 1)
        pomme_ligne = random.randint(0, self.lignes - 1)

        pomme_x = pomme_col * self.taille_case + self.taille_case / 2
        pomme_y = pomme_ligne * self.taille_case + self.taille_case / 2

        return pygame.Vector2(pomme_x, pomme_y)
    
    def creer(self, ecran):
         pygame.draw.circle(ecran, "red", (int(self.pos.x), int(self.pos.y)), self.largeur_pomme)

    def generer(self, serpent, largeur_serpent, largeur_pomme):
        # Tant que la position de la pomme est sur le serpent, on regénère une nouvelle position.
        while True:
            self.pos = self.possition()
            collision = False
            for segment in serpent: 
                if self.pos.distance_to(segment) < largeur_serpent + largeur_pomme:
                    collision = True
                    break
            if  not collision:   
                break

        pygame.draw.circle(self.ecran, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), largeur_pomme // 2)
        return self.pos
    
"""
classe pour le serpent du jeu snake
entrees: taille des cases, largeur et couleur du serpent, vitesse du serpent et position de départ
sorties: le controle du serpent, le serpent qui grandit lorsqu'il mange une pomme, le serpent qui meurt lorsqu'il touche les murs ou lui même
"""

class serpent_object:

    def __init__(self, taille_case, largeur_serpent, couleur_serpent, vitesse, pos_depart):
        self.corp_serpent = [pygame.Vector2(pos_depart)]
        self.taille_case = taille_case
        self.largeur_serpent = largeur_serpent
        self.couleur_serpent = couleur_serpent
        self.vitesse = vitesse
        self.prochain_mouvement = pygame.Vector2(0, -1)
        self.mouvement = pygame.Vector2(0, -1)

    def creer(self, ecran):
        for segment in self.corp_serpent:
            pygame.draw.circle(ecran, self.couleur_serpent, segment, self.largeur_serpent)

    def grandir(self):
        for i in range(10):
            self.corp_serpent.append(self.corp_serpent[-1])

    def collision_serpent(self):
        tete_serpent = self.corp_serpent[0]
        for segment in self.corp_serpent[20:]:
            if tete_serpent.distance_to(segment) < self.largeur_serpent +5:
                return True
        return False
    
    def collision_mur(self, ecran):
        tete_serpent = self.corp_serpent[0]
        if tete_serpent.x >= ecran.get_width() or tete_serpent.x <= 0 or tete_serpent.y >= ecran.get_height() or tete_serpent.y <= 0:
            return True
        return False
    
    def ctl_mouvement(self):
        touches = pygame.key.get_pressed()
        if touches[pygame.K_w] or touches[pygame.K_UP]:
            if self.prochain_mouvement != pygame.Vector2(0, 1): 
                self.prochain_mouvement = pygame.Vector2(0, -1)
            
        if touches[pygame.K_s] or touches[pygame.K_DOWN]:
            if self.prochain_mouvement != pygame.Vector2(0, -1):
                self.prochain_mouvement = pygame.Vector2(0, 1)
        
        if touches[pygame.K_a] or touches[pygame.K_LEFT]:
            if self.prochain_mouvement != pygame.Vector2(1, 0):
                self.prochain_mouvement = pygame.Vector2(-1, 0)
            
        if touches[pygame.K_d] or touches[pygame.K_RIGHT]:
            if self.prochain_mouvement != pygame.Vector2(-1, 0):
                self.prochain_mouvement = pygame.Vector2(1, 0)
    
    def marge(self, dt):     
        #Serpent avance de 3,2 pixels par frame(image) et ca va à 60 images par secondes.
        #pour déterminer la marge de tolerance pour tourner pcq à 60 fps, ca se peut qu'on skip le centre.
        marge_centre_max = self.vitesse * dt - 1 #Peut pas descendre plus bas que moins 1 sans affecter le gameplay.
        #               x     -        20,    modulo    40
        position_x = (self.corp_serpent[0].x - self.taille_case / 2) % self.taille_case #Si on est au centre = 0
        #               y     -        20,    modulo    40
        position_y = (self.corp_serpent[0].y - self.taille_case / 2) % self.taille_case

        # marge_x est TRUE si position_x est <= a notre marge_max OU si >= 40 - marge_max
        # marge_x est TRUE si ca vaut 0,1,2 ou 37, 38, 39
        marge_x = position_x <= marge_centre_max or position_x >= self.taille_case - marge_centre_max
        marge_y = position_y <= marge_centre_max or position_y >= self.taille_case - marge_centre_max
        

        if marge_x and marge_y: 
        
            if self.prochain_mouvement + self.mouvement != pygame.Vector2(0, 0):
                self.mouvement = self.prochain_mouvement
            
    
    def animation(self, dt):
        nouveau_segment = self.corp_serpent[0] + self.mouvement * self.vitesse * dt
        self.corp_serpent.insert(0, nouveau_segment)
        self.corp_serpent.pop()

