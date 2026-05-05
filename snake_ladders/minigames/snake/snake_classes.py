"""
classes pour le mini jeu Snake.
Auteurs: Elie Thauvette et Tommy Brunelle
date: 5 mai 2026
"""

import pygame
import random

class background:
    """
    But: Indiquer les valeurs de base du fond d'écran.\
             (La taille des carrés du quadrillé, et les couleurs.)
    Entrée: self et taille_case.
    Sortie: Aucune.
    """
    def __init__(self, taille_case):
        self.taille_case = taille_case


    def generer_background(self, ecran):
        """
        But: Générer la grille qui sert de plateau de jeu.
        Entrée: self et la taille de l'écran.
        Sortie: Aucune.
        """

        ecran.fill((75, 154, 76))

        # Pour chaque pixel de 0 à la largeur de l'écran, on a un marqueur aux 40 pixels (taille_case).
        for x in range(0, ecran.get_width(), self.taille_case):
            for y in range(0, ecran.get_height(), self.taille_case):

                # Si c'est une case pair, on colore la case.
                if (x // self.taille_case + y // self.taille_case) % 2 == 0:

                    # Dessiner les cases.
                    pygame.draw.rect(ecran, (67, 138, 69), (x, y, self.taille_case, self.taille_case))


class pomme:

    def __init__(self, colonnes, lignes, taille_case, ecran, largeur_pomme ):
        """
        But: Définir les variables de base pour les fonctions dans la classe.
        Entrées: Self, nombre de colonnes et de lignes, taille des cases, de l'écran et de la pomme.
        Sorties: Aucune.
        """
        self.colonnes = colonnes
        self.lignes = lignes
        self.taille_case = taille_case
        self.ecran = ecran
        self.largeur_pomme = largeur_pomme
        self.pos = self.position()


    def position(self):
        """
        But: Générer une pomme à une position aléatoire sur l'écran, mais pas sur le serpent.
        Entrées: Self.
        Sorties: Aucune.
        """
        pomme_col = random.randint(0, self.colonnes - 1)
        pomme_ligne = random.randint(0, self.lignes - 1)

        pomme_x = pomme_col * self.taille_case + self.taille_case / 2
        pomme_y = pomme_ligne * self.taille_case + self.taille_case / 2

        return pygame.Vector2(pomme_x, pomme_y)
    
    
    def creer(self, ecran):
        """
        But: Créer la première pomme.
        Entrées: Self et ecran.
        Sorties: Aucune.
        """
        pygame.draw.circle(ecran, "red", (int(self.pos.x), int(self.pos.y)), self.largeur_pomme)


    def generer(self, serpent, largeur_serpent, largeur_pomme):
        """
        But: Générer une nouvelle pomme lorsque la tête du serpent entre en contact avec la pomme actuelle.
        Entrées: Self, serpent, largeur_serpent, largeur_pomme.
        Sorties: self.pos (la posiiton de la nouvelle pomme).
        """
        # Tant que la position de la pomme est sur le serpent, on regénère une nouvelle position.
        while True:
            self.pos = self.position()
            collision = False
            for segment in serpent: 
                if self.pos.distance_to(segment) < largeur_serpent + largeur_pomme:
                    collision = True
                    break
            if  not collision:   
                break

        pygame.draw.circle(self.ecran, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), largeur_pomme // 2)
        return self.pos


class serpent_object:

    def __init__(self, taille_case, largeur_serpent, couleur_serpent, vitesse, pos_depart):
        """
        But: Définir les variables de base pour les fonctions dans la classe.
        Entrées: Self, taille_case, largeur_serpent, couleur_serpent, vitesse, pos_depart.
        Sortie: Aucune.
        """
        self.corp_serpent = [pygame.Vector2(pos_depart)]
        self.taille_case = taille_case
        self.largeur_serpent = largeur_serpent
        self.couleur_serpent = couleur_serpent
        self.vitesse = vitesse
        self.prochain_mouvement = pygame.Vector2(0, -1)
        self.mouvement = pygame.Vector2(0, -1)
        

    def creer(self, ecran):
        """
        But: Créer le serpent selon sa longueur.
        Entrées: Self, ecran.
        Sortie: Aucune.
        """
        for segment in self.corp_serpent:
            pygame.draw.circle(ecran, self.couleur_serpent, segment, self.largeur_serpent)


    def grandir(self):
        """
        But: Allonger la taille du serpent.
        Entrée: Self.
        Sortie: Aucune.
        """
        for i in range(10):
            self.corp_serpent.append(self.corp_serpent[-1])


    def collision_serpent(self):
        """
        But: Détecter une collision avec soi-même.
        Entrées: Self.
        Sortie: Boolean (True ou False).
        """
        tete_serpent = self.corp_serpent[0]
        for segment in self.corp_serpent[20:]:
            if tete_serpent.distance_to(segment) < self.largeur_serpent +5:
                return True
        return False
    
    
    def collision_mur(self, ecran):
        """
        But: Détecter une collision avec le mur.
        Entrées: Self, ecran.
        Sortie: Boolean (True ou False).
        """
        tete_serpent = self.corp_serpent[0]
        if tete_serpent.x >= ecran.get_width() or tete_serpent.x <= 0 or tete_serpent.y >= ecran.get_height() or tete_serpent.y <= 0:
            return True
        return False
    
    
    def ctl_mouvement(self):
        """
        But: Bouger le serpent dans une direction choisie par les flèches du clavier.
        Entrées: Self.
        Sortie: Aucune.
        """
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
        """
        But: Limiter les mouvements du serpents "dans la grille".
        Entrées: Self, dt.
        Sortie: Aucune.
        """
        # Marge de tolerance pour le centre de la case, en fonction de la vitesse du serpent.
        marge_centre_max = self.vitesse * dt - 1 #Peut pas descendre plus bas que moins 1 sans affecter le gameplay.
        position_x = (self.corp_serpent[0].x - self.taille_case / 2) % self.taille_case #Si on est au centre = 0
        position_y = (self.corp_serpent[0].y - self.taille_case / 2) % self.taille_case

        marge_x = position_x <= marge_centre_max or position_x >= self.taille_case - marge_centre_max
        marge_y = position_y <= marge_centre_max or position_y >= self.taille_case - marge_centre_max
        

        if marge_x and marge_y: 
        
            if self.prochain_mouvement + self.mouvement != pygame.Vector2(0, 0):
                self.mouvement = self.prochain_mouvement
            
    
    def animation(self, dt):
        """
        But: Faire qu ele serpent garde sa longueur en bougeant.
        Entrées: Self, dt.
        Sortie: Aucune.
        """
        nouveau_segment = self.corp_serpent[0] + self.mouvement * self.vitesse * dt
        self.corp_serpent.insert(0, nouveau_segment)
        self.corp_serpent.pop()

