import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

board = []
visited = []
ans = -sys.maxsize
k = 0
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def main():
    global board, visited, k
    n, m, k = map(int, input().split())
    board = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for y in range(n):
        s = [int(_) for _ in input().split()]
        for x in range(m):
            board[y][x] = s[x]

    go((0, 0), cnt=0, vsum=0)
    print(ans)


def go(start, cnt, vsum):
    global ans, visited
    if cnt == k:
        ans = max(ans, vsum)
        return
    st_y, st_x = start
    for y in range(st_y, len(board)):
        xx = st_x if st_y == y else 0
        for x in range(xx, len(board[0])):
            if visited[y][x]:
                continue
            ok = True
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]):
                    continue
                if visited[ny][nx]:
                    ok = False
                    break
            if ok:
                visited[y][x] = True
                go((y, x), cnt+1, vsum + board[y][x])
                visited[y][x] = False
main()
