import os
import time
import re
import functools


def main():

    # input
    print(os.getcwd())
    day = "05"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'../inputs/input{day}.txt'

    with open(inputFile) as f:
        lines = f.read().splitlines()

    start_time = time.time()

    # part 1
    bp_min, bp_max = 1000, 0
    bpp = 0

    # def ones(x):
    #     return int(x == 'R' or x == 'B')
    ops = "".maketrans('FBLR', '0101')
    print(ops)
    for l in lines:
        # bp = 0
        # for i in l:
        #     bp <<= 1
        #     bp += ones(i)
        
        bp = int(l.translate(ops),2)
        bp_max, bp_min = max(bp_max, bp), min(bp_min, bp)
        bpp ^= bp
    part1 = bp_max

    # part2
    part2 = bpp ^ functools.reduce(
        lambda x, y: x ^ y, [i for i in range(bp_min, bp_max+1)])

    # output
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
