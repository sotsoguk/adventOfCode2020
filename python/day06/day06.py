import os
import time
import re
import functools


def main():

    # input
    print(os.getcwd())
    day = "06"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'../inputs/input{day}.txt'

    with open(inputFile) as f:
        lines = f.read().splitlines()

    start_time = time.time()

    set_1, set_2 = set(), set("abcdefghijklmnopqrstuvwxyz")
    all_1, all_2 = [], []

    # part 1
    for l in lines:
        if l == "":
            all_1.append(set_1)
            all_2.append(set_2)
            set_1 = set()
            set_2 = set("abcdefghijklmnopqrstuvwxyz")
        else:
            set_2 = set_2.intersection(set(l))
            set_1 = set_1.union(set(l))

    all_1.append(set_1)
    all_2.append(set_2)

    part1 = sum([len(i) for i in all_1])
    part2 = sum([len(i) for i in all_2])

    # output
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
