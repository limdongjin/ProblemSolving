import heapq
from sys import stdin
from collections import namedtuple
import sys
sys.setrecursionlimit(300001)

input = stdin.readline
Jewel = namedtuple('Jewel', 'weight price')
def solve(jewels, bags) -> int:
    bags.sort()
    jewels.sort(key=lambda jew: (jew.weight, jew.price))

    ret = 0
    mxh = []
    for weight in bags:
        while jewels and weight >= jewels[0].weight:
            heapq.heappush(mxh, -jewels[0].price)
            heapq.heappop(jewels)
        if mxh:
            ret += heapq.heappop(mxh)
        elif not jewels:
            break
    return -ret

def main():
    n, k = map(int, input().split())
    jewels = [Jewel(*map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(k)]

    print(solve(jewels, bags))


if __name__ == '__main__':
    # test()
    main()