import os
import time
#import timeit
from collections import Counter
from itertools import groupby
from functools import reduce
from operator import mul
import cmath


class Mover:
    def __init__(self, start_pos=complex(0, 0), start_dir=complex(1, 0)):
        self.pos = start_pos
        self.direction = start_dir
        self.compass = {'N': complex(0, 1), 'S': complex(
            0, -1), 'W': complex(-1, 0), 'E': complex(1, 0)}

    def move_forward(self, steps=1):
        self.pos += steps * self.direction

    def turn_left(self, steps_90=1):
        for _ in range(steps_90):
            self.direction *= complex(0, 1)

    def turn_right(self, steps_90=1):
        for _ in range(steps_90):
            self.direction *= complex(0, -1)

    def move_direction(self, com_dir, steps=1):
        for _ in range(steps):
            self.pos += self.compass[com_dir]

    def get_distance_origin_manhattan(self):
        return abs(self.pos.real) + abs(self.pos.imag)


class Mover2:
    def __init__(self, ship_pos=complex(0, 0), way_pos=complex(10, 1)):
        self.ship_pos = ship_pos
        self.way_pos = way_pos
        self.compass = {'N': complex(0, 1), 'S': complex(
            0, -1), 'W': complex(-1, 0), 'E': complex(1, 0)}

    def move_forward(self, steps=1):
        self.ship_pos += steps * self.way_pos

    def turn_left(self, steps_90=1):
        for _ in range(steps_90):
            self.way_pos *= complex(0, 1)

    def turn_right(self, steps_90=1):
        for _ in range(steps_90):
            self.way_pos *= complex(0, -1)

    def move_direction(self, com_dir, steps=1):
        for _ in range(steps):
            self.way_pos += self.compass[com_dir]

    def get_distance_origin_manhattan(self):
        return abs(self.ship_pos.real) + abs(self.ship_pos.imag)


def main():

    # input
    print(os.getcwd())
    day = "12"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # part1 & part 2
    movers = [Mover(), Mover2()]

    for l in lines:
        cmd, arg = l[0], int(l[1:])
        if cmd == 'F':
            for i in [0, 1]:
                movers[i].move_forward(arg)
        elif cmd == 'R':
            for i in [0, 1]:
                movers[i].turn_right(arg//90)
        elif cmd == 'L':
            for i in [0, 1]:
                movers[i].turn_left(arg//90)
        else:
            for i in [0, 1]:
                movers[i].move_direction(cmd, arg)

    part1 = int(movers[0].get_distance_origin_manhattan())
    part2 = int(movers[1].get_distance_origin_manhattan())

    # output
    duration = int((time.time() - start_time) * 1000)

    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
