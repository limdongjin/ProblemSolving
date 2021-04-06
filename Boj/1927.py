import sys
import heapq
input = sys.stdin.readline

N = int(input())
min_heap = []
for _ in range(N):
    op = int(input())
    if op == 0:
        if not min_heap:
            print(0)
            continue
        print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, op)