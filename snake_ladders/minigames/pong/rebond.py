import math

def rebonds(
        coordonnee_balle_y, 
        coordonnee_balle_x,
        rayon,
        trajectoire_y,
        trajectoire_x,
        joueur,
        adversaire,
        vitesse_balle
        ):
    
    # Rebond mur du haut.
    if coordonnee_balle_y - rayon <= 0:
        coordonnee_balle_y = rayon
        # Inverse la direction de la balle.
        trajectoire_y = -trajectoire_y

    # Rebond mur du bas.
    if coordonnee_balle_y + rayon >= 720:
        coordonnee_balle_y = 720 - rayon
        trajectoire_y = -trajectoire_y

    # Rebond sur joueur.
    if joueur.collidepoint(coordonnee_balle_x + rayon, coordonnee_balle_y):
        coordonnee_balle_x = joueur.left - rayon

        # calcul impact: Y balle - Y centre joueur = endroit sur rectangle.
        # Endroit sur rectangle equivaut combien en % sur rectangle? divise par 2 pour que l'echelle 40 à -40 soit de 1 à -1 et non 0.5 à -0.5.
        endroit_impact = (coordonnee_balle_y - joueur.centery) / (joueur.height / 2)

        # angle max 60 degrés. Testé plus haut et c'était trop facile.
        angle = endroit_impact * math.radians(60)

        # Nouvelle trajectoire selon endroit de rebond.
        trajectoire_x = -math.cos(angle) * vitesse_balle
        trajectoire_y = math.sin(angle) * vitesse_balle

        # Accélération de la balle à chaque impact.
        vitesse_balle *= 1.05

    # Rebond sur adversaire.
    if adversaire.collidepoint(coordonnee_balle_x - rayon, coordonnee_balle_y):
        coordonnee_balle_x = adversaire.right + rayon

        endroit_impact = (coordonnee_balle_y - adversaire.centery) / (adversaire.height / 2)

        angle = endroit_impact * math.radians(60)

        trajectoire_x = math.cos(angle) * vitesse_balle
        trajectoire_y = math.sin(angle) * vitesse_balle

        vitesse_balle *= 1.05

    return coordonnee_balle_x, coordonnee_balle_y, trajectoire_x, trajectoire_y, vitesse_balle