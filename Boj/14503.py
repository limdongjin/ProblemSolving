import sys
input = sys.stdin.readline

def dfs(r, c, d):
    if not visited[r][c]:
        global ans
        visited[r][c] = 1
        ans += 1
    
    # a, b logic
    for _ in range(4):
        d = left[d]
        lr, lc = r+dirs[d][0], c+dirs[d][1]
        if board[lr][lc] != 1 and not visited[lr][lc]:
            dfs(lr, lc, d)
            return

    # c logic
    bd = (-1*d[0], -1*d[1])
    br, bc = r+dirs[bd][0], c+dirs[bd][1]
    if board[br][bc] != 1:
        dfs(br, bc, d)
        return

    # d logic
    return
    

ans = 0
N, M = map(int, input().split())

# robot position
rr, rc, d = map(int, input().split())
rr, rc = rr+1, rc+1

board = [[1]*(M+2) for r in range(N+2)]
visited = [[0]*(M+2) for r in range(N+2)]

dirs = [(-1, 0), (0, 1), (1, 0),(0,-1)]
left = {0: 3, 1: 0, 2: 1, 3: 2}
# up, right, down, left

for r in range(1, N+1):
    s = list(map(int, input().split()))
    for c in range(1,M+1):
        board[r][c] = s[c-1]

dfs(rr, rc, d)
print(ans)

