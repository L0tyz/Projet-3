import pygame

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,800))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: self.running = False
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: self.running = False

            self.screen.fill((50,35,20))

            f = pygame.font.SysFont("8bitwondernominal", 20)

            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if btn.collidepoint(pygame.mouse.get_pos()): self.running = False

            pygame.display.update()
            self.clock.tick(60)
