import os
import time
from collections import defaultdict
from functools import reduce
from operator import mul
import sys
import re




def check_cfg(rules, rule_nr, word, pos):
    rule = rules[rule_nr]
    # if rule is terminal (starts with a "")
    if rule[0][0][0] == '"':
        if pos < len(word) and word[pos] == rule[0][0][1]:
            return {pos+1}
        else:
            return set() # word cant be expressed with grammar
    else:
        suffixes = set()
        for subrule in rule:
            buf = {pos}
            for p in subrule:
                tmp = set()
                for l in buf:
                    # tmp.union(check_cfg(rules,p,word,l))
                    tmp |= check_cfg(rules,p,word,l)
                buf = tmp
            # suffixes = suffixes.union(buf)
            suffixes |=  buf
        return suffixes

def main():

    # input
    print(os.getcwd())
    print(sys.version)
    day = "19"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    # with open(inputFile) as f:
    #     lines = f.read().splitlines()

    f = open(inputFile).read()
    inp = f.split('\n\n')
    # rules
    lines_rules = inp[0].splitlines()
    rules = {}
    for line in lines_rules:
        toks = line.split(': ')
        rule_nr = toks[0]
        rule = [s.split(' ') for s in toks[1].split(' | ')]
        rules[rule_nr] = rule

    # print(rules)
    # messages received
    messages = inp[1].splitlines()
    # print(messages)



    # part1 & 2

    results = [len(word) in check_cfg(rules,'0',word,0) for word in messages]
    part1 = results.count(True)

    # part2
    rules['8'] = [['42'],['42','8']]
    rules['11'] = [['42','31'],['42','11','31']]

    results = [len(word) in check_cfg(rules,'0',word,0) for word in messages]
    part2 = results.count(True)
    # output
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
