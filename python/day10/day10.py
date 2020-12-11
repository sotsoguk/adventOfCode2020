import os
import time
#import timeit
from collections import Counter
from itertools import groupby
from functools import reduce
from operator import mul

def main():

    # input
    print(os.getcwd())
    day = "10"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # preprocess data
    num_list = sorted([int(i) for i in lines])
    num_list += [num_list[-1]+3]

    # part1
    diffs = [i-j for i, j in zip(num_list, [0]+num_list)]
    c = Counter(diffs)
    part1 = c[1] * c[3]

    # part2
    # group together 1's
    digit_groups = [list(g) for _, g in groupby(diffs)]
    group_lengths = [len(i) for i in digit_groups if i[0] == 1]

    # possibilites for the different lengths of subgroups
    num_choices = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7, 5: 13}
    sub_choices = [num_choices[i] for i in group_lengths]
    part2 = reduce(mul, sub_choices, 1)
   
    # output
    duration = int((time.time() - start_time) * 1000)

    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")
    print(num_list[1:-1])

    # part2 dynamic programming
    # reachable = {0:1}
    # for n in num_list[1:-1]:
    #     ways = 0
    #     for i in range(1,4):
    #         if (n-i) in reachable:
    #             ways += reachable[n-i]
    #     reachable[n] = ways


if __name__ == "__main__":
    main()
