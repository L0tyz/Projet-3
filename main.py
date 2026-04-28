# Fichier principal du projet, qui affiche le menu principal et lance le jeu et les options en fonction du choix de l'utilisateur

import pygame
import sys
from snake_ladders.game import Game
from snake_ladders.options import Options
tile_image = pygame.image.load('assets/bg.png')
class MainMenu:
    def __init__(self):
        # Initialisation de la fenetre du menu principals
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Snake and Chaos")
        self.clock = pygame.time.Clock()

        font_path = "assets/8-BIT.ttf"
        self.big = pygame.font.Font(font_path, 70)
        self.font = pygame.font.Font(font_path, 30)

        self.colors = {
            "background": (90, 62, 43),
            "panel": (194, 176, 128),
            "accent": (139, 90, 43),
            "border": (60, 40, 20),
            "green": (75, 160, 54),
            "orange": (123, 90, 60),
            "mint": (178, 216, 178),
            "red": (160, 52, 29),
            "text": (250, 240, 220)
        }
        for x in range(0, 1000, 16):
                for y in range(0, 800, 16):
                    self.screen.blit(tile_image, (x, y))
            
        pygame.display.flip()

        self.options = Options(self.screen, self.font, self.colors)
    """ Affiche un bouton avec un effet de hover """
    def draw_button(self, rect, text, mouse_pos):
        color = self.colors["orange"] if rect.collidepoint(mouse_pos) else self.colors["accent"]
        pygame.draw.rect(self.screen, color, rect, border_radius=12)
        pygame.draw.rect(self.screen, self.colors["border"], rect, 3, border_radius=8)
        label = self.font.render(text, True, self.colors["text"])
        self.screen.blit(label, label.get_rect(center=rect.center))

    def run(self):
        """ Structure le menu principal et retourne les choix de l'utilisateur """
        while True:
            # Récupère la position de la souris pour gérer les collisions avec les boutons
            mouse_pos = pygame.mouse.get_pos()

            panel = pygame.Rect(200,40,600,720)
            pygame.draw.rect(self.screen, self.colors["panel"], panel, border_radius=12)

            s = self.big.render("SNAKES", True, self.colors["green"])
            l = self.big.render("LADDERS", True, self.colors["orange"])
            ch = self.font.render("CHAOS", True, self.colors["mint"])

            self.screen.blit(s, s.get_rect(center=(500,140)))
            lr = l.get_rect(center=(500,240))
            self.screen.blit(l, lr)
            # fait une petite croix rouge sur le ladders
            pygame.draw.line(self.screen, self.colors["red"], (lr.left, lr.top), (lr.right, lr.bottom), 15)
            pygame.draw.line(self.screen, self.colors["red"], (lr.left, lr.bottom), (lr.right, lr.top), 15)
            self.screen.blit(ch, ch.get_rect(center=(500,280)))

            #position des boutons
            play_rect = pygame.Rect(350, 420, 300, 70)
            options_rect = pygame.Rect(350, 510, 300, 70)
            quit_rect = pygame.Rect(350, 600, 300, 70)
            # Affiche les boutons et gère les interactions
            self.draw_button(play_rect, "JOUER", mouse_pos)
            self.draw_button(options_rect, "OPTIONS", mouse_pos)
            self.draw_button(quit_rect, "QUITTER", mouse_pos)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return "QUIT"
                if e.type == pygame.MOUSEBUTTONDOWN:
                    # Vérifie si un bouton a été cliqué et retourne le choix correspondant
                    if play_rect.collidepoint(mouse_pos):
                        return "PLAY"
                    if options_rect.collidepoint(mouse_pos):
                        result = self.options.run()
                        if result == "QUIT":
                            return "QUIT"
                    if quit_rect.collidepoint(mouse_pos):
                        return "QUIT"
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN: return "PLAY"

            pygame.display.update()
            self.clock.tick(60)


def main():
    """ Affiche le menu principal et lance le jeu ou les options en fonction du choix de l'utilisateur  """
    m = MainMenu()
    while True:
        c = m.run()
        if c == "PLAY": Game().run()
        if c == "QUIT": pygame.quit(); sys.exit()

if __name__ == "__main__": main()

