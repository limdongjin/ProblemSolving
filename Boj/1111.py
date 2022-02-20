from sys import stdin
from functools import reduce
input = stdin.readline


def solve(n, nums):
    if n == 1:
        return "A"
    elif nums[0] == nums[1]:
        return nums[0] if len(set(nums)) == 1 else "B"
    elif n == 2:
        return "A"

    a, r = divmod((nums[2] - nums[1]), (nums[1] - nums[0]))
    if r != 0:
        return "B"
    b = nums[2] - a * nums[1]

    for i in range(3, n):
        if nums[i] != a * nums[i - 1] + b:
            return "B"

    ret = a * nums[n - 1] + b

    return ret


def main():
    n = int(input())
    nums = [int(v) for v in input().split()]

    print(solve(n, nums))


main()
