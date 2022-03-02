import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def dfs(y, x):
    check[y][x] = True
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if board[ny][nx] == 0 or check[ny][nx]:
            continue
        dfs(ny, nx)


if __name__ == '__main__':
    board, check = [[]], [[]]
    dy, dx = [0,0,1,-1], [1,-1,0,0]
    tc = int(input())

    for _ in range(tc):
        width, height, K = map(int, input().split())
        board = [[0]*(width+2) for _ in range(height+2)]
        check = [[0]*(width+2) for _ in range(height+2)]
        for _ in range(K):
            x, y = map(int, input().split())
            board[y+1][x+1] = 1

        ans = 0
        for y in range(1, height+1):
            for x in range(1, width+1):
                if board[y][x] == 0 or check[y][x]:
                    continue
                dfs(y, x)
                ans += 1

        print(ans)