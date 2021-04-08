import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def solve(board, height):
    n = len(board)
    visited = [[False]*n for _ in range(n)]
    ret = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and board[r][c] > height:
                dfs(board, visited, (r, c), height)
                ret = ret + 1
    return ret

def dfs(board, visited, rc, h):
    r, c = rc
    n = len(board)
    visited[r][c] = True
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for direction in range(4):
        nr = r + dx[direction]
        nc = c + dy[direction]
        if nr < 0 or nr >= n or nc >= n or nc < 0:
            continue
        if board[nr][nc] <= h:
            continue
        if visited[nr][nc]:
            continue
        dfs(board, visited, (nr, nc), h)

n = int(input())
board = [[0]*n for _ in range(n)]
min_val = 1000
max_val = -1
for i in range(n):
    inp = [int(_) for _ in input().split()]
    for j in range(n):
        board[i][j] = inp[j]
        min_val = min(board[i][j], min_val)
        max_val = max(board[i][j], max_val)

ret = -1
for height in range(0, max_val+1):
    ret = max(ret, solve(board, height))

print(ret)