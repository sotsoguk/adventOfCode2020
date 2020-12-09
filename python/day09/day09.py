import os
import time
#import timeit


def sum_possible(target, nums):
    lo, hi = 0, len(nums)-1
    while lo < hi:
        currSum = nums[lo] + nums[hi]
        if currSum == target:
            return True
        elif currSum < target:
            lo += 1
        else:
            hi -= 1

    return False


def sum_subset(target, nums):
    subset_sum, lo, hi = 0, 0, 0
    while subset_sum != target and hi < len(nums):
        if subset_sum < target:
            subset_sum += nums[hi]
            hi += 1
        else:
            subset_sum -= nums[lo]
            lo += 1

    rmin, rmax = min(nums[lo:hi]), max(nums[lo:hi])
    return (rmin, rmax)


def main():

    # input
    print(os.getcwd())
    day = "09"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # preprocess data
    num_list = [int(i) for i in lines]
    pre_size = 25
    curr_list = num_list[:pre_size]

    # part1
    for i in range(pre_size, len(num_list)):
        curr_list = sorted(num_list[i-pre_size:i])
        curr_element = num_list[i]
        possible = sum_possible(curr_element, curr_list)
        if not possible:
            part1 = curr_element
            break

    # part2
    part2 = sum(sum_subset(part1, num_list))

    # output
    duration = int((time.time() - start_time) * 1000)

    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    #print(timeit.timeit(main,number=100))
    main()
