from collections import deque
from typing import Deque, List
import sys
input = sys.stdin.readline

def bfs(box_map: List, queue: Deque['tuple']):
    is_valid_point = lambda r, c: 0 <= r < len(box_map) and 0 <= c < len(box_map[0])
    can_visit = lambda r, c: box_map[r][c] == 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while queue:
        qsize = len(queue)
        for _ in range(qsize):
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dy[i]
                nc = c + dx[i]
                if not is_valid_point(nr, nc):
                    continue
                if not can_visit(nr, nc):
                    continue
                box_map[nr][nc] = box_map[r][c] + 1
                queue.append((nr, nc))


width, height = (int(x) for x in input().split())
box_map = []
starting_points: Deque['tuple'] = deque()
for r in range(height):
    box_row = []
    for i, num in enumerate(input().split()):
        n = int(num)
        box_row.append(n)
        if n == 1:
            starting_points.append((r, i))
    box_map.append(box_row)

if len(starting_points) == 0:
    print(0)
    exit()

bfs(box_map, starting_points)

max_value = 0
for row in box_map:
    for col in row:
        if col == 0:
            print(-1)
            exit()
        max_value = max(max_value, col)

print(max_value - 1)