import os
import time
import operator
import functools


def trees_on_slope(slope, grid):
    grid_w, grid_h = len(grid[0]), len(grid)
    trees = sum(grid[i][j] == 1 for i, j in [
                (i, (i*slope[0]//slope[1]) % grid_w) for i in range(0, grid_h, slope[1])])
    return trees


def main():

    # input
    print(os.getcwd())
    day = "03"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'../inputs/input{day}.txt'

    with open(inputFile) as f:
        lines = f.read().splitlines()

    start_time = time.time()
    grid = [[1 if c == '#' else 0 for c in l] for l in lines]

    # part1 / 2
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [trees_on_slope(s, grid) for s in slopes]
    part1 = trees[1]
    part2 = functools.reduce(operator.mul, trees, 1)

    # output
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
