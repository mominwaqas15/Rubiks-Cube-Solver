# Rubik's Cube Solver

## Overview
This project aims to solve the Rubik's Cube puzzle using the Iterative Deepening A* (IDA*) search algorithm. The solver employs a heuristic function to estimate the distance from the current state of the cube to the goal state. It utilizes a Python implementation of the Rubik's Cube and IDA* algorithm.

## Features
- Solves the Rubik's Cube from any valid starting configuration
- Supports cubes of different sizes (e.g., 2x2, 3x3)
- Computes and utilizes a heuristic function to guide the search
- Provides a command-line interface for running the solver and displaying the solution steps
- Optional visualization of cube state after each move

## Usage
1. Install Python 3.11 if not already installed.
2. Clone the repository: `git clone https://github.com/mominwaqas15/Rubiks-Cube-Solver.git`
3. Navigate to the project directory: `cd rubiks-cube-solver`
4. Run the solver: `python main.py`

## Configuration
- `MAX_MOVES`: Maximum number of moves allowed for scrambling the cube and searching for the solution.
- `NEW_HEURISTICS`: Flag to determine whether to compute new heuristic values or load from a precomputed file.
- `HEURISTIC_FILE`: File path for storing precomputed heuristic values (if `NEW_HEURISTICS` is set to `False`).

## Files
- `main.py`: Main script for running the Rubik's Cube solver.
- `cube.py`: Python implementation of the Rubik's Cube.
- `solver.py`: Implementation of the Iterative Deepening A* (IDA*) search algorithm.

## Contributors
- [Momin Waqas](https://github.com/mominwaqas15)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
