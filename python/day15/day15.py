import os
import time
import timeit
from collections import defaultdict
from itertools import groupby
from functools import reduce
from operator import mul
import sys


def search_history(h,n,index):
    if n in h:
        delta = index - h[n]
        h[n] = index
        return delta
    else:
        h.update({n:index})
        return 0 

def p2(sequence, target):
    h = {sequence[x]:x+1 for x in range(len(sequence))}
    for i in range(len(sequence),target):
        sequence.append(search_history(h,sequence[i-1],i))
    return sequence[target-1]

def main():

    # input
    print(os.getcwd())
    print(sys.version)
    day = "15"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    # start_time = time.time()
    # with open(inputFile) as f:
    #     lines = f.read().splitlines()
    #real
    # input = "10,16,6,0,1,17"
    # test
    input = "3,1,2"
    #input="0,0,1"
    # target = 2020
    target = 30000000
    # part1
    input_ints = [int(i) for i in input.split(',')]
    # print(input_ints[:-1])
    # print(lut)
    # array version
    last = input_ints[-1]
    start_time = time.time()
    lut = [-1] * target
    duration = int((time.time() - start_time) * 1000)
    # for i,n in enumerate(input_ints[:-1]):
    #     lut[n] = i
    # for i in range(len(input_ints),target):
    #     # new number
    #     if lut[last] == -1:
    #         lut[last] = i-1
    #         last = 0
    #     # already seen
    #     else:
    #         d = (i-1) - lut[last]
    #         lut[last] = i-1

    #         last = d
    #     # print(i,last)
    # print(last)
    # dict version
    # lut = dict()
    # for i, n in enumerate(input_ints[:-1]):
    #     lut[n] = i
    # last = input_ints[-1]
    # for i in range(len(input_ints),target):
    #     # new number
    #     if last in lut:
    #         d = (i-1) - lut[last]
    #         lut[last] = i-1
    #         last = d
    #     # already seen
    #     else:
            
    #         lut[last] = i-1
    #         last = 0
    # print(last)
    # num_spoken = []
    # num_spoken.extend(input_ints)
    # last_spoken = defaultdict(list)
    # # last_number = input_ints[-1]
    # for i,n in enumerate(input_ints):
    #     last_spoken[n] = [i]

    # # print(last_number,last_spoken)
    # for i in range(len(input_ints),target):
    #     last_number = num_spoken[-1]
    #     curr_number = 0
    #     if len(last_spoken[last_number]) == 1:
    #         curr_number = 0
    #         num_spoken.append(0)
    #         last_spoken[0].append(i)
    #     else:
    #         curr_number = last_spoken[last_number][-1]-last_spoken[last_number][-2]
    #         num_spoken.append(curr_number)
    #         last_spoken[curr_number].append(i)
        
    #     #print(i,num_spoken,curr_number)

    # # for i in range(len(num_spoken)//10):
    # #     print(num_spoken[i*10:(i+1)*10])

    # print(max(num_spoken))
    # last_spoken = [-1]*target
    # last_num = input_ints[-1]
    # for i in range(len(input_ints),10):
    #     if last_spoken[last_num] == -1:
    #         last_spoken[last_num] = i-1
    #         last_num = 0
    #     else:
    #         tmp = (i-1) - last_spoken[last_num]
    #         last_num = tmp
    #         last_spoken[last_num] = i-1

    #     print(i,last_num,last_spoken)

    
    #print(p2(input_ints,target))
    #
    # output

    
    
    duration = int((time.time() - start_time) * 1000)

    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
