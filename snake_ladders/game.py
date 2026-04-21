import os

import pygame
import snake_ladders.generateBackground as generateBackground

class Character:
    def __init__(self, image_path, name, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.name = name

class Character:
    def __init__(self, image_path, name, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.name = name

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((1100,800))
        self.clock = pygame.time.Clock()
        self.running = True
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, "img")
    
        self.characters = [
            Character(os.path.join(img_dir, "pion.png"), "Bleu", 200, 250),
            Character(os.path.join(img_dir, "pionrouge.png"), "Rouge", 425, 250),
            Character(os.path.join(img_dir, "pionvert.png"), "Vert", 650, 250)
        ]
        
        self.selected = None


    def run(self):
        selecting = True
        while self.running and selecting:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                    selecting = False
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
            
            for i, char in enumerate(self.characters):
                self.screen.blit(char.image, char.rect)
                
                
                if self.selected == i:
                    pygame.draw.rect(self.screen, (75, 160, 54), char.rect, 5)
                else:
                    pygame.draw.rect(self.screen, (139, 90, 43), char.rect, 3)
                
                
                name_text = f.render(char.name, True, (250, 240, 220))
                self.screen.blit(name_text, name_text.get_rect(center=(char.rect.centerx, char.rect.bottom + 50)))

            pygame.display.update()
            self.clock.tick(60)