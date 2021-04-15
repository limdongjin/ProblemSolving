import sys
input = sys.stdin.readline

def main():
    n, m = [int(_) for _ in input().split()]
    board = [int(_) for _ in input().split()]
    cache = [int(_) for _ in range(n)]
    ret = 0
    for i in range(n):
        ret = ret + board[i]
        cache[i] = ret

    for _ in range(m):
        i, j = [int(_)-1 for _ in input().split()]
        print(cache[j] - cache[i] + board[i])

main()