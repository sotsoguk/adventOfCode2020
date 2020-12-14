import os
import time
import timeit
from collections import Counter
from itertools import groupby
from functools import reduce
from operator import mul
import copy
import sys



def setBit(value, bit):
    return value | (1<<bit)

def clearBit(value, bit):
    return value & ~(1<<bit)

def getBit(value, bit):
    return (value >> bit) &1

def applyMask(value, mask):
    for i,b in enumerate(mask):
        if b == '0':
            value = clearBit(value,len(mask)-1-i)
        elif b == '1':
            value = setBit(value,len(mask)-1-i)
    return value

def getAddressSpace(address, mask):
    inital_address = address
    # change the 1's
    for i,b in enumerate(mask):
        if b=='1':
            inital_address = setBit(inital_address,len(mask)-i-1)
    all_address = [inital_address]
    # compute all variations of floating bits
    for i,b in enumerate(mask):
        pos = len(mask)-i-1
        if b=='X':
            tmp_address = []
            for a in all_address:
                if (getBit(a,pos)) == 1:
                    tmp_address.append(clearBit(a,pos))
                else:
                    tmp_address.append(setBit(a,pos))
            all_address.extend(tmp_address)
    return all_address

def main():

    # input
    print(os.getcwd())
    print(sys.version)
    day = "14"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # part1
    memory = dict()
    memory2 = dict()
    curr_mask = ""
    for l in lines:
        toks = l.split()
        if toks[0] == "mask":
            curr_mask = toks[2]
        else:
            curr_address = int(toks[0].split('[')[1][:-1])
            value = int(toks[2])
            memory[curr_address] = applyMask(value,curr_mask)
    
            # part2
            address2 = getAddressSpace(curr_address, curr_mask)
            for a in address2:
                memory2[a] = value
    # output
    
    part1 = sum(memory.values())
    part2 = sum(memory2.values())
    duration = int((time.time() - start_time) * 1000)

    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
