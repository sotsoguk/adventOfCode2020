import os
import time

def main():
    # input
    print(os.getcwd())
    day = "02"
    part1, part2 = 0, 0
    starLine = "*" * 19
    inputFile = f'../inputs/input{day}.txt'

    with open(inputFile) as f:
        lines = f.read().splitlines()
    
    start_time = time.time()

    for l in lines[:]:
        # extract data

        toks = l.split()
        minOcc, maxOcc = [int(i) for i in toks[0].split('-')]
        char, password = toks[1][0], toks[2]
        occ = sum([1 for c in password if c == char])

        # part 1
        if minOcc <= occ <= maxOcc:
            part1 += 1

        # part 2
        if bool(password[minOcc-1] == char) ^ bool(password[maxOcc-1] == char):
            part2 += 1

    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{starLine}\n AoC 2020 - Day {day}\n{starLine}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
