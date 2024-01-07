

class Solver:

    def __init__(self):
        self.matrix = [['-' for _ in range(10)] for _ in range(8)]
        self.safe_squares = []

    def update_matrix(self, new_matrix):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == '-':
                    self.matrix[i][j] = new_matrix[i][j]
        self.safe_squares = []
        self.process_matrix()
        self.process_matrix()

    def get_unopened_neighbors(self, x, y):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue  # Skip the cell itself
                nx, ny = x + i, y + j
                # Check if neighbor is within the bounds of the matrix and is unopened
                if 0 <= nx < len(self.matrix[0]) and 0 <= ny < len(self.matrix) and self.matrix[ny][nx] == '-':
                    neighbors.append((nx, ny))
        return neighbors

    def get_bomb_neighbors(self, x, y):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue  # Skip the cell itself
                nx, ny = x + i, y + j
                # Check if neighbor is within the bounds of the matrix and is unopened
                if 0 <= nx < len(self.matrix[0]) and 0 <= ny < len(self.matrix) and self.matrix[ny][nx] == 9:
                    neighbors.append((nx, ny))
        return neighbors

    def process_cell(self, x, y):
        cell = self.matrix[y][x]

        if cell in ['-', 9, 0]:
            return  # Skip if the cell is '-', '9', or '0'

        bomb_neighbors = len(self.get_bomb_neighbors(x, y))
        remaining_bombs = int(cell) - bomb_neighbors
        unopened_neighbors = self.get_unopened_neighbors(x, y)

        if len(unopened_neighbors) == remaining_bombs:
            for nx, ny in unopened_neighbors:
                self.matrix[ny][nx] = '9'
        elif remaining_bombs == 0:
            self.safe_squares.extend(unopened_neighbors)
        # self.print_matrix()

    
    def process_matrix(self):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):        
                self.process_cell(x, y)

    def get_safe_squares(self):
        return [(x+1, y+1) for (x, y) in self.safe_squares]

    def print_matrix(self):
        for row in self.matrix:
            print(' '.join([str(x) for x in row]))
        print()
        print()

