# DS Engineer Test Task

This repository contains solutions for the ML/DS test tasks.

The project uses **uv** for fast Python dependency management.

## Project Structure
- `task1_isl/` - Task 1: Counting islands (DFS algorithm)
- `task2_reg/` - Task 2: Tabular data regression (EDA, Train, Predict)
- `task3_archtr/` - Task 3: OOP MNIST Classifier architecture


## Environment Setup

Install **uv** (Python package manager):

2. Run `uv sync` to install dependencies (or use `pip install -r requirements.txt`).

## Task 1: Counting Islands
Run the solution:
`python task1_isl/solution.py < input.txt`

The program reads the grid from **stdin** and outputs the number of islands.
This solution counts the number of islands in a 2D grid.

## Approach
The algorithm uses iterative DFS with an explicit stack.
Each time a land cell (`1`) is found, a flood-fill is performed to mark the whole island as visited.

## Complexity
- Time: O(m * n)
- Space: O(m * n) in the worst case due to the stack

## Input format
The program reads from standard input:
- first line: `m n`
- next `m` lines: `n` integers (`0` or `1`)

## Example
Input:
3 4
1 1 0 0
0 1 0 1
0 0 1 1

Output:
2