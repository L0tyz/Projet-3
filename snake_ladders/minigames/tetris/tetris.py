"""
Vincent Goulet
Fichier principale contenant les fonctions pygame 
"""
import pygame, sys
from game import Game
from colors import Colors


def run_minijeu(screen, infinite=False):
    title_font = pygame.font.Font(None, 40)
    score_surface = title_font.render("Score", True, Colors.couleur_texte)
    next_surface = title_font.render("Next", True, Colors.couleur_texte)
    game_over_surface = title_font.render("GAME OVER", True, Colors.couleur_texte)

    score_rect = pygame.Rect(320, 55, 170, 60)
    next_rect = pygame.Rect(320, 215, 170, 180)

    clock = pygame.time.Clock()
    game = Game()
    SCORE_VICTOIRE = 300

    GAME_UPDATE = pygame.USEREVENT + 10  # éviter conflit avec le jeu principal
    pygame.time.set_timer(GAME_UPDATE, 200)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if game.game_over:
                    running = False
                if event.key == pygame.K_LEFT and not game.game_over:
                    game.move_left()
                if event.key == pygame.K_RIGHT and not game.game_over:
                    game.move_right()
                if event.key == pygame.K_DOWN and not game.game_over:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP and not game.game_over:
                    game.rotate()
            if event.type == GAME_UPDATE and not game.game_over:
                game.move_down()

        if game.score >= SCORE_VICTOIRE or game.game_over:
            if not infinite:
                running = False

        score_value_surface = title_font.render(str(game.score), True, Colors.couleur_texte)

        screen.fill(Colors.couleur_fond)
        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (375, 180, 50, 50))

        if game.game_over:
            screen.blit(game_over_surface, (320, 450, 50, 50))

        pygame.draw.rect(screen, Colors.couleur_carre, score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
            centery=score_rect.centery))
        pygame.draw.rect(screen, Colors.couleur_carre, next_rect, 0, 10)
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.time.set_timer(GAME_UPDATE, 0)
    return game.score >= SCORE_VICTOIRE


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 620))
    pygame.display.set_caption("Python Tetris")
    run_minijeu(screen)
    pygame.quit()
    sys.exit()