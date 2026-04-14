import pygame
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
win = False


def create_color_grid(rows, cols, palette=None):
    """Return a rows x cols 2D list of RGB tuples.

    If palette is provided, choose colours from it; otherwise generate random
    bright-ish colours.
    """
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if palette:
                color = random.choice(palette)
            else:
                # Generate a random bright colour (avoid too dark)
                color = (
                    random.randint(80, 255),
                    random.randint(80, 255),
                    random.randint(80, 255),
                )
            row.append(color)
        grid.append(row)
    return grid


def draw_rect_grid(surface, rows, cols, cell_size, color_grid=None, outline_color=(200, 200, 200)):
    """Draw a grid of rectangles. If color_grid is provided it must be a 2D
    list of the same dimensions and will be used to fill each cell before
    drawing the outline."""
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            if color_grid:
                try:
                    fill_color = color_grid[row][col]
                except Exception:
                    fill_color = (0, 0, 0)
                pygame.draw.rect(surface, fill_color, rect)  # filled
            # Draw the outline on top so grid lines remain visible
            pygame.draw.rect(surface, outline_color, rect, 1)


def flood_fill_color(grid, start_row, start_col, new_color):
    """Replace the contiguous region (4-neighbour) of the start cell's
    original colour with new_color."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    old_color = grid[start_row][start_col]
    if old_color == new_color:
        return
    stack = [(start_row, start_col)]
    while stack:
        r, c = stack.pop()
        if grid[r][c] != old_color:
            continue
        grid[r][c] = new_color
        # neighbors: up, down, left, right
        if r > 0:
            stack.append((r - 1, c))
        if r < rows - 1:
            stack.append((r + 1, c))
        if c > 0:
            stack.append((r, c - 1))
        if c < cols - 1:
            stack.append((r, c + 1))
def check_win_condition(grid):
    global win
    """Check if all cells in the grid are the same colour."""
    first_color = grid[0][0]
    for row in grid:
        for color in row:
            if color != first_color:
                win = False
                return
    
    win = True
    return


def main():
    rows, cols, cell_size = 10, 10, 60
    # Palette with only five allowed colours: pink, orange, red, yellow, purple
    PALETTE = [
        (255, 105, 180),  # pink
        (255, 165, 0),    # orange
        (220, 20, 60),    # red
        (255, 215, 0),    # yellow
        (148, 0, 211),    # purple
    ]

    # Create an initial random colour grid that persists until reshuffled
    color_grid = create_color_grid(rows, cols, palette=PALETTE)
    selected_index = 0  # which palette button is selected (default first)
    # Limit palette clicks
    MAX_PALETTE_CLICKS = 20
    palette_clicks = 0
    game_over = False

    # Compute button layout at bottom of the screen
    screen_w, screen_h = screen.get_size()
    bottom_area_y = rows * cell_size
    bottom_area_h = screen_h - bottom_area_y
    button_w, button_h = 80, 80
    spacing = 20
    total_w = len(PALETTE) * button_w + (len(PALETTE) - 1) * spacing
    start_x = (screen_w - total_w) // 2
    button_y = bottom_area_y + (bottom_area_h - button_h) // 2
    # Precompute button rects
    button_rects = []
    for i in range(len(PALETTE)):
        x = start_x + i * (button_w + spacing)
        button_rects.append(pygame.Rect(x, button_y, button_w, button_h))

    # Font for instructions
    try:
        font = pygame.font.SysFont(None, 20)
    except Exception:
        font = None

    running = True
    while running:
        check_win_condition(color_grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Press R to reshuffle the grid colours
                if event.key == pygame.K_r:
                    color_grid = create_color_grid(rows, cols, palette=PALETTE)
                    # Reset game state on restart
                    palette_clicks = 0
                    game_over = False
                    selected_index = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click
                    mx, my = event.pos
                    # Check palette button clicks first
                    for i, rect in enumerate(button_rects):
                        if rect.collidepoint(mx, my):
                            # If game over, ignore palette clicks (only R restarts)
                            if game_over:
                                break
                            selected_index = i
                            # Count this palette click and check limit
                            palette_clicks += 1
                            if palette_clicks > MAX_PALETTE_CLICKS:
                                game_over = True
                                # Do not apply the colour — show lose popup instead
                                break
                            # Immediately apply the selected colour to the bottom-left
                            # contiguous region so the player doesn't need to click
                            # the cell itself.
                            flood_fill_color(color_grid, rows - 1, 0, PALETTE[selected_index])
                            break
                    else:
                        # If click wasn't on a button, check grid region to paint.
                        # User may only paint the bottom-left square (row = rows-1, col = 0).
                        if 0 <= mx < cols * cell_size and 0 <= my < rows * cell_size:
                            col = mx // cell_size
                            row = my // cell_size
                            # Only allow painting the bottom-left cell directly
                            if row == rows - 1 and col == 0:
                                # Use flood-fill: change contiguous region of the
                                # bottom-left cell's original colour to the selected colour.
                                flood_fill_color(color_grid, row, col, PALETTE[selected_index])

        # Clear screen each frame
        screen.fill((0, 0, 0))

        # Draw the coloured grid
        draw_rect_grid(screen, rows, cols, cell_size, color_grid=color_grid)

        # Draw palette buttons
        for i, rect in enumerate(button_rects):
            pygame.draw.rect(screen, PALETTE[i], rect)
            # Outline
            border_color = (255, 255, 255) if i == selected_index else (200, 200, 200)
            pygame.draw.rect(screen, border_color, rect, 3 if i == selected_index else 1)

        # Draw click counter
        if font:
            click_counter = font.render(f'Palette clicks: {palette_clicks}/{MAX_PALETTE_CLICKS}', True, (0, 0, 0))
            screen.blit(click_counter, (10, 10))

        if win:
            # semi-transparent overlay
            overlay = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
            overlay.fill((255, 255, 255, 180))
            screen.blit(overlay, (0, 0))
            if font:
                win_text = font.render('you win! press r to restart.', True, (0, 128, 0))
                tw, th = win_text.get_size()
                screen.blit(win_text, ((screen_w - tw) // 2, (screen_h - th) // 2))
        # If game over, show popup overlay
        if game_over:
            # semi-transparent overlay
            overlay = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))
            if font:
                lose_text = font.render('you lose! press r to restart.', True, (255, 0, 0))
                tw, th = lose_text.get_size()
                screen.blit(lose_text, ((screen_w - tw) // 2, (screen_h - th) // 2))

        # Draw simple instructions
        if font:
            instructions = font.render('Turn the whole board one colour! \nClick a palette colour to change the bottom left square\'s colour and conquer the board!', True, (255, 255, 255))
            screen.blit(instructions, (10, screen_h - 30))

        # Game Logic & Rendering Here (add UI, score, etc.)

        pygame.display.flip()  # Update screen
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
