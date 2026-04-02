## Map Coloring Problem using CSP (Python)

This project solves the Map Coloring problem using Constraint Satisfaction Problem (CSP) techniques for the seven regions of Australia.

## Problem Statement

Assign colors to each region such that no adjacent regions share the same color.

## Regions

- WA – Western Australia  
- NT – Northern Territory  
- SA – South Australia  
- Q – Queensland  
- NSW – New South Wales  
- V – Victoria  
- T – Tasmania  

## Constraints

- Adjacent regions cannot have the same color
- At least 3 colors are required

## Techniques Used

- Backtracking Search
- AC-3 Algorithm (Arc Consistency)
- Forward Checking
- MRV Heuristic (Minimum Remaining Values)

## Features

- Default color set (Red, Green, Blue)
- Custom color input
- Menu-driven interface
- Efficient pruning using CSP techniques
- Clean output formatting

## Algorithm Flow

1. Initialize domains for all variables
2. Apply AC-3 to reduce domains
3. Select variable using MRV heuristic
4. Assign a valid color
5. Apply forward checking
6. Backtrack if needed
7. Repeat until solution is found

## Adjacency Map

WA → NT, SA  
NT → WA, SA, Q  
SA → WA, NT, Q, NSW, V  
Q → NT, SA, NSW  
NSW → Q, SA, V  
V → SA, NSW  
T → No neighbors  

## How to Run

1. Make sure Python is installed
2. Run the file:

   python map_coloring.py

## Sample Output

Solution:

State                     Colour  
-------------------       -----  
Western Australia         Red  
Northern Territory        Green  
South Australia           Blue  
Queensland                Red  
New South Wales           Green  
Victoria                  Red  
Tasmania                  Blue  

## Requirements

- Python 3.x

## Applications

- AI Constraint Satisfaction Problems
- Scheduling problems
- Graph coloring
- Resource allocation

## Author

Shiva Reddy
