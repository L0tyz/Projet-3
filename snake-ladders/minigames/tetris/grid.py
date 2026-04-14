import pygame

class Grid:
    def __init__(self):
        self.num_rows = 20 # nombre de carre sur le long 
        self.num_cols = 10 # nombre de carre sur le large
        self.cell_size = 30 
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] # list de zero qui se repete ,pour pas a le faire manuellement, representant la valeur de chaque case 
        #liste de couleur a utiliser
        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range (self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def get_cell_colors(self):

        gris_foncer = (26, 31, 40)
        vert = (47, 230, 23)
        rouge = (232, 18, 18)
        orange = (226, 116, 17)
        jaune = (237, 234, 4)
        mauve = (166, 0, 247)
        cyan = (21, 204, 209)
        bleu = (13, 64, 216)

        return [gris_foncer, vert, rouge, orange, jaune, mauve, cyan, bleu]
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)