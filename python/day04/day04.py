import os
import time
import re


def passport_part2_valid(p):
    # byr
    if not (1920 <= int(p['byr']) <= 2020):
        return False

    # iyr
    if not (2010 <= int(p['iyr']) <= 2020):
        return False

    # eyr
    if not (2020 <= int(p['eyr']) <= 2030):
        return False

    # hcl
    match = re.search(r'^#(?:[0-9a-fA-F]{6})$', p['hcl'])
    if not match:
        return False

    # hgt
    if not ((p['hgt'].endswith('in') and 59 <= int(p['hgt'][:-2]) <= 76) or (p['hgt'].endswith('cm') and 150 <= int(p['hgt'][:-2]) <= 193)):
        return False
    # ecl
    valid_ecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if not (p['ecl'] in valid_ecl):
        return False

    # pid
    match_pid = re.search('^\d{9}$', p['pid'])
    if not match_pid:
        return False

    return True


def main():

    # input
    print(os.getcwd())
    day = "04"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'../inputs/input{day}.txt'

    with open(inputFile) as f:
        lines = f.read().splitlines()

    start_time = time.time()
    fields = dict()
    passports, valid_passports = [], []
    for l in lines:
        if l == "":
            passports.append(fields)
            fields = dict()
        else:
            toks = l.split()
            for t in toks:
                k, v = t.split(':')
                fields[k] = v
    passports.append(fields)
    required_1 = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for p in passports:
        if p.keys() >= required_1:
            part1 += 1
            valid_passports.append(p)

    # part2
    part2 = sum([1 for p in valid_passports if passport_part2_valid(p)])

    # output
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")

    match = re.search('^\d{9}$', "00000000")
    if match:
        print("True")


if __name__ == "__main__":
    main()
