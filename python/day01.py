import os
import numpy as np
from itertools import combinations

import time

def main():
    # input
    print(os.getcwd())
    day = "01"
    inputFile = f'../inputs/input{day}.txt'
    print(inputFile)

    with open(inputFile) as f:
        lines = f.read().splitlines()

    nlist = [int(i) for i in lines]
    nset = set(nlist)
    target = 2020
    
    
    # print(len(lines))
    start_time = time.time()
    # for i in range(10000000):
    #     t = np.random.choice(nlist,3,replace = False)
    #     if sum(t) == target:
    #         print(i,t,t[0]*t[1]*t[2])
    #         break
    # part1
    part1 = 0
    for i in nlist:
        if (target - i) in nset:
            part1 = i * (target-i)


    # part2
    part2 = 0
    for i in range(len(nlist)):
        for j in range(i,len(nlist)):
            missing = target - (nlist[i]+nlist[j])
            if missing in nset:
                part2 = nlist[i] * nlist[j] * missing
     
    
    duration = int((time.time() - start_time) * 1000000)

    print(f"AoC 2020\nDay {day}:\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nDuration:\t{duration} ns")

    # # alternative using itertools
    # # BUT: much slower (2 ms vs 50 ms)


    # start_time2 = time.time()
    
    # for c in combinations(nlist,2):
    #     if sum(c) == target:
    #         part1 = c[0] * c[1]
    #         break

    # for c in combinations(nlist,3):
    #     if sum(c) == target:
    #         part1 = c[0] * c[1] *c[2]
    #         break

    # duration = int((time.time() - start_time2) * 1000000)
    
    # print(f"AoC 2020\nDay {day}:\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nDuration:\t{duration} ns")
if __name__ == "__main__":
    main()