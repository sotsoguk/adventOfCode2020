import os
import time
from collections import defaultdict
from functools import reduce
from operator import mul
import sys
import re




def main():

    # input
    print(os.getcwd())
    print(sys.version)
    day = "21"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()

    all_ingredients_cnt = defaultdict(int)
    allergens = defaultdict(list)
    # part1 & 2

    for l in lines:
        # check if it contains allergens
        ingredients = []
        
        if l[-1] == ')':
            toks = l.split(' (')
            ingredients = toks[0].split(' ')
            al = toks[1][9:-1].split(', ')
            for a in al:
                allergens[a].append(set(toks[0].split(' ')))
        else:
            ingredients = l.split(' ')
        
        for i in ingredients:
            all_ingredients_cnt[i] += 1

    
    # for all allergens create intersect
    all_possible = set()
    intersects = {}
    for a,l in allergens.items():
        intersects[a] = set.intersection( *l)
        all_possible.update(intersects[a])
    
    for i, v in all_ingredients_cnt.items():
        if i not in all_possible:
            part1 += v
    # part2
    
    allergens_possible_ingredients = sorted(intersects,key = lambda x:len(intersects[x]))
    solution = []
    while (len(allergens_possible_ingredients) > 0):
        allergen = allergens_possible_ingredients[0]
        ing = intersects[allergen].pop()
        solution.append((allergens_possible_ingredients[0],ing))
        # delete ingredient from all allergens
        for v in intersects.values():
            if ing in v:
                v.remove(ing)
        del intersects[allergen]
        allergens_possible_ingredients = sorted(intersects,key = lambda x:len(intersects[x]))
        
        
    # sort solution
    sorted_solution = sorted(solution,key = lambda x:x[0])
    part2 = ",".join([j for i,j in sorted_solution])
    
  
    # output
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
