import math
from sys import stdin
from functools import reduce
from typing import List

input = stdin.readline


def predicate(cutting_length, wanted_num, given_lines):
    # Proposition:
    # 주어진 랜선들을 잘라서,
    # wanted_num 개 이상의 cutting_length 길이를 가진 랜선을 만들수 있다.

    cnt = sum(line // cutting_length for line in given_lines)
    return True if cnt >= wanted_num else False


def solve(k: int, n: int, given_lines: List[int]):
    # solve by Binary Search
    ans = 1
    low = 1  # min length
    high = max(given_lines) + 1  # max length

    while low < high:
        mid = math.floor((low + high) / 2)
        if predicate(cutting_length=mid,
                     wanted_num=n,
                     given_lines=given_lines):
            ans, low = mid, mid + 1
        else:
            high = mid

    return ans


def main():
    k, n = map(int, input().split())
    given_lines = [int(input()) for _ in range(k)]

    ans: int = solve(k, n, given_lines)

    print(ans)


main()
