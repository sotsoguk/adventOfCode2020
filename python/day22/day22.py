import os
import time
from collections import defaultdict
from collections import deque
from functools import reduce
from operator import mul
import sys
import re
import itertools


def eval_deck(deck):
    return sum(map(lambda x: x[0] * x[1], zip(deck, range(len(deck), 0, -1))))


def play_game_rec(p1, p2, game_id):
    counter = game_id + 1
    seen = set()
    while (len(p1) * len(p2) > 0):
        hand = (tuple(p1), tuple(p2))
        if hand in seen:
            return 1
        else:
            seen.add(hand)
        p1c, p2c, winner = p1.popleft(), p2.popleft(), 0

        if len(p1) >= p1c and len(p2) >= p2c:

            winner = play_game_rec(deque(list(p1.copy())[:p1c]), deque(
                list(p2.copy())[:p2c]), counter)
            counter += 1

        else:
            winner = 1 if p1c > p2c else 2

        if winner == 1:
            p1.extend([p1c, p2c])
        else:
            p2.extend([p2c, p1c])

    if game_id == 1:
        return eval_deck(p2) if len(p1) == 0 else eval_deck(p1)

    return 2 if len(p1) == 0 else 1


def play_game(p1, p2):
    while len(p1) * len(p2) > 0:
        p1c, p2c = p1.popleft(), p2.popleft()
        if p1c > p2c:
            p1.extend([p1c, p2c])
        else:
            p2.extend([p2c, p1c])

    return eval_deck(p1) if len(p2) == 0 else eval_deck(p2)


def main():

    # input
    print(os.getcwd())
    print(sys.version)
    day = "22"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    f = open(inputFile).read()

    players = f.split('\n\n')
    p1 = deque([int(i) for i in (players[0].splitlines()[1:])])
    p2 = deque([int(i) for i in (players[1].splitlines()[1:])])

    part1 = play_game(p1.copy(), p2.copy())
    part2 = play_game_rec(p1.copy(), p2.copy(), 1)

    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
