import sys
import heapq
input = sys.stdin.readline
N = int(input())
maxheap = []
for _ in range(N):
    op = int(input())
    # breakpoint()
    if op == 0:
        if not maxheap:
            print(0)
            continue
        print(heapq.heappop(maxheap)[1])
    else:
        heapq.heappush(maxheap, (-op, op))