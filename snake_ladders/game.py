import pygame
import snake_ladders.generateBackground as generateBackground

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((1100,800))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: self.running = False
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: self.running = False

            self.screen.fill((50,35,20))
            generateBackground.generate_background(self, self.screen)
            pygame.display.flip()

            
  
            self.clock.tick(60)
