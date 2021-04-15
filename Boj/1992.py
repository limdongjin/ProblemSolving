

def main():
    n = int(input())
    board = [[0]*n for _ in range(n)]
    for y in range(n):
        s = input()
        for x in range(n):
            board[y][x] = int(s[x])

    print(solve(board, (0, 0),n))

def solve(board, start, n):
    y, x = start
    if n == 1:
        if board[y][x] == 0:
            return '0'
        elif board[y][x] == 1:
            return '1'
    ret = ''
    n_divide2 = n // 2
    for dy in range(2):
        for dx in range(2):
            d = solve(board, (y + n_divide2*dy, x + n_divide2*dx), n_divide2)
            ret += d
    if ret == '1111':
        return '1'
    elif ret == '0000':
        return '0'

    return '('+ret+')'
main()
