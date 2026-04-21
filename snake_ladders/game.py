import pygame


class Game:


    def draw_checkered_grid(self):
        font = pygame.font.SysFont(None, 24)
        color1 = (154, 121, 168)  # purple
        color2 = (148, 105, 49)   # brown
        tile_size = 70
        margin = 50
        columns, rows = 10, 10

        # We number from bottom (r=0) to top (r=rows-1). Each row alternates
        # direction: even r -> left-to-right, odd r -> right-to-left.
        for row in range(rows):
            for column in range(columns):
                # compute visual column depending on row parity (zig-zag)
                if row % 2 == 0:
                    col = column
                else:
                    col = columns - 1 - column

                # screen coordinates: x increases left->right, y increases top->bottom
                x = margin + col * tile_size
                # r=0 is bottom row, so compute y from top as (rows-1-r)
                y = margin + (rows - 1 - row) * tile_size

                # For consistent checker pattern compute visual grid indices
                grid_x = col
                grid_y = rows - 1 - row
                color = color1 if (grid_x + grid_y) % 2 == 0 else color2

                pygame.draw.rect(self.screen, color, (x, y, tile_size, tile_size))

                # Calculate tile number (1..rows*cols)
                number = row * columns + column + 1
                num_surf = font.render(str(number), True, (0, 0, 0))
                nx = x + 10
                ny = y + 10
                self.screen.blit(num_surf, (nx, ny))

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
            self.draw_checkered_grid()
            pygame.display.flip()

            
  
            self.clock.tick(60)
