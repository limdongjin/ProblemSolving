import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)


def solve(r, c, size):
    if size == 1:
        return r * 2 + c

    return solve(r % size, c % size, size // 2) + (c // size + (r // size) * 2) * size * size


N, r, c = [int(x) for x in input().split()]
print(solve(r, c, 2 ** (N - 1)))