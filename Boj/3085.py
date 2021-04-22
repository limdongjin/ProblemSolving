

def main():
    n = int(input())
    board = [[' ']*n for i in range(n)]
    for i in range(n):
        s = input().rstrip()
        for j in range(n):
            board[i][j] = s[j]

    print(solve(board))


def solve(board):
    n = len(board)
    ans = -1
    for y in range(n):
        for x in range(n):
            # 오른쪽과 swap
            if x < n-1:
                swap(board, (y, x), (y, x+1))
                ans = max(ans, check(board, (y, x), (y, x+1)))
                swap(board, (y, x), (y, x+1))
            # 아래와 swap
            if y < n - 1:
                swap(board, (y, x), (y+1, x))
                ans = max(ans, check(board, (y, x), (y+1, x)))
                swap(board, (y, x), (y+1, x))
    return ans
def check(board, start, end):
    start_row, start_col = start
    end_row, end_col = end
    n = len(board)
    ans = -1

    # 행 검사
    for row in range(start_row, end_row+1):
        cnt = 1
        for x in range(0, n-1):
            if board[row][x] == board[row][x+1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)

    # 열 검사
    for col in range(start_col, end_col+1):
        cnt = 1
        for y in range(0, n-1):
            if board[y][col] == board[y+1][col]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)

    return ans

def swap(board, pos1, pos2):
    y, x = pos1
    y1, x1 = pos2
    board[y][x], board[y1][x1] = board[y1][x1], board[y][x]

main()