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
                    else square.temp:
                        font = pygame.font.Font(None, 24)
                        text = font.render(str(square.val), True, BLACK)
                        self.blit(text, square.rect.center)
        if self.selected is not None:
            pygame.draw.rect(self, BLUE, self.selected.rect, width=2)

    def check_value():
        row = self.grid[self.selected.row]
        col = self.grid[:, self.selected.col]

        # get the sub square of the selected square
        if self.selected.row <= 2:
            if self.selected.col <= 2:
                square = self.grid[:2, :2]
            elif self.selected.col <= 5:
                square = self.grid[:2, 3:5]
            else:
                square = self.grid[:2, 5:]
        elif self.selected.row <= 

    
    def handle_click(self, pos):
        col = pos[0] // (self.get_width() // 9)
        row = pos[1] // (self.get_height() // 9)
        self.selected = self.grid[row][col]

    def handle_key(self, key):
        if self.selected is not None:
            if key == 13:
                self.check_val()
            elif key == 27:
                self.selected = None
            elif key >= 48 and key <= 57:
                self.selected.val = key - 48

def main():
    pygame.init()
    window_size = (540, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("pysu")
    clock = pygame.time.Clock()

    board = Board((window_size[0], window_size[0]))

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


