## Sudoku Solver using CSP (Python)

This project presents an efficient solution to the Sudoku puzzle using Constraint Satisfaction Problem (CSP) techniques. The solver applies intelligent search strategies and constraint propagation to find valid solutions quickly.

## Introduction

Sudoku is a popular logic-based number placement puzzle. It consists of a 9x9 grid divided into 3x3 subgrids. Some cells are pre-filled, and the goal is to fill the remaining cells while satisfying all constraints.

This project models Sudoku as a CSP where:
- Variables represent empty cells
- Domains represent possible values (1–9)
- Constraints enforce Sudoku rules

## Problem Definition

Given a partially filled 9x9 grid:
- Fill all empty cells (denoted by 0)
- Ensure no number repeats in:
  - Any row
  - Any column
  - Any 3x3 subgrid

## CSP Formulation

### Variables
Each empty cell in the grid

### Domains
Values from 1 to 9

### Constraints
- Row constraint: No duplicate values in a row
- Column constraint: No duplicate values in a column
- Subgrid constraint: No duplicate values in each 3x3 box

## Techniques Used

### Backtracking Search
A recursive algorithm that tries assigning values to variables and backtracks when a constraint violation occurs.

### MRV Heuristic (Minimum Remaining Values)
Selects the variable with the fewest legal values left, reducing the search space and improving efficiency.

### Forward Checking
After assigning a value, it removes inconsistent values from neighboring domains to detect failure early.

## Algorithm Workflow

1. Start with the initial Sudoku grid  
2. Identify all unassigned cells  
3. Select the next variable using MRV heuristic  
4. Generate domain (possible values) for that cell  
5. Try assigning each value  
6. Apply forward checking to prune invalid choices  
7. If assignment leads to a dead end, backtrack  
8. Continue until all cells are filled  

## Input Format

- A 9x9 matrix (list of lists)
- Empty cells are represented by 0

## Output Format

- A completed 9x9 Sudoku grid
- Each row printed clearly

## Example Input

5 3 0 0 7 0 0 0 0  
6 0 0 1 9 5 0 0 0  
0 9 8 0 0 0 0 6 0  
8 0 0 0 6 0 0 0 3  
4 0 0 8 0 3 0 0 1  
7 0 0 0 2 0 0 0 6  
0 6 0 0 0 0 2 8 0  
0 0 0 4 1 9 0 0 5  
0 0 0 0 8 0 0 7 9  

## Example Output

5 3 4 6 7 8 9 1 2  
6 7 2 1 9 5 3 4 8  
1 9 8 3 4 2 5 6 7  
8 5 9 7 6 1 4 2 3  
4 2 6 8 5 3 7 9 1  
7 1 3 9 2 4 8 5 6  
9 6 1 5 3 7 2 8 4  
2 8 7 4 1 9 6 3 5  
3 4 5 2 8 6 1 7 9  

## How to Run

1. Install Python 3  
2. Save the file as:

   sudoku_solver.py  

3. Run the program:

   python sudoku_solver.py  

## Performance Considerations

- MRV significantly reduces branching factor  
- Forward checking avoids unnecessary recursion  
- Backtracking ensures completeness  

## Time Complexity

- Worst-case: O(9^(n)), where n is number of empty cells  
- Practical performance is much faster due to heuristics  

## Space Complexity

- O(n) for recursion stack  
- Additional space for domain calculations  

## Advantages of CSP Approach

- Efficient pruning of search space  
- Systematic and complete solution  
- Scales better than brute-force methods  

## Applications

- Artificial Intelligence problem solving  
- Constraint-based scheduling  
- Puzzle solving systems  
- Game development  

## Future Improvements

- Implement AC-3 for stronger constraint propagation  
- Add GUI for better visualization  
- Support different Sudoku sizes (4x4, 16x16)  
- Show step-by-step solving process  

## Conclusion

This project demonstrates how CSP techniques can effectively solve complex constraint-based problems like Sudoku. By combining heuristics and constraint propagation, the solver achieves efficient and optimal performance.

## Author

Shiva Reddy
