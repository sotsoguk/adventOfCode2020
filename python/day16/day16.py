import os
import time
from collections import defaultdict
from functools import reduce
from operator import mul
import sys
import re


def get_valid_tickets(rules, tickets):
    invalid = 0
    valid_tickets = []
    allrules = set().union(*[r for r in rules.values()])
    for t in tickets:
        ticket_is_valid = True
        for num in t:
            if not num in allrules:
                invalid += num
                ticket_is_valid = False
                continue
        if ticket_is_valid:
            valid_tickets.append(t)
    
    return valid_tickets, invalid

def identify_fields(rules, valid_tickets):
    # group together each column of all tickets
    pos = []
    num_fields = len(valid_tickets[0])
    for i in range(num_fields):
        pos.append(set([valid_tickets[n][i] for n in range(len(valid_tickets))]))
    
    rule_col_dict = dict()
    possible = defaultdict(list)
    for i,p in enumerate(pos):
        for rule_name, rule_range in rules.items():
            if p.issubset(rule_range):
                possible[rule_name].append(i)
    possible_names = sorted(possible, key = lambda x:len(possible[x]))
    possible_cols = list(range(len(valid_tickets[0])))
    for p in possible_names:
        for f in possible[p]:
            if f in possible_cols:
                possible_cols.remove(f)
                rule_col_dict[p] = f
    return rule_col_dict


def main():

    # input
    print(os.getcwd())
    print(sys.version)
    day = "16"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # parse input
    re_nums = re.compile('\d+')
    ## reading rules
    rules, line_cnt = dict(), 0
    
    for i,l in enumerate(lines):
        if l == "":
            line_cnt = i+2
            break
        else:
            rule_name = l.split(':')[0]
            nums = [int(i) for i in re.findall(re_nums,l)]
            range_set = set(range(nums[0],nums[1]+1)).union(set(range(nums[2],nums[3]+1)))
            rules[rule_name] = range_set
            
    ## your ticket
    ticket = [int(i) for i in lines[line_cnt].split(',')]

    ## nearby tickets
    nearby = []
    for i in range(line_cnt+3,len(lines)):
        nearby.append([int(d) for d in lines[i].split(',')])
    
    # part1
    valid_tickets, part1 = get_valid_tickets(rules,nearby)
    
    # part2
    rcd = identify_fields(rules,valid_tickets)
    part2 = reduce(mul,[ticket[v] for k,v in rcd.items() if k.startswith('departure')],1)
    
    # output
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")

   
if __name__ == "__main__":
    main()
