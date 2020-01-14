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
    def __init__(self, rect):
        self.rect = rect
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
                r.append(Square(rect))
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
                        font = pygame.font.Font(None, 18)
                        text = font.render(str(square.val), True, BLACK)
                        self.blit(text, (0, 0))
                    elif not square.temp:
                        font = pygame.font.Font(None, 24)
                        text = font.render(str(square.val), True, BLACK)
                        self.blit(text, (0, 0))
        if self.selected is not None:
            pygame.draw.rect(self, BLUE, self.selected.rect, width=2)


    def handle_click(self, pos):
        col = pos[0] // (self.get_width() // 9)
        row = pos[1] // (self.get_height() // 9)
        self.selected = self.grid[row][col]

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
           
        screen.fill(WHITE)
        
        board.draw()
        screen.blit(board, (0, 0))
        
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
        

if __name__ == '__main__':
    main()


