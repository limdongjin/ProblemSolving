from sys import stdin

input = stdin.readline


def check(cur_row, candidate_col):
    for r in range(cur_row):
        if candidate_col == board[r] or (cur_row - r) == abs(candidate_col - board[r]):
            return False
    return True


def solve(cur_row):
    if cur_row == N:
        return 1

    ret = 0
    for candidate_col in range(N):
        if check(cur_row, candidate_col):
            board[cur_row] = candidate_col
            ret += solve(cur_row + 1)

    return ret


N = int(input())
board = [-1] * N

ans = solve(0)

print(ans)

