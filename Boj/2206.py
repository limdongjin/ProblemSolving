import sys
from collections import deque
sys.setrecursionlimit(10000001)
input = sys.stdin.readline


def main():
    h, w = [int(_) for _ in input().split()]
    map = [[0]*w for _ in range(h)]
    for r in range(h):
        s = input()
        for c in range(w):
            map[r][c] = True if s[c] == '1' else False

    ret = solve(map)
    print(ret)


def solve(map):
    return bfs(map)
    # visited = [[False]*w for _ in range(h)]
    # return dfs((0, 0), 0)


def bfs(map):
    h = len(map)
    w = len(map[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque()
    queue.append((0, 0, 1))
    visited2 = [[[0]*w for r in range(h)] for can_break in range(2)]
    visited2[1][0][0] = 1
    while queue:
        r, c, can_break = queue.popleft()
        if r == h - 1 and c == w - 1:
            return visited2[can_break][r][c]
        for direction in directions:
            nr = r + direction[0]
            nc = c + direction[1]
            if nr < 0 or nc < 0 or nr >= h or nc >= w:
                continue
            if map[nr][nc] and can_break == 1:
                visited2[0][nr][nc] = visited2[1][r][c] + 1
                queue.append((nr, nc, 0))
            elif not map[nr][nc] and visited2[can_break][nr][nc] == 0:
                visited2[can_break][nr][nc] = visited2[can_break][r][c] + 1
                queue.append((nr, nc, can_break))

    return -1


main()


# dfs 로 구현하면 메모리 초과로 불통과한다.
# def dfs(start, cnt):
#     # global h
#     # global w
#     # global map
#     # global visited
#     r, c = start
#     if visited[r][c]:
#         # print('[-already visit]', 'cnt=', cnt, 'r=',r,'c=',c,)
#         return 10000000
#     visited[r][c] = True
#     ret = 10000000
#     global directions
#     # directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     for direction in directions:
#         nr = r + direction[0]
#         nc = c + direction[1]
#         if nr == h - 1 and nc == w - 1:
#             # print('[find]','r=',r, 'c=',c,'direc=',direction,'cnt=',cnt)
#             return 1
#         if nr < 0 or nc < 0 or nc >= w or nr >= h:
#             # print('[reject0]', 'nr=',nr,'nc=', nc, 'ret=',ret,'cnt=',cnt, 'r=',r,'c=',c,'direc=',direction)
#             continue
#         if visited[nr][nc]:
#             # print('[already visit]', 'nr=',nr,'nc=', nc, 'ret=',ret,'cnt=',cnt, 'r=',r,'c=',c,'direc=',direction)
#             continue
#
#         if map[nr][nc] and cnt == 0:
#             # print('[dfs-to-wall]','nr=',nr,'nc=', nc, 'ret=',ret,'cnt=',cnt)
#             ret = min(dfs((nr, nc), 1) + 1, ret)
#         elif not map[nr][nc]:
#             # print('[dfs]','nr=',nr,'nc=', nc, 'ret=',ret,'cnt1=',cnt)
#             ret = min(dfs((nr, nc), cnt) + 1, ret)
#         # else:
#             # print('[skip]', 'nr=',nr,'nc=', nc, 'ret=',ret,'cnt=',cnt, 'r=',r,'c=',c,'direc=',direction)
#     # visited[r][c] = False
#     # print('return')
#     return ret