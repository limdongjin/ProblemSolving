import sys
input = sys.stdin.readline

def solve(pos, board, cache):
    n = len(board)
    y, x = pos
    if pos == (n-1, n-1):
        return True
    if y >= n or x >= n:
        return False
    if cache[y][x] != -1:
        return cache[y][x]

    d_pos = (y+board[y][x], x)
    r_pos = (y, x+board[y][x])

    cache[y][x] = solve(d_pos, board, cache) or solve(r_pos, board, cache)
    return cache[y][x]

tc = int(input())
for _ in range(tc):
    n = int(input())
    board = [[0]*n for y in range(n)]
    
    # -1: not checked , 0: False, 1: True
    cache = [[-1]*n for y in range(n)]
    
    for y in range(n):
        line = [int(_) for _ in input().split()]
        for x in range(n):
            board[y][x] = line[x]
    
    print('YES' if solve((0,0), board, cache) else 'NO')
