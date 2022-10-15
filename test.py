from fifteen_puzzle_solvers.puzzle import Puzzle
from fifteen_puzzle_solvers.algorithms import AStar, BreadthFirst
from fifteen_puzzle_solvers.solver import PuzzleSolver

puzzle = Puzzle([[1, 2, 3, 4], [5, 6, 7, 8], [0, 10, 11, 12], [9, 13, 14, 15]])

for strategy in [BreadthFirst, AStar]:
    puzzle_solver = PuzzleSolver(strategy(puzzle))
    puzzle_solver.run()
    puzzle_solver.print_performance()
    puzzle_solver.print_solution()