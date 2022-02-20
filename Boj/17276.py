from sys import stdin
input = stdin.readline

def print_x(x):
    for y in range(len(x)):
        print(" ".join(map(str, x[y])))


def rotate_45(board):
    n = len(board)
    new_board = [board[y][:] for y in range(n)]

    for i in range(n):
        # 가열 <- 주대
        new_board[i][n//2] = board[i][i]
        # 부대 <- 가열
        new_board[i][n-1-i] = board[i][n//2]
        # 가행 <- 부대
        new_board[n//2][i] = board[n-1-i][i]
        # 주대 <- 가행
        new_board[i][i] = board[n//2][i]

    return new_board

def rotate_minus45(board):
    n = len(board)
    new_board = [board[y][:] for y in range(n)]

    for i in range(n):
        # 가행 <- 주대
        new_board[n//2][i] = board[i][i]
        # 주대 <- 가열
        new_board[i][i] = board[i][n//2]
        # 가열 <- 부대
        new_board[i][n//2] = board[i][n-1-i]
        # 부대 <- 가행
        new_board[n-1-i][i] = board[n//2][i]
    return new_board


def main():
    T = int(input())
    for t in range(T):
        n, d = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        if abs(d) == 360:
            d = 0
        if d > 0:
            for _ in range(d // 45):
                board = rotate_45(board=board)
        elif d < 0:
            for _ in range(((-1)*d) // 45):
                board = rotate_minus45(board=board)
        print_x(board)
main()