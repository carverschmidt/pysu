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
        for row in self.grid:
            for square in row:
                pygame.draw.rect(self, BLACK, square.rect, width=1)
                    

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
           
        screen.fill(WHITE)
        
        board.draw()
        screen.blit(board, (0, 0))
        
        clock.tick(15)
        pygame.display.flip()

    pygame.quit()
        

if __name__ == '__main__':
    main()


