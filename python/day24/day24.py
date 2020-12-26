import os
import time
from collections import defaultdict
from functools import reduce
from operator import mul
import sys
import re


def add_t(at,bt):
    return tuple([i+j for i,j in zip(at,bt)])


def main():

    # input
    print(os.getcwd())
    print(sys.version)
    day = "24"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()
    dir_dict = {'e':(1,-1,0),'se':(0,-1,1),'sw':(-1,0,1),'w':(-1,1,0),'nw':(0,1,-1),'ne':(1,0,-1)}
    reg_dir = re.compile('e|se|sw|w|nw|ne')
    def get_neighbours(pos):
        neighs = []
        for v in dir_dict.values():
            neighs.append(add_t(pos,v))
        return neighs
    commands = []
    for l in lines:
        toks = reg_dir.findall(l)
        commands.append(toks)
    black_tiles = set()
    for coms in commands:
        pos = (0,0,0)
        for c in coms:
            pos = add_t(pos,dir_dict[c])
        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.add(pos)

    # print(len(black_tiles))
    # print(get_neighbours((0,0,0)))
    for j in range(1,101):
        # get set to check
        check_set = set()
        new_set = set()
        for b in black_tiles:
            # print(b)
            check_set.update([b])
            check_set.update(get_neighbours(b))
            # print(check_set)
        # print('cs',check_set)
        # apply rules
        for i in check_set:
            # print(i)
            ni = get_neighbours(i)
            sum_neighs = sum([1 if n in black_tiles else 0 for n in ni ])
            if i in black_tiles and 1<=sum_neighs <= 2:
                new_set.update([i])
            if i not in black_tiles and sum_neighs == 2:
                new_set.update([i])
        print(j,len(new_set))
        black_tiles = new_set.copy()
        

    
  
    # output
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
