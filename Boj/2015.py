from sys import stdin
from collections import defaultdict
input = stdin.readline


def solve(n, k, nums):
    d = defaultdict(int)
    psum = nums[:]
    for i in range(1, n):
        psum[i] += psum[i-1]

    ret = psum.count(k)
    for i in range(n):
        ret += d[psum[i] - k]
        d[psum[i]] += 1
    return ret


def main():
    N, K = map(int, input().split())
    A = [int(_) for _ in input().split()]

    print(solve(N, K, A))


main()