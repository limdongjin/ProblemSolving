import sys
import heapq


def sync_heap(heap, sync_map):
    while heap and not sync_map[heap[0][1]]:
        heapq.heappop(heap)


input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    k = int(input())
    minheap = []
    maxheap = []
    sync_map = {}
    for i in range(k):
        op, num = input().split()
        num = int(num)
        # print(minheap)
        # print(maxheap)
        if op == 'I':
            heapq.heappush(minheap, (num, i))
            heapq.heappush(maxheap, (-num, i))
            sync_map[i] = True
            continue
        if num == 1:
            sync_heap(maxheap, sync_map)
            if maxheap:
                sync_map[maxheap[0][1]] = False
                heapq.heappop(maxheap)
        else:
            sync_heap(minheap, sync_map)
            if minheap:
                sync_map[minheap[0][1]] = False
                heapq.heappop(minheap)
    sync_heap(minheap, sync_map)
    sync_heap(maxheap, sync_map)
    if not minheap:
        print("EMPTY")
        continue
    print(maxheap[0][0]*-1, minheap[0][0])