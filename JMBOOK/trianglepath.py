import sys
input = sys.stdin.readline
def solve(board, n):
    cache = [[-1]*(n+1) for _ in range(n+1)]
    
    def _path(y, x):
        if y == n - 1:
            return board[y][x]
        if cache[y][x] != -1:
            return cache[y][x]

        cache[y][x] = board[y][x] + max(_path(y+1, x), _path(y+1, x+1))
        return cache[y][x]

    return _path(y=0,x=0)

TC = int(input())
board = [[0]*101 for _ in range(101)]
for _ in range(TC):
    n  = int(input())
    for y in range(n):
        line = list(map(int, input().split()))
        for x in range(y+1):
            board[y][x] = line[x]

    print(solve(board, n))

