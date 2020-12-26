import os
import time
from collections import defaultdict
from functools import reduce
from operator import mul
import sys
import re


def main():
    day = "25"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    # output
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")

    l1,l2,i1, i2 = 13207740,8229037,2069194,16426071
    # l1,l2,i1, i2 = 8,11,5764801,17807724

    modv = 20201227
    sn = 7
    # loop size 1
    cnt1 = 1
    v = 1
    while True:
        v *= sn
        v %= modv
        if v == i1:
            break
        cnt1 += 1
        # print(cnt1)
    print('l1',cnt1)

    cnt2 = 1
    v = 1
    while True:
        v *= sn
        v %= modv
        if v == i2:
            break
        cnt2 += 1
        # print(cnt1)
    print('l2',cnt2)
    # compute encryption key
    # sn = i1
    # v = 1
    # for i in range(l2):
    #     v *= sn
    #     v %= modv
    # print(v)

    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")
if __name__ == "__main__":
    main()
