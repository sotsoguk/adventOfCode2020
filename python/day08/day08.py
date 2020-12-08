import os
import time
import re
import functools


def exec_code(code) ->(int,int):
    """ AoC2020 / Day 8: execute code
    
    Input:
        Code compatible with AoC2020/8

    Output:
        (exit_code, acc)

        exit_code:
            0:  code terminated normally
            -1: code runs into infinite loop

        acc:
            value of accumulator just before exiting
    """
    acc, ip = 0, 0
    seen = set()
    while True:
        if ip >= len(code):
            return (0, acc)
        elif ip in seen:
            return (-1, acc)
        else:
            seen.add(ip)
        op, arg = code[ip]

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
    _, part1 = exec_code(code)
    

    # part2
    for i, cmd in enumerate(code):
        modCode = code.copy()
        c, a = cmd
        if c % 2 == 0:
            modCode[i] = ((c+2) % 4, a)
        else:
            continue
        return_code, a = exec_code(modCode)
        if return_code == 0:
            part2 = a
            break

    
    #output
    duration = int((time.time() - start_time) * 1000)

    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
