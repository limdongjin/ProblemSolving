import sys
from sys import stdin
import math
from collections import namedtuple
import heapq
from typing import List

input = stdin.readline
Point = namedtuple('Point', 'x y')
MAX_DIST = 8500
INF = 100000000000

class PrimeChecker:
    def __init__(self, max_number):
        self.max_number = max_number
        self._is_prime = [True for _ in range(max_number + 1)]
        self._is_prime[0] = self._is_prime[1] = False

        for x in range(int(math.sqrt(max_number)) + 1):
            if not self._is_prime[x]:
                continue
            for v in range(x + x, max_number + 1, x):
                self._is_prime[v] = False

    def is_prime(self, num):
        assert num < 8500
        return self._is_prime[num]


def dist(pos1: Point, pos2: Point) -> int:
    return int(math.sqrt(abs(pos1.y - pos2.y)**2 + abs(pos1.x - pos2.x)**2))


def dijkstra(adj, src: int) -> List[int]:
    d = [INF]*len(adj)
    d[src] = 0
    pq = []
    heapq.heappush(pq, (0, src))

    while pq:
        cost, to_ = heapq.heappop(pq)
        if d[to_] < cost:
            continue
        for weight, to_to in adj[to_]:
            next_dist = cost + weight
            if d[to_to] > next_dist:
                d[to_to] = next_dist
                heapq.heappush(pq, (next_dist, to_to))

    return d


def solve(start: Point, end: Point, villages: List[Point]) -> int:
    prime_checker = PrimeChecker(MAX_DIST)

    # build graph
    nodes = [start, *villages, end]
    n = len(nodes)
    adj = [[] for _ in range(n)]

    for id1 in range(n-1):
        for id2 in range(id1+1, n):
            d = dist(nodes[id1], nodes[id2])
            if prime_checker.is_prime(d):
                adj[id1].append((d, id2))
                adj[id2].append((d, id1))

    # dijkstra
    zero_to = dijkstra(adj, src=0)
    ret = zero_to[n-1]
    ret = -1 if ret >= INF else ret

    return ret


def main():
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    villages = [Point(*map(int, input().split())) for _ in range(n)]
    ans = solve(start=Point(x1, y1), end=Point(x2, y2), villages=villages)
    print(ans)


def test():
    assert solve(Point(1, 2), Point(5, 4),
                 [Point(4, 1), Point(6, 2)]) == 6
    assert solve(Point(1, 2), Point(5, 4), []) == -1
    assert solve(Point(1, 2), Point(5, 4), [Point(6, 2)]) == 7
    # print('test success')


if __name__ == '__main__':
    # test()
    main()
