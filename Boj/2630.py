import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)


def addition_tuple(tup1, tup2):
    return tuple(t1+t2 for t1, t2 in zip(tup1, tup2))


def solve(board, r, c, size):
    if size == 1:
        #      blue, white
        return board[r][c], 1 - board[r][c]
    half_size = size // 2
    d1 = solve(board, r=r, c=c, size=half_size)
    d2 = solve(board, r=r, c=c + half_size, size=half_size)
    d3 = solve(board, r=r + half_size, c=c, size=half_size)
    d4 = solve(board, r=r + half_size, c=c + half_size, size=half_size)

    dsum = addition_tuple(d1, d2)
    dsum = addition_tuple(dsum, d3)
    dsum = addition_tuple(dsum, d4)

    if dsum[1] == 0:
        dsum = (1, 0)
    elif dsum[0] == 0:
        dsum = (0, 1)

    return dsum


N = int(input())
board = [[0] * N for _ in range(N)]
for r in range(N):
    s: list = input().split()
    for c in range(N):
        board[r][c] = int(s[c])

blue, white = solve(board, r=0, c=0, size=N)
print(white)
print(blue)
