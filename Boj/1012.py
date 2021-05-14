import sys
sys.setrecursionlimit(2500*2500)
def dfs(map, point, ret):
    r, c = point

    dx = [0, 1, 0, -1]
    dy = [-1,0,1,0]
    for direction in range(4):
        nr = r + dy[direction]
        nc = c + dx[direction]
        if nr < 0 or nc < 0 or nr >= len(map) or nc >= len(map[0]) or map[nr][nc] != -1:
            continue
        map[nr][nc] = ret
        dfs(map, (nr, nc), ret)

tc = int(input())
for _ in range(tc):
    width, height, K = [int(x) for x in input().split()]
    map = [[0]*width for i in range(height)]
    points = []
    for i in range(K):
        c, r = [int(x) for x in input().split()]
        map[r][c] = -1
        points.append((r, c))
    ret = 1
    for point in points:
        if map[point[0]][point[1]] != -1:
            continue
        dfs(map, point, ret)
        ret = ret + 1
    print(ret - 1)
