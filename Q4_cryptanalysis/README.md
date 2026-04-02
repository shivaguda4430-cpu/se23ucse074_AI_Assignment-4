## Cryptarithmetic Puzzle using CSP (SEND + MORE = MONEY)

This project implements the classic cryptarithmetic puzzle SEND + MORE = MONEY using Constraint Satisfaction Problem (CSP) techniques in Python.

## Problem Statement

Each letter represents a unique digit (0–9). The goal is to find a mapping such that:

SEND  
+ MORE  
= MONEY  

## Objective

- Assign digits to letters  
- Ensure no two letters share the same digit  
- Leading digits (S and M) cannot be zero  
- The arithmetic equation must be satisfied  

## Variables

S, E, N, D, M, O, R, Y  

## Domains

Each variable can take values from 0 to 9  

## Constraints

- All digits must be unique  
- S ≠ 0 and M ≠ 0  
- SEND + MORE = MONEY  

## Techniques Used

- Backtracking Search  
- Constraint Checking  
- Early Pruning  
- Recursive Problem Solving  

## Algorithm Flow

1. Select an unassigned variable  
2. Assign a digit from 0–9  
3. Check constraints  
4. If valid, continue recursively  
5. If invalid, backtrack  
6. Stop when solution is found  

## How to Run

1. Install Python 3  
2. Save file as:

   crypto_solver.py  

3. Run:

   python crypto_solver.py  

## Sample Output

Solution:

D = 7  
E = 5  
M = 1  
N = 6  
O = 0  
R = 8  
S = 9  
Y = 2  

## Explanation

SEND  = 9567  
MORE  = 1085  
MONEY = 10652  

9567 + 1085 = 10652  

## Time Complexity

- Worst case: O(10!)  
- Reduced using pruning and constraints  

## Applications

- Artificial Intelligence (CSP problems)  
- Puzzle solving systems  
- Constraint optimization problems  

## Advantages

- Systematic search approach  
- Guarantees correct solution  
- Efficient with pruning  

## Future Improvements

- Add GUI visualization  
- Support dynamic puzzles  
- Implement MRV heuristic  
- Add AC-3 algorithm  

## Author

Shiva Reddy
