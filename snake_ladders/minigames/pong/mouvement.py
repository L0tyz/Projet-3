import pygame

def joueur(joueur, dt):
    touches = pygame.key.get_pressed()
    if touches[pygame.K_w]:
        joueur.y -= 300 * dt
        
    if touches[pygame.K_s]:
        joueur.y += 300 * dt

def adversaire(adversaire, dt, coordonnee_balle_y, vitesse_adversaire):
    if adversaire.centery < coordonnee_balle_y:
        adversaire.y += vitesse_adversaire * dt
    
    # Si le Y du centre du rectangle est > que le Y de la balle: TRUE.
    if adversaire.centery > coordonnee_balle_y:
        # Adversaire monte.
        adversaire.y -= vitesse_adversaire * dt

def balle(coordonnee_balle_x, coordonnee_balle_y, trajectoire_x, trajectoire_y, dt):
    coordonnee_balle_x += trajectoire_x * dt
    coordonnee_balle_y += trajectoire_y * dt
    
    return coordonnee_balle_x, coordonnee_balle_y