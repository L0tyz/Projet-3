import pygame
from classe_joueur import joueur
from classe_adversaire import adversaire
from classe_balle import balle


def run_minijeu(screen, infinite=False):
    clock = pygame.time.Clock()
    dt = 0
    score_joueur = 0
    score_adversaire = 0
    victoire = 5

    police = pygame.font.SysFont("consolas", 80, bold=True)

    joueur_obj = joueur()
    adversaire_obj = adversaire()
    balle_obj = balle()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill("black")

        joueur_obj.mouvement(dt)
        adversaire_obj.mouvement(dt, balle_obj.position_y)
        balle_obj.mouvement(dt)
        balle_obj.rebonds(joueur_obj, adversaire_obj)

        joueur_obj.rect.clamp_ip(screen.get_rect())
        adversaire_obj.rect.clamp_ip(screen.get_rect())

        # point adversaire
        if balle_obj.position_x - balle_obj.rayon > screen.get_width():
            score_adversaire += 1
            balle_obj.reinitialiser()
            joueur_obj.reinitialiser()
            adversaire_obj.reinitialiser()

        # point joueur
        if balle_obj.position_x + balle_obj.rayon < 0:
            score_joueur += 1
            balle_obj.reinitialiser()
            joueur_obj.reinitialiser()
            adversaire_obj.reinitialiser()

        if score_joueur == victoire or score_adversaire == victoire:
            if not infinite:
                running = False

        joueur_obj.dessiner(screen)
        adversaire_obj.dessiner(screen)
        balle_obj.dessiner(screen)

        texte = police.render(f"{score_adversaire} - {score_joueur}", False, "white")
        screen.blit(texte, texte.get_rect(center=(screen.get_width() // 2, 50)))

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    return score_joueur >= victoire


if __name__ == "__main__":
    pygame.init()
    ecran = pygame.display.set_mode((720, 720))
    run_minijeu(ecran)
    pygame.quit()