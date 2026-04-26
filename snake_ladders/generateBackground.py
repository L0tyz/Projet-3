import os
import pygame
import math

TILE_SIZE = 70
MARGIN = 50
COLUMNS = 10
ROWS = 10

def get_tile_center(tile_number):
    """Calcule les coordonnées (x, y) du centre d'une case (1 à 100)."""
    if tile_number < 1: tile_number = 1
    if tile_number > 100: tile_number = 100
    
    tile_idx = tile_number - 1
    row = tile_idx // COLUMNS
    col_in_row = tile_idx % COLUMNS

    if row % 2 == 0:
        col = col_in_row
    else:
        col = (COLUMNS - 1) - col_in_row

    # calcul des pixels
    x = MARGIN + col * TILE_SIZE + (TILE_SIZE // 2)
    y = MARGIN + (ROWS - 1 - row) * TILE_SIZE + (TILE_SIZE // 2)
    return (x, y)

def draw_element_between_tiles(screen, image, start_tile, end_tile, width=40, image_is_horizontal=False):
    """
    Étire et pivote une image pour relier deux cases.
    Gère les images sources verticales (échelles) et horizontales (serpents).
    """
    p1 = get_tile_center(start_tile)
    p2 = get_tile_center(end_tile)
    
    # Calcul des distances
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    # distance euclidienne
    distance = int(math.hypot(dx, dy))
    
    #math.atan2 donne l'angle par rapport a X
    angle = math.degrees(math.atan2(-dy, dx)) 
    
    if image_is_horizontal:
        pass
    else:
        angle -= 90

    if image_is_horizontal:
        img_stretched = pygame.transform.scale(image, (distance, width))
    else:
        img_stretched = pygame.transform.scale(image, (width, distance))
    img_rotated = pygame.transform.rotate(img_stretched, angle)
    
    #centrer image finale entre les deux points
    rect = img_rotated.get_rect(center=((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2))
    screen.blit(img_rotated, rect)

def add_snakes_and_ladders(screen):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "..", "assets")

    try:
        ladder_img = pygame.image.load(os.path.join(assets_dir, "ladder.png")).convert_alpha()
        snake_img = pygame.image.load(os.path.join(assets_dir, "snek.png")).convert_alpha()
        reverse_img = pygame.image.load(os.path.join(assets_dir, "uno_reverse.png")).convert_alpha()
        portal_blue = pygame.image.load(os.path.join(assets_dir, "portal_blue.png")).convert_alpha()
        portal_orange = pygame.image.load(os.path.join(assets_dir, "portal_orange.png")).convert_alpha()
    except pygame.error as e:
        print(f"Erreur image : {e}")
        return

    # echelles

    draw_element_between_tiles(screen, ladder_img, 3, 37, width=100) 
    draw_element_between_tiles(screen, ladder_img, 10, 32, width=100)
    draw_element_between_tiles(screen, ladder_img, 26, 47, width=100)
    draw_element_between_tiles(screen, ladder_img, 51, 68, width=100)
    draw_element_between_tiles(screen, ladder_img, 61, 81, width=100)

    # serpents
    draw_element_between_tiles(screen, snake_img, 98, 64, width=40, image_is_horizontal=True) 
    draw_element_between_tiles(screen, snake_img, 66, 36, width=40, image_is_horizontal=True) 
    draw_element_between_tiles(screen, snake_img, 41, 20, width=40, image_is_horizontal=True)

    # portail/reverse
    rev = pygame.transform.scale(reverse_img, (30, 30))
    screen.blit(rev, rev.get_rect(center=get_tile_center(7)))
    screen.blit(rev, rev.get_rect(center=get_tile_center(50)))

    p_img = pygame.transform.scale(portal_blue, (45, 45))
    screen.blit(p_img, p_img.get_rect(center=get_tile_center(92)))
    screen.blit(p_img, p_img.get_rect(center=get_tile_center(81)))
    
    po_img = pygame.transform.scale(portal_orange, (45, 45))
    screen.blit(po_img, po_img.get_rect(center=get_tile_center(22)))

def draw_checkered_grid(screen):
    font = pygame.font.SysFont(None, 24)
    color1 = (154, 121, 168)  
    color2 = (148, 105, 49)  

    for row in range(ROWS):
        for column in range(COLUMNS):
            
            if row % 2 == 0: col = column
            else: col = COLUMNS - 1 - column

            x = MARGIN + col * TILE_SIZE
            y = MARGIN + (ROWS - 1 - row) * TILE_SIZE

            color = color1 if (col + (ROWS - 1 - row)) % 2 == 0 else color2
            pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))

            number = row * COLUMNS + column + 1
            num_surf = font.render(str(number), True, (0, 0, 0))
            screen.blit(num_surf, (x + 5, y + 5))

def generate_background(screen):
    screen.fill((50, 35, 20))
    draw_checkered_grid(screen)
    add_snakes_and_ladders(screen)