import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000000)


def solve(map, lands):
    w = len(map[0])
    h = len(map)
    visited = [[False]*w for _ in range(h)]

    ret = 0
    for land in lands:
        if not visited[land[0]][land[1]]:
            dfs(map, visited, land)
            ret = ret + 1
    return ret


def dfs(map, visited, land):
    r, c = land
    visited[r][c] = True

    dr = [-1, 0,1,0,-1,-1,1,1]
    dc = [0,1,0,-1,-1,1,1,-1]
    for direction in range(8):
        nr = r + dr[direction]
        nc = c + dc[direction]
        if nr < 0 or nc < 0 or nc >= len(map[0]) or nr >= len(map):
            continue
        if map[nr][nc] != 1:
            continue
        if visited[nr][nc]:
            continue
        dfs(map, visited, (nr, nc))


while True:
    w, h = [int(_) for _ in input().split()]
    if w == 0 and h == 0:
        break
    map = [[0]*w for _ in range(h)]
    lands = []
    for r in range(h):
        inp = [int(_) for _ in input().split()]
        for c in range(w):
            map[r][c] = inp[c]
            if inp[c] == 1:
                lands.append((r, c))

    print(solve(map, lands))