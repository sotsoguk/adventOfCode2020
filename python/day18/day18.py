import os
import time
from collections import defaultdict
from functools import reduce
from operator import mul
import sys
import re


def conv_to_rpn(tokens, precedence):
    rpn, stack = [], []
    operators = set(['+', '*', '(', ')'])

    for t in tokens:
        if t in operators:
            if len(stack) == 0:
                stack.append(t)
            else:
                if t == '(':
                    stack.append(t)
                elif t == ')':
                    ts = stack.pop()
                    while ts != '(':
                        rpn.append(ts)
                        ts = stack.pop()

                else:
                    t_top = stack[-1]
                    if precedence[t] > precedence[t_top]:
                        stack.append(t)
                    else:
                        rpn.append(stack.pop())
                        stack.append(t)

        else:
            rpn.append(int(t))
    while len(stack) > 0:
        rpn.append(stack.pop())
    return rpn


def eval_rpn(rpn):
    result = 0
    stack = []
    operators = set(['+', '*'])
    for t in rpn:
        if t in operators and len(stack) > 0:
            a, b = stack.pop(), stack.pop()
            if t == '+':
                stack.append(a+b)
            elif t == '*':
                stack.append(a*b)
        else:
            stack.append(t)
    return stack.pop()


def main():

    # input
    print(os.getcwd())
    print(sys.version)
    day = "18"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()

    toks_re = re.compile('\S')

    # part1 & 2
    precedence1 = {'+': 1, '*': 1, '(': 0}
    precedence2 = {'+': 2, '*': 1, '(': 0}
    for l in lines:
        toks = toks_re.findall(l)
        part1 += eval_rpn(conv_to_rpn(toks, precedence1))
        part2 += eval_rpn(conv_to_rpn(toks, precedence2))

    # output
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
