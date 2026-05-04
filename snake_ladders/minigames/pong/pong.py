import pygame
from classe_joueur import joueur
from classe_adversaire import adversaire
from classe_balle import balle

pygame.init()

ecran = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()

running = True

# Delta time. Permet plus tard d'ajuster le FPS.
dt = 0

# Scores initiaux.
score_joueur = 0
score_adversaire = 0

victoire = 5

# Police pour le score.
police = pygame.font.SysFont("consolas", 80, bold=True)

# Les objets.
joueur = joueur()
adversaire = adversaire()
balle = balle()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ecran.fill("black")

    joueur.mouvement(dt)
    adversaire.mouvement(dt, balle.position_y)
    balle.mouvement(dt)

    balle.rebonds(joueur, adversaire)

    # Limiter le déplacement des joueurs dans l'écran.
    joueur.rect.clamp_ip(ecran.get_rect())
    adversaire.rect.clamp_ip(ecran.get_rect())

    # point adversaire
    if balle.position_x - balle.rayon > 720:
        score_adversaire += 1
        balle.reinitialiser()
        joueur.reinitialiser()
        adversaire.reinitialiser()

    # point joueur
    if balle.position_x + balle.rayon < 0:
        score_joueur += 1
        balle.reinitialiser()
        joueur.reinitialiser()
        adversaire.reinitialiser()

    # victoire
    if score_joueur == victoire or score_adversaire == victoire:
        running = False

    # dessins
    joueur.dessiner(ecran)
    adversaire.dessiner(ecran)
    balle.dessiner(ecran)

    texte = police.render(f"{score_adversaire} - {score_joueur}", False, "white")
    ecran.blit(texte, texte.get_rect(center=(360,50)))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()