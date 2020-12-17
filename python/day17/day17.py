import os
import time
from collections import defaultdict
from functools import reduce
from operator import mul
import sys
import re



class Grid3d:
    
    def __init__(self,input):
        self.data = self.read_input(input)
        self.region = self.calc_region()

    def read_input(self,lines):
        g = set()
        for i,l in enumerate(lines):
            for j,cc in enumerate(l):
                if cc == '#':
                    g.add((j,i,0))
        return g

    def count_active(self):
        return len(self.data)

    
    def calc_region(self):
        region = set()
        for p in self.data:
            region.add(p)
            region.update(self.get_n(p))
        return region

    def get_n(self,p3d):
        xp, yp, zp = p3d
        return [(x,y,z) for x in range(xp-1,xp+2) for y in range(yp-1,yp+2) for z in range(zp-1,zp+2) if not (x== xp and y== yp and z== zp)]

    def do_step(self):
        new_data = set()
        for i in self.region:
            ns = self.get_n(i)
            active_ns = sum([1 for n in ns if n in self.data])
            if i in self.data and 2<=active_ns<=3:
                new_data.add(i)
            if (i not in self.data) and active_ns == 3:
                new_data.add(i)
        self.data = new_data        
        self.region = self.calc_region()

class Grid4d:
    
    def __init__(self,input):
        self.data = self.read_input(input)
        self.xmin,self.xmax,self.ymin,self.ymax,self.zmin, self.zmax, self.wmin,self.wmax = 0,0,0,0,0,0,0,0
        self.region = self.calc_region()

    def read_input(self,lines):
        g = set()
        for i,l in enumerate(lines):
            for j,cc in enumerate(l):
                if cc == '#':
                    g.add((j,i,0,0))
        return g

    def count_active(self):
        return len(self.data)

    def calc_region(self):
        region = set()
        for p in self.data:
            region.add(p)
            region.update(self.get_n(p))
        return region
    def get_n(self,p4d):
        xp, yp, zp,wp = p4d
        return [(x,y,z,w) for x in range(xp-1,xp+2) for y in range(yp-1,yp+2) for z in range(zp-1,zp+2) for w in range(wp-1,wp+2) if not (x== xp and y== yp and z== zp and w==wp)]

    def do_step(self):
        
        new_data = set()
        for i in self.region:
            ns = self.get_n(i)
            active_ns = sum([1 for n in ns if n in self.data])
            if i in self.data and 2<=active_ns<=3:
                new_data.add(i)
            if (i not in self.data) and active_ns == 3:
                new_data.add(i)
        self.data = new_data        
        self.region = self.calc_region()


def main():

    # input
    print(os.getcwd())
    print(sys.version)
    day = "17"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # part1 & 2
    boot_process = 6
    g3d = Grid3d(lines)
    g4d = Grid4d(lines)

    # print(g3d.region)
    for _ in range(boot_process):
        g3d.do_step()
        g4d.do_step()

    part1 = g3d.count_active()
    part2 = g4d.count_active()
    # output
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
