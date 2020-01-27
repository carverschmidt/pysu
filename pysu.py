#!/usr/local/bin/python3
"""
pysu is a python implementation of the game Sudoku.

The game also includes the ability to solve itself using a backtracking
algorithm.

author: Carver Schmidt <cjs5194@rit.edu>
"""

import pygame

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class Square:
    def __init__(self, rect, row, col):
        self.rect = rect
        self.row = row
        self.col = col
        self.val = None
        self.og = False
        self.temp = True


class Board(pygame.Surface):
    def __init__(self, size):
        super().__init__(size)

        # initialize grid
        self.grid = []
        for row in range(9):
            r = []
            for col in range(9):
                rect = pygame.Rect((self.get_width() // 9) * col,
                                    (+ self.get_height() // 9) * row,
                                    self.get_width() // 9, self.get_height() // 9)
                r.append(Square(rect, row, col))
            self.grid.append(r)

        # selected square for input
        self.selected = None

    def new_puzzle(self, puzzle=None):
        if puzzle == None:
            puzzle = [[0,0,4,3,0,0,2,0,9],
                      [0,0,5,0,0,9,0,0,1],
                      [0,7,0,0,6,0,0,4,3],
                      [0,0,6,0,0,2,0,8,7],
                      [1,9,0,0,0,7,4,0,0],
                      [0,5,0,0,8,3,0,0,0],
                      [6,0,0,0,0,0,1,0,5],
                      [0,0,3,5,0,8,6,9,0],
                      [0,4,2,9,1,0,3,0,0]] 

        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != 0:
                    self.grid[i][j].val = puzzle[i][j]
                    self.grid[i][j].og = True
                    self.grid[i][j].temp = False
                 
    def draw(self):
        self.fill(WHITE)
        for row in self.grid:
            for square in row:
                pygame.draw.rect(self, BLACK, square.rect, width=1)
                if square.val is not None:
                    if square.temp:
                        font = pygame.font.Font(None, 32)
                        text = font.render(str(square.val), True, BLACK)
                        alpha = pygame.Surface(text.get_size(), pygame.SRCALPHA)
                        alpha.fill((255, 255, 255, 140))
                        text.blit(alpha, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                        self.blit(text, (square.rect.x + 5, square.rect.y + 5))
                    else:
                        font = pygame.font.Font(None, 48)
                        text = font.render(str(square.val), True, BLACK)
                        text_rect = text.get_rect()
                        self.blit(text, (square.rect.centerx - text_rect.width / 2,
                                        square.rect.centery - text_rect.height // 2))
        if self.selected is not None:
            pygame.draw.rect(self, BLUE, self.selected.rect, width=2)

    def check_value(self):
        row = self.grid[self.selected.row]
        col = [r[self.selected.col] for r in self.grid] 

        # get the sub matrix of the grid for the selected square
        if self.selected.row <= 2:
            if self.selected.col <= 2:
                sub_matrix = [r[:3] for r in self.grid[:3]]
            elif self.selected.col <= 5:
                sub_matrix = [r[3:6] for r in self.grid[:3]]
            else:
                sub_matrix = [r[6:] for r in self.grid[:3]]
        elif self.selected.row <= 5:
            if self.selected.col <= 2:
                sub_matrix = [r[:3] for r in self.grid[3:6]]
            elif self.selected.col <= 5:
                sub_matrix = [r[3:6] for r in self.grid[3:6]]
            else:
                sub_matrix = [r[6:] for r in self.grid[3:6]]
        else:
            if self.selected.col <= 2:
                sub_matrix = [r[:3] for r in self.grid[6:]]
            elif self.selected.col <= 5:
                sub_matrix = [r[3:6] for r in self.grid[6:]]
            else:
                sub_matrix = [r[6:] for r in self.grid[6:]]

        # check if value exists in row, col, or sub matrix
        invalid = False
        for square in row:
            if not square.temp and square.val == self.selected.val:
                invalid = True
                print('invalid entry!')
        for square in col:
            if not square.temp and square.val == self.selected.val:
                invalid = True
                print('invalid entry!')
        for row in sub_matrix:
            for square in row:
                if not square.temp and square.val == self.selected.val:
                    invalid = True
                    print('invalid entry!')
        if not invalid:
            self.selected.temp = False

    def handle_click(self, pos):
        col = pos[0] // (self.get_width() // 9)
        row = pos[1] // (self.get_height() // 9)
        self.selected = self.grid[row][col]

    def handle_key(self, key):
        if self.selected is not None:
            if key == 8:
                if not self.selected.og:
                    self.selected.val = None
            if key == 13:
                self.check_value()
            elif key == 27:
                self.selected = None
            elif key >= 49 and key <= 57:
                if self.selected.temp:
                    self.selected.val = key - 48

def main():
    pygame.init()
    window_size = (540, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("pysu")
    clock = pygame.time.Clock()

    board = Board((window_size[0], window_size[0]))
    board.new_puzzle()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < board.get_width() and pos[1] < board.get_height():
                    board.handle_click(pos)
            if event.type == pygame.KEYDOWN:
                if event.mod == pygame.KMOD_NONE:
                    board.handle_key(event.key)
           
        screen.fill(WHITE)
        
        board.draw()
        screen.blit(board, (0, 0))
        
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
        

if __name__ == '__main__':
    main()

