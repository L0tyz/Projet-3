# Fichier principal du jeu, qui affiche la fenetre de selection des personnages et lance le jeu une fois un personnage selectionné
# en appelant la fonction start_game du module logic et en generant le background avec le module generateBackground

import os
import pygame
import snake_ladders.generateBackground as generateBackground
import snake_ladders.logic as logic

class Character:
    """ Clase qui permet de representer les personnages en chargan leurs images """
    def __init__(self, image_path, name, x, y):
        img = pygame.image.load(image_path).convert_alpha()
        selection_size = (96, 96)
        game_size = (48, 48)
        self.selection_image = pygame.transform.scale(img, selection_size)
        self.game_image = pygame.transform.scale(img, game_size)
        self.rect = self.selection_image.get_rect(topleft=(x, y))
        self.name = name

class Game:

    def __init__(self):
        """ Initialisation de la fenetre de selection des personnages """
        self.screen = pygame.display.set_mode((1100,800))
        self.clock = pygame.time.Clock()
        self.running = True
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(base_dir, "..", "assets")

        self.characters = [
            Character(os.path.join(assets_dir, "pion.png"), "Bleu", 200, 250),
            Character(os.path.join(assets_dir, "pionrouge.png"), "Rouge", 425, 250),
            Character(os.path.join(assets_dir, "pionvert.png"), "Vert", 650, 250)
        ]
        
        self.selected = None

    def run(self):
        """ Affiche la fenetre de selection des personnages et lance le jeu une fois un personnage selectionné """
        selecting = True
        while self.running and selecting:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                    selecting = False
                # Permet de quitter la fenetre de selection avec echap
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    self.running = False
                    selecting = False
                if e.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for i, char in enumerate(self.characters):
                        if char.rect.collidepoint(pos):
                            self.selected = i
                            selecting = False

            self.screen.fill((50, 35, 20))
            
            f = pygame.font.SysFont("8bitwondernominal", 30)
            title = f.render("SELECTIONNER VOTRE PION", True, (250, 240, 220))
            self.screen.blit(title, title.get_rect(center=(500, 50)))
            # Affiche les personnages et leur nom, et entoure le personnage selectionné
            for i, char in enumerate(self.characters):
                self.screen.blit(char.selection_image, char.rect)
                
                # Entoure le personnage selectionné en vert, les autres en orange
                if self.selected == i:
                    pygame.draw.rect(self.screen, (75, 160, 54), char.rect, 5)
                else:
                    pygame.draw.rect(self.screen, (139, 90, 43), char.rect, 3)
                
                
                name_text = f.render(char.name, True, (250, 240, 220))
                self.screen.blit(name_text, name_text.get_rect(center=(char.rect.centerx, char.rect.bottom + 50)))
            
            pygame.display.update()
            self.clock.tick(30)
        # Lance le jeu une fois un personnage selectionné
        if self.running and not selecting:
            logic.start_game(self.screen, self.characters, self.selected)
            self.running = False