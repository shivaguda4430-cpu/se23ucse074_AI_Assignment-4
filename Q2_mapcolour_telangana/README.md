## Map Coloring Problem using CSP (Telangana - 33 Districts)

This project implements the Map Coloring problem using Constraint Satisfaction Problem (CSP) techniques for the 33 districts of Telangana.

## Problem Statement

Assign colors to each district such that no two adjacent districts share the same color.

## Objective

- Ensure adjacent districts have different colors
- Use a minimum set of colors efficiently
- Apply CSP techniques to find a valid solution

## Districts Considered

The model includes all 33 districts of Telangana:

Adilabad, Bhadradri Kothagudem, Hyderabad, Jagtial, Jangaon, Jayashankar Bhupalpally, Jogulamba Gadwal, Kamareddy, Karimnagar, Khammam, Komaram Bheem, Mahabubabad, Mahabubnagar, Mancherial, Medak, Medchal Malkajgiri, Mulugu, Nagarkurnool, Nalgonda, Narayanpet, Nirmal, Nizamabad, Peddapalli, Rajanna Sircilla, Rangareddy, Sangareddy, Siddipet, Suryapet, Vikarabad, Wanaparthy, Warangal Rural, Warangal Urban, Yadadri Bhuvanagiri

## Constraints

- No two neighboring districts can have the same color
- Each district must be assigned exactly one color
- At least 3 colors are required

## Techniques Used

- Backtracking Search
- AC-3 Algorithm (Arc Consistency)
- Forward Checking
- MRV Heuristic (Minimum Remaining Values)

## Features

- Efficient CSP-based solution
- Domain reduction using AC-3
- Faster solving with heuristics
- Clean and readable output
- Handles unsolvable cases

## Algorithm Flow

1. Initialize domains for all districts
2. Apply AC-3 to enforce arc consistency
3. Select district using MRV heuristic
4. Assign a valid color
5. Apply forward checking
6. Backtrack if conflict occurs
7. Continue until all districts are assigned

## Adjacency Representation

Each district is connected to its neighboring districts based on geographic boundaries.

## How to Run

1. Ensure Python 3 is installed
2. Save the file as:

   telangana_map_coloring.py

3. Run the program:

   python telangana_map_coloring.py

## Sample Output

Telangana District Map Coloring:

Adilabad                     Red  
Bhadradri_Kothagudem        Green  
Hyderabad                   Blue  
...                         ...  

## Requirements

- Python 3.x

## Applications

- Graph Coloring Problems
- AI Constraint Satisfaction Problems
- Scheduling and Resource Allocation
- Geographic Mapping

## Author

Shiva Reddy
