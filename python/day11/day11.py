import os
import time
#import timeit
from collections import Counter
from itertools import groupby
from functools import reduce
from operator import mul
import copy


class Grid:
    def __init__(self, input=False):
        self.d = []
        self.cdict = {0: '.', 1: 'L', 10: '#'}
        self.rdict = {'.': 0, 'L': 1, '#': 10}
        self.rule1 = {0: 40, 1: 50}
        if not input:
            self.w = 10
            self.h = 10
            for _ in range(self.h):
                line = [0]*self.w
                self.d.append(line)
        else:
            for l in input:
                line = [self.rdict[c] for c in l]
                self.d.append(line)
            self.w, self.h = len(self.d[0]), len(self.d)
        self.seats = []
        for y in range(self.h):
            for x in range(self.w):
                if self.d[y][x] > 0:
                    self.seats.append((x,y))
                    
    def print(self):
        for i in range(self.h):
            line = "".join([self.cdict[j] for j in self.d[i]])
            print(line)

    def get_n1(self, x, y):
        ns = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                else:
                    xt, yt = x+i, y+j
                    if xt >= 0 and xt < self.w and yt >= 0 and yt < self.h:
                        ns.append((xt, yt))
        return ns

    def get_n2(self, x, y):
        def valid(x, y):
            return x >= 0 and x < self.w and y >= 0 and y < self.h
        dirs = [(1, 0), (1, 1), (0, 1), (-1, 1),
                (-1, 0), (-1, -1), (0, -1), (1, -1)]
        ns = []
        for d in dirs:
            xd, yd = d
            xt, yt = x+xd, y+yd
            while valid(xt, yt):
                if self.d[yt][xt] > 0:
                    ns.append((xt, yt))
                    break
                else:
                    xt += xd
                    yt += yd
        return ns

    def get_n(self, x, y, part2=False):
        if part2:
            return self.get_n2(x, y)
        else:
            return self.get_n1(x, y)

    def do_step(self, part2=False):
        #new_d = copy.deepcopy(self.d)
        new_d = [x[:] for x in self.d]
        changes = 0
        rule1 = self.rule1[int(part2)]
        # for y in range(self.h):
        #     for x in range(self.w):
        for x,y in self.seats:
                if self.d[y][x] == 0:
                    continue
                ns = self.get_n(x, y, part2)
                sum_ns = sum([self.d[j][i] for (i, j) in ns])

                # rule 1
                if self.d[y][x] == 1 and sum_ns < 10:
                    new_d[y][x] = 10
                    changes += 1

                elif self.d[y][x] == 10 and sum_ns >= rule1:
                    new_d[y][x] = 1
                    changes += 1

        #self.d = copy.deepcopy(new_d)
        self.d = [x[:] for x in new_d]
        return changes

    def count_occupied(self):
        count = sum([1 for i in range(self.h)
                     for j in range(self.w) if self.d[i][j] == 10])
        return count


def main():

    # input
    print(os.getcwd())
    day = "11"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # part1
    grid = Grid(lines)
    while True:
        ch = grid.do_step()
        if ch == 0:
            break
    part1 = grid.count_occupied()

    # part2
    grid = Grid(lines)
    while True:
        ch = grid.do_step(part2=True)
        if ch == 0:
            break
    part2 = grid.count_occupied()
    # output
    duration = int((time.time() - start_time) * 1000)

    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
