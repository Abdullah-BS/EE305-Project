# EE305-Project

## Table of Contents

- [Overview](#1.overview)
- [Recursive Algorithm Steps](#Recursive-Algorithm-Steps)
- [Functions](#Functions)
- [Pseudocode](#Pseudocode)
- [Conclusion](#Conclusion)


## 1. Overview
Here is a representation of a project centered around solving Sudoku puzzles using recursive backtracking algorithms. Sudoku is a popular puzzle game that relies on logic and number placement. The project's purpose is to explore the application of recursive algorithms in solving complex puzzles and to develop a practical tool for solving Sudoku. The recursive backtracking algorithm, a fundamental technique in computer science. It offers a systematic approach to solving Sudoku puzzles by iteratively exploring possible solutions and backtracking when encountering dead ends.

---

## 2. Recursive Algorithm Steps
1-	`Base Case:` The algorithm begins by checking if the Sudoku puzzle is already solved. If all cells are filled and no constraints are violated, the puzzle is considered solved, and the algorithm returns True.

2-	`Find Empty Cell:` If the puzzle is not solved, the algorithm searches for an empty cell (a cell with the value 0) in the grid. If no empty cells are found, it indicates that the puzzle is unsolvable with the current configuration.

3-	`Try Values:` For the empty cell found, the algorithm attempts to fill in each possible value from 1 to 9.

4-	`Valid Move:` Before placing a value in the cell, the algorithm checks if the move is valid. A move is considered valid if the same value does not already exist in the same row, column, or 3x3 sub grid.

5-	`Recursion:` If the move is valid, the algorithm recursively calls itself with the updated grid. This step allows the algorithm to explore all possible solutions by systematically trying different combinations of values.

6-	`Backtrack:` If no valid value can be placed in the current cell, the algorithm backtracks by resetting the cell's value to 0 and tries the next value. This backtracking mechanism allows the algorithm to explore alternative paths when a dead-end is encountered.

Repeat: Steps 2-6 are repeated until a solution is found or until all possibilities are exhausted.

---

## 3. Functions

1.	```generate()```: this function generates the sudoku problem using the dokusan library, it generates a string of numbers in the sudoku, then changes it a list of lists inside 9x9 matrix.

2. ```is_valid_move(grid, row, col, num)```: this function makes sure that the number that will be placed in the matrix is valid and doesn’t violate the puzzle rules. Shown in figure (2).

3.	```find_empty(grid)```: search for empty cells in the puzzle then returns the position of that cell in a tuple. If there are no empty cells, then it will return nothing. Shown in figure (2).

4.	```solve_sudoku(grid)```: this is the main function; it uses the functions number 2 and 3 in this list as constraints. It solves the puzzle using backtracking by finding an empty cell then trying the numbers 1-9, trying to solve the sudoku recursively. If a solution was found, it returns true, if not false. The function is shown in figure (3).


5.	```SudokuGUI:``` this is a class to show the puzzle in GUI, was made by using the Tkinter, contains the constructor method __inti__(), a printer to the terminal and a solve button.



![image](https://github.com/Abdullah-BS/EE305-Project/assets/139412761/044cddde-0869-4e19-93ed-2e9e01f23556)


![image](https://github.com/Abdullah-BS/EE305-Project/assets/139412761/c8fe1298-c14c-46cb-81c8-6e59f5f29dc0) ![image](https://github.com/Abdullah-BS/EE305-Project/assets/139412761/6ace96d5-c283-4929-924a-25475acf1df1)

---

## 4. Pseudocode

![image](https://github.com/Abdullah-BS/EE305-Project/assets/139412761/847af3ac-41cd-436d-8e6c-63b18ed4a77d)

![image](https://github.com/Abdullah-BS/EE305-Project/assets/139412761/69f14d36-091d-40ca-98ca-7dbafab04566)

---

## 5. Conclusion
This project used the recursive backtracking method which we studied in discrete mathematics, to solve a complex sudoku puzzle. The concept of recursive backtracking is about backtracking to every option available until a solution is found in which none of the constraints are violated. Using the recursive backtracking method to solve the sudoku puzzle, showed us the effectiveness of using logic and mathematics to solve problems and how fast they can be solved. This kind of project which is based on discrete mathematics will help us in solving problems we encounter in the future by using logic instead of other methods that might have disadvantages.
