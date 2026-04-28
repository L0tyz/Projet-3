import os
import pygame
import sys
import snake_ladders.logic as logic
from snake_ladders.game import Game
from snake_ladders.options import Options

class MainMenu:
    """ Classe qui gère la base de pygame et les differentes choses necessaires pour le menu """
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Snake and Chaos")
        self.clock = pygame.time.Clock()

        font_path = "assets/8-BIT.ttf"
        self.big = pygame.font.Font(font_path, 70)
        self.font = pygame.font.Font(font_path, 30)
        self.tile_image = pygame.image.load('assets/bg.png')
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
        # Affiche un background en damier en utilisant l'image de tile chargée et en la répétant sur toute la surface de l'écran
        for x in range(0, 1000, 16):
            for y in range(0, 800, 16):
                self.screen.blit(self.tile_image, (x, y))
        pygame.display.flip()

        self.options = Options(self.screen, self.font, self.colors)

    def draw_button(self, rect, text, mouse_pos):
        """ Affiche un bouton avec un effet de hover """
        color = self.colors["orange"] if rect.collidepoint(mouse_pos) else self.colors["accent"]
        pygame.draw.rect(self.screen, color, rect, border_radius=12)
        pygame.draw.rect(self.screen, self.colors["border"], rect, 3, border_radius=8)
        label = self.font.render(text, True, self.colors["text"])
        self.screen.blit(label, label.get_rect(center=rect.center))

    def run(self):
        """ Structure le menu principal et retourne les choix de l'utilisateur """
        while True:
            mouse_pos = pygame.mouse.get_pos()
        
            for x in range(0, 1000, 16):
                for y in range(0, 800, 16):
                    self.screen.blit(self.tile_image, (x, y))

            panel = pygame.Rect(200, 40, 600, 720)
            pygame.draw.rect(self.screen, self.colors["panel"], panel, border_radius=12)

            s = self.big.render("SNAKES", True, self.colors["green"])
            l = self.big.render("LADDERS", True, self.colors["orange"])
            ch = self.font.render("CHAOS", True, self.colors["mint"])

            self.screen.blit(s, s.get_rect(center=(500, 140)))
            lr = l.get_rect(center=(500, 240))
            self.screen.blit(l, lr)
            pygame.draw.line(self.screen, self.colors["red"], (lr.left, lr.top), (lr.right, lr.bottom), 15)
            pygame.draw.line(self.screen, self.colors["red"], (lr.left, lr.bottom), (lr.right, lr.top), 15)
            self.screen.blit(ch, ch.get_rect(center=(500, 280)))

            play_rect = pygame.Rect(350, 420, 300, 70)
            options_rect = pygame.Rect(350, 510, 300, 70)
            minigames_rect = pygame.Rect(350, 600, 300, 70)
            quit_rect = pygame.Rect(350, 690, 300, 70)

            self.draw_button(play_rect, "JOUER", mouse_pos)
            self.draw_button(options_rect, "OPTIONS", mouse_pos)
            self.draw_button(minigames_rect, "MINI JEUX", mouse_pos)
            self.draw_button(quit_rect, "QUITTER", mouse_pos)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return "QUIT"
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if play_rect.collidepoint(mouse_pos):
                        return "PLAY"
                    if options_rect.collidepoint(mouse_pos):
                        result = self.options.run()
                        if result == "QUIT":
                            return "QUIT"
                    if minigames_rect.collidepoint(mouse_pos):
                        return "MINIGAMES"
                    if quit_rect.collidepoint(mouse_pos):
                        return "QUIT"
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        return "PLAY"

            pygame.display.update()
            self.clock.tick(60)


class MiniGameMenu:
    """ Classe qui gère le menu de selection des mini-jeux et lance le mini-jeu sélectionné en appelant la fonction run_minigame du module logic """
    def __init__(self, screen, font, colors, tile_image):
        self.screen = screen
        self.font = font
        self.colors = colors
        self.tile_image = tile_image
        self.clock = pygame.time.Clock()

        self.minigames = [
            {"label": "Color Conquest", "path": "colorconquest/colorconquest.py"},
            {"label": "Tetris",         "path": "tetris/tetris.py"},
            {"label": "Tic Tac Toe",    "path": "tictactoe/tictactoe.py"},
            {"label": "Snake",          "path": "snake/snake.py"},
            {"label": "Pong",           "path": "pong/pong.py"},
            {"label": "Hangman",        "path": "hangman/hangman.py"},
        ]

    def draw_button(self, rect, text, mouse_pos):
        """ Affiche un bouton avec un effet de hover """
        color = self.colors["orange"] if rect.collidepoint(mouse_pos) else self.colors["accent"]
        pygame.draw.rect(self.screen, color, rect, border_radius=12)
        pygame.draw.rect(self.screen, self.colors["border"], rect, 3, border_radius=8)
        label = self.font.render(text, True, self.colors["text"])
        self.screen.blit(label, label.get_rect(center=rect.center))

    def run(self):
        """ Affiche le menu de selection des mini-jeux et lance le mini-jeu sélectionné en appelant la fonction run_minigame du module logic """
        while True:
            mouse_pos = pygame.mouse.get_pos()

            for x in range(0, 1000, 16):
                for y in range(0, 800, 16):
                    self.screen.blit(self.tile_image, (x, y))

            panel = pygame.Rect(150, 40, 700, 720)
            pygame.draw.rect(self.screen, self.colors["panel"], panel, border_radius=12)

            buttons = []
            for idx, mg in enumerate(self.minigames):
                col, row = idx % 2, idx // 2
                rect = pygame.Rect(185 + col * 300, 150 + row * 100, 270, 70)
                buttons.append((rect, mg))
                self.draw_button(rect, mg["label"], mouse_pos)

            back_rect = pygame.Rect(350, 680, 300, 55)
            self.draw_button(back_rect, "RETOUR", mouse_pos)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    return
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(mouse_pos):
                        return
                    for rect, mg in buttons:
                        if rect.collidepoint(mouse_pos):
                            logic.run_minigame(self.screen, mg["path"])

            pygame.display.update()
            self.clock.tick(60)


def main():
    """ Affiche le menu principal et lance le jeu ou les options en fonction du choix de l'utilisateur """
    m = MainMenu()
    while True:
        c = m.run()
        if c == "PLAY":
            Game().run()
        elif c == "MINIGAMES":
            MiniGameMenu(m.screen, m.font, m.colors, m.tile_image).run()
        elif c == "QUIT":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()