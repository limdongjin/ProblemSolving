import sys
sys.setrecursionlimit(200000000)

def main():
    n = int(input())
    board = [0 for _ in range(n)]

    for i in range(n):
        board[i] = int(input())

    cache = [0 for _ in range(n)]
    cache[0] = board[0]
    if n == 1:
        print(cache[0])
        exit()
    cache[1] = board[0] + board[1]
    if n == 2:
        print(cache[1])
        exit()
    cache[2] = max(board[0] + board[2], board[1]+board[2])

    print(solve(board, cache, n-1))


def solve(board, cache, n):
    if n < 0:
        return 0
    elif cache[n]:
        return cache[n]

    cache[n] = solve(board, cache, n-2) + board[n]
    cache[n] = max(cache[n], solve(board, cache, n-3)+board[n-1]+board[n])

    return cache[n]
main()