import os
import time
import re
import functools
from functools import lru_cache


rules = dict()
can_gold = dict()
bags_inside_mem = dict()


def bags_inside(bag):
    if bag in bags_inside_mem.keys():
        return bags_inside_mem[bag]

    bag_rule = rules[bag]

    if not bag_rule:
        return 1
    bags = 1

    bags = sum([v*bags_inside(b) for b, v in bag_rule]) + 1
    bags_inside_mem[bag] = bags
    return bags


def part2a():
    return bags_inside('shiny gold')-1


def main():

    # input
    print(os.getcwd())
    day = "07"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # RegExs
    outer_regex = re.compile('^\w+ \w+')
    inner_regex = re.compile('\d+ \w+ \w+')

    # output
    for l in lines:
        ob = outer_regex.match(l)
        ib = inner_regex.findall(l)
        rules[ob[0]] = []
        for i in ib:
            toks = i.split()
            rules[ob[0]].append((" ".join(toks[1:]), int(toks[0])))

    part1 = sum([carry_outer(k) for k in rules.keys()])

    part2 = part2a()

    duration = int((time.time() - start_time) * 1000)

    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


def carry_outer(outer):
    for b, _ in rules[outer]:
        if carry_gold(b):
            return True
    return False


@lru_cache(maxsize=None)
def carry_gold(outer):

    if outer == 'shiny gold':
        return True
    subrules = rules[outer]
    if not subrules:
        return False
    for b, _ in rules[outer]:
        if carry_gold(b):
            return True
    return False


if __name__ == "__main__":
    main()
