import sys
from collections import deque
sys.setrecursionlimit(200000000)
input = sys.stdin.readline

def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        r, c = [int(_) for _ in input().split()]
        to_r, to_c = [int(_) for _ in input().split()]

        print(solve((r, c), (to_r, to_c), n))


def solve(from_position, to_position, n):
    r, c = from_position
    to_r, to_c = to_position
    if r == to_r and c == to_c:
        return 0
    return bfs((r, c), (to_r, to_c), n)


def bfs(from_position, to_position, n):
    queue = deque()
    queue.append(from_position)
    visited = [[False]*n for _ in range(n)]
    visited[from_position[0]][from_position[1]] = True
    level = 0
    directions = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, -1), (2, 1)]
    while queue:
        size = len(queue)
        level = level + 1
        for i in range(size):
            r, c = queue.popleft()
            # print(r, c)
            # print('level ', level)
            # print(size)
            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]
                if nr < 0 or nc < 0 or nr >= n or nc >= n:
                    continue
                if visited[nr][nc]:
                    continue
                if nr == to_position[0] and nc == to_position[1]:
                    return level
                queue.append((nr, nc))
                visited[nr][nc] = True
    return level
main()