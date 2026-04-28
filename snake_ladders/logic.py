import os
import sys
import pygame
import random
from snake_ladders import generateBackground


LADDERS       = {5: 16, 14: 29, 23: 44, 37: 60, 58: 76}
SNAKES        = {94: 72, 81: 59, 67: 46, 48: 30, 33: 12}
REVERSE_TILES = {34, 82}
PORTAL_PAIRS  = {19: 52, 52: 19, 61: 87, 87: 61}
MINIGAME_TILES = {11, 26, 39, 54, 70, 88}

MINIGAME_LIST = [
    "colorconquest/colorconquest.py",
]


def run_minigame(screen, minigame_name):
    base_dir      = os.path.dirname(os.path.abspath(__file__))
    minigames_dir = os.path.join(base_dir, "minigames")
    game_path     = os.path.join(minigames_dir, minigame_name)
    if not os.path.exists(game_path):
        print(f"[Mini-jeu] Fichier introuvable : {game_path}")
        return False
    game_dir = os.path.dirname(game_path)
    if game_dir not in sys.path:
        sys.path.insert(0, game_dir)
    import importlib.util
    spec = importlib.util.spec_from_file_location("minigame_module", game_path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "run"):
        return bool(mod.run(screen))
    return False


def apply_tile_effect(screen, position, current_idx, positions, human_index):
    positions = list(positions)
    msg = None

    if position in LADDERS:
        positions[current_idx] = LADDERS[position]
        msg = f"Echelle !  {position} -> {LADDERS[position]}"

    elif position in SNAKES:
        positions[current_idx] = SNAKES[position]
        msg = f"Serpent !  {position} -> {SNAKES[position]}"

    elif position in REVERSE_TILES:
        others = [i for i in range(len(positions)) if i != current_idx]
        if others:
            target = random.choice(others)
            positions[current_idx], positions[target] = positions[target], positions[current_idx]
            msg = f"Reverse !  Echange avec joueur {target + 1}"

    elif position in PORTAL_PAIRS:
        positions[current_idx] = PORTAL_PAIRS[position]
        msg = f"Portail !  {position} -> {PORTAL_PAIRS[position]}"

    elif position in MINIGAME_TILES:
        if current_idx == human_index:
            game = random.choice(MINIGAME_LIST)
            won = run_minigame(screen, game)
            if won:
                positions[current_idx] = min(100, positions[current_idx] + 4)
                msg = "Mini-jeu gagne !  +4 cases"
            else:
                positions[current_idx] = max(1, positions[current_idx] - 4)
                msg = "Mini-jeu perdu.  -4 cases"
        else:
            won = random.choice([True, False])
            if won:
                positions[current_idx] = min(100, positions[current_idx] + 4)
                msg = f"Bot {current_idx + 1} mini-jeu : gagne !  +4 cases"
            else:
                positions[current_idx] = max(1, positions[current_idx] - 4)
                msg = f"Bot {current_idx + 1} mini-jeu : perdu.  -4 cases"

    return positions, msg



def start_game(screen, characters, start_index):
    tile_size = 70
    margin = 50
    columns, rows = 10, 10

    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "..", "assets")

    dice_images = []
    for i in range(1, 7):
        path = os.path.join(assets_dir, f"dice_{i}.png")
        if os.path.exists(path):
            img = pygame.image.load(path).convert_alpha()
            dice_images.append(img)
        else:
            s = pygame.Surface((80, 80), pygame.SRCALPHA)
            s.fill((210, 210, 210))
            f = pygame.font.SysFont(None, 48)
            t = f.render(str(i), True, (0, 0, 0))
            s.blit(t, t.get_rect(center=(40, 40)))
            dice_images.append(s)

    die_size = (80, 80)
    dice_images = [pygame.transform.scale(img, die_size) for img in dice_images]
    die_x = screen.get_width() - 140
    die_y = screen.get_height() // 2 - 40
    die_pos = (die_x, die_y)

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
                    # animate die
                    for _ in range(10):
                        generateBackground.generate_background(screen)
                        for i, char in enumerate(characters):
                            cx, cy = tile_to_pos(positions[i])
                            rect = char.game_image.get_rect(center=(cx, cy))
                            screen.blit(char.game_image, rect)
                            if i == start_index:
                                v_surf = font.render("Vous", True, (255, 215, 0))
                                v_rect = v_surf.get_rect(center=(cx, cy - 36))
                                screen.blit(v_surf, v_rect)
                        face = random.choice(dice_images)
                        screen.blit(face, die_pos)
                        info_text = f"{characters[current].name} lance"
                        info_surf = font.render(info_text, True, (250, 240, 220))
                        info_rect = info_surf.get_rect(center=(die_pos[0] + die_size[0] // 2, die_pos[1] - 24))
                        screen.blit(info_surf, info_rect)
                        pygame.display.update()
                        pygame.time.delay(60)

                    # final roll
                    face = dice_images[roll - 1]
                    # move pawn step by step with redraw
                    for _ in range(roll):
                        positions[current] += 1
                        if positions[current] > 100:
                            positions[current] = 100
                        generateBackground.generate_background(screen)
                        for i, char in enumerate(characters):
                            cx, cy = tile_to_pos(positions[i])
                            rect = char.game_image.get_rect(center=(cx, cy))
                            screen.blit(char.game_image, rect)
                            if i == start_index:
                                v_surf = font.render("Vous", True, (255, 215, 0))
                                v_rect = v_surf.get_rect(center=(cx, cy - 36))
                                screen.blit(v_surf, v_rect)
                        screen.blit(face, die_pos)
                        info_text = f"{characters[current].name} lance: {roll}"
                        info_surf = font.render(info_text, True, (250, 240, 220))
                        info_rect = info_surf.get_rect(center=(die_pos[0] + die_size[0] // 2, die_pos[1] - 24))
                        screen.blit(info_surf, info_rect)
                        pygame.display.update()
                        pygame.time.delay(120)

                    if positions[current] >= 100:
                        winner_text = font.render(f"{characters[current].name} a gagne!", True, (250, 240, 220))
                        generateBackground.generate_background(screen)
                        for i, char in enumerate(characters):
                            cx, cy = tile_to_pos(positions[i])
                            rect = char.game_image.get_rect(center=(cx, cy))
                            screen.blit(char.game_image, rect)
                            if i == start_index:
                                v_surf = font.render("Vous", True, (255, 215, 0))
                                v_rect = v_surf.get_rect(center=(cx, cy - 36))
                                screen.blit(v_surf, v_rect)
                        screen.blit(face, die_pos)
                        screen.blit(winner_text, (350, 20))
                        pygame.display.update()
                        pygame.time.delay(2000)
                        running = False
                    else:
                        positions, msg = apply_tile_effect(
                            screen, positions[current], current, positions, start_index)

                        if msg:
                            generateBackground.generate_background(screen)
                            for i, char in enumerate(characters):
                                cx, cy = tile_to_pos(positions[i])
                                rect = char.game_image.get_rect(center=(cx, cy))
                                screen.blit(char.game_image, rect)
                                if i == start_index:
                                    v_surf = font.render("Vous", True, (255, 215, 0))
                                    v_rect = v_surf.get_rect(center=(cx, cy - 36))
                                    screen.blit(v_surf, v_rect)
                            screen.blit(face, die_pos)
                            eff_surf = font.render(msg, True, (255, 80, 80))
                            eff_rect = eff_surf.get_rect(center=(die_pos[0] + die_size[0] // 2, die_pos[1] + die_size[1] + 16))
                            screen.blit(eff_surf, eff_rect)
                            pygame.display.update()
                            pygame.time.delay(900)

                        
                        if positions[current] >= 100:
                            winner_text = font.render(f"{characters[current].name} a gagne!", True, (250, 240, 220))
                            generateBackground.generate_background(screen)
                            for i, char in enumerate(characters):
                                cx, cy = tile_to_pos(positions[i])
                                rect = char.game_image.get_rect(center=(cx, cy))
                                screen.blit(char.game_image, rect)
                            screen.blit(face, die_pos)
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
            rect = char.game_image.get_rect(center=(cx, cy))
            screen.blit(char.game_image, rect)
            if i == start_index:
                v_surf = font.render("Vous", True, (255, 215, 0))
                v_rect = v_surf.get_rect(center=(cx, cy - 36))
                screen.blit(v_surf, v_rect)

        # draw die and info on right
        if last_roll is not None:
            screen.blit(dice_images[last_roll - 1], die_pos)
        info = f"Tour: {characters[current].name}"
        info_surf = font.render(info, True, (250, 240, 220))
        info_rect = info_surf.get_rect(center=(die_pos[0] + die_size[0] // 2, die_pos[1] - 24))
        screen.blit(info_surf, info_rect)

        pygame.display.update()
        clock.tick(30)