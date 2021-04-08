import sys
from collections import deque
sys.setrecursionlimit(20000000)
input = sys.stdin.readline


def solve():
    global board
    global comps
    global zl
    global yl
    global xl

    visited = [[[False]*xl for y in range(yl)] for z in range(zl)]
    queue = comps
    dx = [0, 1, 0, -1, 0, 0]
    dy = [-1, 0, 1, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    ret = 0

    while queue:
        size = len(queue)
        ret = ret + 1
        for _ in range(size):
            pos = queue.popleft()
            visited[pos[0]][pos[1]][pos[2]] = True
            board[pos[0]][pos[1]][pos[2]] = 1

            for direction in range(6):
                nz = pos[0] + dz[direction]
                ny = pos[1] + dy[direction]
                nx = pos[2] + dx[direction]
                if nx < 0 or ny < 0 or nz < 0 or nx >= xl or ny >= yl or nz >= zl:
                    continue
                if board[nz][ny][nx] != 0 or visited[nz][ny][nx]:
                    continue

                queue.append((nz, ny, nx))

    for z in range(zl):
        for y in range(yl):
            for x in range(xl):
                if board[z][y][x] == 0:
                    return -1

    return ret - 1


xl, yl, zl = (int(_) for _ in input().split())
board = [[ [[] for x in range(xl)] for y in range(yl)] for z in range(zl)]
comps = deque()
flag = False
for z in range(zl):
    for y in range(yl):
        inp = (int(_) for _ in input().split())
        for x in range(xl):
            board[z][y][x] = next(inp)
            if board[z][y][x] == 1:
                comps.append((z, y, x))
            if board[z][y][x] == 0:
                flag = True
if not flag:
    print(0)
else:
    print(solve())