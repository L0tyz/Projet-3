import pygame
import random
from snake_ladders import generateBackground


def start_game(screen, characters, start_index):
    tile_size = 70
    margin = 50
    columns, rows = 10, 10

    def tile_to_pos(n):
        n = max(1, min(100, int(n)))
        row = (n - 1) // 10
        column = (n - 1) % 10
        if row % 2 == 0:
            col_vis = column
        else:
            col_vis = columns - 1 - column
        x = margin + col_vis * tile_size + tile_size // 2
        y = margin + (rows - 1 - row) * tile_size + tile_size // 2
        return x, y

    clock = pygame.time.Clock()
    running = True
    positions = [1 for _ in characters]
    current = start_index if start_index is not None else 0
    font = pygame.font.SysFont(None, 28)
    last_roll = None

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                if e.key == pygame.K_SPACE:
                    roll = random.randint(1, 6)
                    last_roll = roll
                    for _ in range(roll):
                        positions[current] += 1
                        if positions[current] > 100:
                            positions[current] = 100
                        generateBackground.generate_background(screen)
                        for i, char in enumerate(characters):
                            cx, cy = tile_to_pos(positions[i])
                            rect = char.image.get_rect(center=(cx, cy))
                            screen.blit(char.image, rect)
                        turn_text = font.render(f"{characters[current].name} lance: {roll}", True, (250, 240, 220))
                        screen.blit(turn_text, (10, 10))
                        pygame.display.update()
                        pygame.time.delay(120)
                    if positions[current] >= 100:
                        winner_text = font.render(f"{characters[current].name} a gagne!", True, (250, 240, 220))
                        generateBackground.generate_background(screen)
                        for i, char in enumerate(characters):
                            cx, cy = tile_to_pos(positions[i])
                            rect = char.image.get_rect(center=(cx, cy))
                            screen.blit(char.image, rect)
                        screen.blit(winner_text, (350, 20))
                        pygame.display.update()
                        pygame.time.delay(2000)
                        running = False
                    else:
                        current = (current + 1) % len(characters)

        if not running:
            break

        generateBackground.generate_background(screen)
        for i, char in enumerate(characters):
            cx, cy = tile_to_pos(positions[i])
            rect = char.image.get_rect(center=(cx, cy))
            screen.blit(char.image, rect)

        info = f"Tour: {characters[current].name}"
        if last_roll is not None:
            info += f"  Dernier de: {last_roll}"
        info_surf = font.render(info, True, (250, 240, 220))
        screen.blit(info_surf, (10, 10))

        pygame.display.update()
        clock.tick(60)
