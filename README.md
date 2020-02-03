# pysu
A basic sudoku game written in python with pygame. The game includes the ability to solve itself using a backtracking algorithm. Some guy on Youtube said this would look good on a resume.

Usage
-----
```
pip3 install pygame
# then...
./pysu.py
```
Select a square by clicking on it. When a square is selected, it will be highlighted blue. Type a number 1-9 to enter a temporary value for a square. Press enter to have the game check the temporary value and make it semi-permanent if it is valid (NOTE: The entered value is checked with the current state of the board. Therefore, accepted values may not actually be the final solution for the square.). Remove any number on the board that is not original to the current puzzle by selecting the square and pressing backspace. Deselect a square by pressing the escape key. Trigger autosolving by pressing s at any time.

TODO
-----
* Refractor to better follow OO principles.
* Include the ability to show the backtracking algorithm working visually.
* Make the board look more like a Sudoku board rather than a grid of numbers.
* Add more puzzles and include a new game button to start a new random puzzle.
* Allow for the user to enter their own puzzle to solve.

