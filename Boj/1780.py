import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def main():
    n = int(input())
    board = [[0]*n for _ in range(n)]

    for y in range(n):
        s = input().split()
        for x in range(n):
            board[y][x] = int(s[x])

    ret = solve(board, (0, 0), n)

    print(ret[0])
    print(ret[1])
    print(ret[2])


def addition_tuple(a, b):
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]


def solve(board, start, n):
    y, x = start
    if n == 1:
        if board[y][x] == -1:
            return 1, 0, 0
        elif board[y][x] == 0:
            return 0, 1, 0
        elif board[y][x] == 1:
            return 0, 0, 1

    n_divide3 = n // 3

    ret = (0, 0, 0)
    for dy in range(3):
        for dx in range(3):
            d = solve(board, (y + n_divide3*dy, x + n_divide3*dx), n_divide3)
            ret = addition_tuple(d, ret)
    if ret[0] == 0 and ret[1] == 0:
        return 0, 0, 1
    elif ret[0] == 0 and ret[2] == 0:
        return 0, 1, 0
    elif ret[1] == 0 and ret[2] == 0:
        return 1, 0, 0

    return ret

main()