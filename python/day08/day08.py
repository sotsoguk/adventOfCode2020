import os
import time
import re
import functools
from collections import deque


def exec_code(code, debug = False):
    """ exit code 0 = normal -1 = infinite loop"""
    acc, ip = 0, 0
    seen = set()
    history = deque()
    while True:
        if ip >= len(code):
            return (0, acc,history)
        elif ip in seen:
            return (-1, acc,history)
        else:
            seen.add(ip)
        op, arg = code[ip]
        if debug:
            history.appendleft((ip,(op,arg)))
        # nop
        if op == 0:
            ip += 1
        # acc
        elif op == 1:
            acc += arg
            ip += 1
        # jmp
        elif op == 2:
            ip += arg


def main():

    # input
    print(os.getcwd())
    day = "08"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()

    commands = {'nop': 0, 'acc': 1, 'jmp': 2}
    code = [(commands[l[:3]], int(l[3:])) for l in lines]

    # part1
    _, part1,hist = exec_code(code, debug = True)
    
    # part2
    while hist:
        i, (op,arg) = hist.popleft()
        
        if op%2 == 0:
            modCode = code.copy()
            modCode[i] = ((op+2) % 4,arg)
            rt,a,_ = exec_code(modCode)
            if rt == 0:
                part2 = a
                break

    #output
    duration = int((time.time() - start_time) * 1000)

    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
