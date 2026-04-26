import os
import pygame


def draw_checkered_grid(screen):
    font = pygame.font.SysFont(None, 24)
    color1 = (154, 121, 168)
    color2 = (148, 105, 49)
    tile_size = 70
    margin = 50
    columns, rows = 10, 10

    for row in range(rows):
        for column in range(columns):
            if row % 2 == 0:
                col = column
            else:
                col = columns - 1 - column

            x = margin + col * tile_size
            y = margin + (rows - 1 - row) * tile_size

            grid_x = col
            grid_y = rows - 1 - row
            color = color1 if (grid_x + grid_y) % 2 == 0 else color2

            pygame.draw.rect(screen, color, (x, y, tile_size, tile_size))

            number = row * columns + column + 1
            num_surf = font.render(str(number), True, (0, 0, 0))
            nx = x + 10
            ny = y + 10
            screen.blit(num_surf, (nx, ny))


def add_snakes_and_ladders(screen):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "..", "assets")

    original_ladder = pygame.image.load(os.path.join(assets_dir, "ladder.png")).convert_alpha()
    base_ladder = pygame.transform.scale(
        original_ladder,
        (int(original_ladder.get_width() * 0.7), int(original_ladder.get_height() * 1.2)),
    )
    ladder_1 = pygame.transform.scale(
        base_ladder, (int(base_ladder.get_width()), int(base_ladder.get_height() * 0.9))
    )
    ladder_1 = pygame.transform.rotate(ladder_1, -35)
    ladder_2 = pygame.transform.scale(
        base_ladder, (int(base_ladder.get_width()), int(base_ladder.get_height() * 1.2))
    )
    ladder_2 = pygame.transform.rotate(ladder_2, 25)
    ladder_3 = pygame.transform.scale(
        base_ladder, (int(base_ladder.get_width()), int(base_ladder.get_height() * 0.5))
    )
    screen.blit(ladder_1, (470, 450))
    screen.blit(ladder_2, (200, 300))
    screen.blit(ladder_3, (555, 140))

    reverse_scale = 0.017
    reverse = pygame.image.load(os.path.join(assets_dir, "uno_reverse.png")).convert_alpha()
    reverse = pygame.transform.scale(
        reverse, (int(reverse.get_width() * reverse_scale), int(reverse.get_height() * reverse_scale))
    )
    screen.blit(reverse, (290, 620))
    screen.blit(reverse, (500, 340))

    portal_scale = 0.17
    blue_portal = pygame.image.load(os.path.join(assets_dir, "portal_blue.png")).convert_alpha()
    orange_portal = pygame.image.load(os.path.join(assets_dir, "portal_orange.png")).convert_alpha()
    blue_portal = pygame.transform.scale(
        blue_portal, (int(blue_portal.get_width() * portal_scale), int(blue_portal.get_height() * portal_scale))
    )
    orange_portal = pygame.transform.scale(
        orange_portal, (int(orange_portal.get_width() * portal_scale), int(orange_portal.get_height() * portal_scale))
    )
    screen.blit(blue_portal, (130, 120))
    screen.blit(blue_portal, (550, 190))
    screen.blit(blue_portal, (130, 680))
    screen.blit(orange_portal, (400, 400))
    screen.blit(orange_portal, (190, 260))


def generate_background(screen):
    draw_checkered_grid(screen)
    add_snakes_and_ladders(screen)