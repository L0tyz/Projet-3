import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20 # nombre de carre sur le long 
        self.num_cols = 10 # nombre de carre sur le large
        self.cell_size = 30 
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] # list de zero qui se repete ,pour pas a le faire manuellement, representant la valeur de chaque case 
        #liste de couleur a utiliser
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range (self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)