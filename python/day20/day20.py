import os
import time
from collections import defaultdict
from functools import reduce
from operator import mul
import sys
import re

def zeroes_to_int(list):
    result = 0
    for l in list:
        result <<= 1
        result += l
    return result

class Tile:
    def __init__(self, number, data,rotation = 0, flipped = False):
        self.number = number
        self.data = data
        self.rotation = rotation
        self.flipped = flipped
        self.borders = self.calc_borders()

    def calc_borders(self):
        borders = {}
        # normal borders (normal orientation)
        top = self.data[0]
        bottom = self.data[-1]
        left = [self.data[i][0] for i in range(len(self.data))]
        right = [self.data[i][-1] for i in range(len(self.data))]
        nt = zeroes_to_int(top)
        ntr = zeroes_to_int(top[::-1])
        nb = zeroes_to_int(bottom)
        nbr = zeroes_to_int(bottom[::-1])
        nl = zeroes_to_int(left)
        nlr = zeroes_to_int(left[::-1])
        nr = zeroes_to_int(right)
        nrr = zeroes_to_int(right[::-1])
        # rotated borders
        # top
        borders[0] = [nt,nlr,nbr,nr,ntr,nl,nb,nrr]
        # right 
        borders[1] = [nr,nt,nlr,nbr,nl,nb,nrr,ntr]
        # bottom
        borders[2] = [nb,nrr,ntr,nl,nbr,nr,nt,nlr]
        # left
        borders[3] = [nl,nb,nrr,ntr,nr,nt,nlr,nbr]
        
        # print(top)
        # print(nt,ntr)
        # print(bottom)
        # print(nb,nbr)
        # print(left)
        # print(nl,nlr)
        # print(right)
        # print(nr, nrr)
        #return {nt,nb,nl,nr,nrr,nlr,nbr,ntr}
        return borders

def main():

    # input
    print(os.getcwd())
    print(sys.version)
    day = "20d"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    # with open(inputFile) as f:
    #     lines = f.read().splitlines()

    f = open(inputFile).read()
    inp = f.split('\n\n')
    toks_re = re.compile('\d+')

    tiles = []
    for t in inp:
        lines = t.splitlines()
        nr = int(lines[0][5:9])
        data = []
        for t in lines[1:]:
            data_line = [1 if c=='#' else 0 for c in t ]
            #print(data_line)
            data.append(data_line)
        #print(lines[0])
        #print(t)
        # print(nr,"\n",data)
        tiles.append(Tile(nr,data))
    # part1 & 2
    # print(tiles[0].data)
    # all_b = set()
    # for t in tiles:
    #     tmp = t.borders
    #     print(sorted(list(tmp)))
    #     if not tmp.isdisjoint(all_b):
    #         print("Duplicate",t.number)
    #         # break
    #     else:
    #         all_b |= tmp
    print(tiles[0].borders)
    # print([1,0,0,0,0][::-1])
    #print(zeroes_to_int([1,0,0,0,0].reverse()))
    # output

    # part 1
    size = int(sqrt(len(tiles)))
    solution = {}
    all_tiles = dict()
    for t in tiles:
        all_tiles[t.number] = t
    
    for i in all_tiles.keys():
        solution = {}
        solution[(0,0)] = i
        remaining = all_tiles.copy()
        del remaining[i]
        for y in range(0,size):
            for x in range(0,size):
                if x==0 and y==0:
                    continue
                tileFound = False
                for r in remaining:
                    left, top = False, False
                    if x == 0:
                        left = True
                    else:
                        for d in range(8):

    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
