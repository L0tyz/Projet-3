### Fichier qui gère les options du jeu, comme la musique, les sons et le volume.
# Il affiche une interface pour permettre à l'utilisateur de modifier ces paramètres.

import pygame

class Options:
    # Initialisation des paramètres et chargement des ressources audio
    def __init__(self, screen, font, c):
        self.screen = screen
        self.font = font
        self.colors = c
        self.music = True
        self.sfx = True
        self.volume = 0.5
        try:
            pygame.mixer.music.load("assets/sounds/music.mp3")
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play(-1)
        except:
            self.music = False
        try:
            self.click = pygame.mixer.Sound("assets/sounds/hit.mp3")
        except:
            self.click = None

    def play_click(self):
        # Joue un son de clic si les effets sonores sont activés
        if self.sfx and self.click:
            self.click.play()

    def run(self):
        # Affiche l'interface des options et gère les interactions de l'utilisateur
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self.screen.fill(self.colors["background"])
            pygame.draw.rect(self.screen, self.colors["panel"], (200, 40, 600, 720), border_radius=12)

            title = self.font.render("OPTIONS", True, self.colors["text"])
            self.screen.blit(title, title.get_rect(center=(500, 120)))

            # Slider de volume
            bar = pygame.Rect(300, 250, 400, 10)
            pygame.draw.rect(self.screen, self.colors["border"], bar)
            knob_x = 300 + int(self.volume * 400)
            pygame.draw.circle(self.screen, self.colors["orange"], (knob_x, 255), 10)

            music_btn = pygame.Rect(350, 350, 300, 60)
            sfx_btn = pygame.Rect(350, 430, 300, 60)

            for rect, txt in [
                (music_btn, f"MUSIQUE {'ACTIF' if self.music else 'INACTIF'}"),
                (sfx_btn, f"SONS {'ACTIFS' if self.sfx else 'INACTIFS'}"),
            ]:
                color = self.colors["orange"] if rect.collidepoint(mouse_pos) else self.colors["accent"]
                pygame.draw.rect(self.screen, color, rect, border_radius=10)
                pygame.draw.rect(self.screen, self.colors["border"], rect, 3, border_radius=10)
                label = self.font.render(txt, True, self.colors["text"])
                self.screen.blit(label, label.get_rect(center=rect.center))

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return "QUIT"
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    return "BACK"
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if bar.collidepoint(mouse_pos):
                        self.volume = max(0, min(1, (mouse_pos[0] - 300) / 400))
                        pygame.mixer.music.set_volume(self.volume)
                    if music_btn.collidepoint(mouse_pos):
                        self.play_click()
                        self.music = not self.music
                        pygame.mixer.music.play(-1) if self.music else pygame.mixer.music.stop()
                    if sfx_btn.collidepoint(mouse_pos):
                        self.play_click()
                        self.sfx = not self.sfx

            pygame.display.update()
