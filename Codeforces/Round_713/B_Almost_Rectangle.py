import sys
input = sys.stdin.readline

def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        board = [['.']*n for _ in range(n)]
        stars = []
        for y in range(n):
            s = input().rstrip()
            for x in range(n):
                if s[x] == '*':
                    board[y][x] = '*'
                    stars.append((y, x))

        if stars[0][0] == stars[1][0]: # same y
            if stars[0][0] != n - 1:
                board[stars[0][0]+1][stars[0][1]] = '*'
                board[stars[1][0]+1][stars[1][1]] = '*'
            else:
                board[stars[0][0]-1][stars[0][1]] = '*'
                board[stars[1][0]-1][stars[1][1]] = '*'
        elif stars[0][1] == stars[1][1]: # same x
            if stars[0][1] != n-1:
                board[stars[0][0]][stars[0][1]+1] = '*'
                board[stars[1][0]][stars[1][1]+1] = '*'
            else:
                board[stars[0][0]][stars[0][1]-1] = '*'
                board[stars[1][0]][stars[1][1]-1] = '*'
        else:
            board[stars[0][0]][stars[1][1]] = '*'
            board[stars[1][0]][stars[0][1]] = '*'

        for y in range(n):
            for x in range(n):
                if x != n - 1:
                    print(board[y][x], end='')
                else:
                    print(board[y][x])

main()