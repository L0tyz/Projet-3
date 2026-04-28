import pygame
class jeu:

    def __init__(self, victoire, vitesse, vitesse_adversaire, rayon):
        self.victoire = victoire
        self.vitesse = vitesse
        self.vitesse_adversaire = vitesse_adversaire
        self.rayon = rayon

    def mouvement(self, joueur, dt):
        touches = pygame.key.get_pressed()
        if touches[pygame.K_w]:
            joueur.y -= 300 * dt
        
        if touches[pygame.K_s]:
            joueur.y += 300 * dt