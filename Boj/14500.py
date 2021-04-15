from collections import namedtuple
import sys
input = sys.stdin.readline

# pypy3


class Result:
    def __init__(self):
        self.val = -1


directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
Position = namedtuple('Position', 'y x')


def main():
    n, m = [int(_) for _ in input().split()]
    board = [[0] * m for _ in range(n)]
    for y in range(len(board)):
        s = [int(_) for _ in input().split()]
        for x in range(len(board[0])):
            board[y][x] = s[x]
    print(solve(board))


def solve(board):
    result = Result()
    visited = [[0]*(len(board[0])) for _ in range(len(board))]

    for y in range(len(board)):
        for x in range(len(board[0])):
            cur_pos = Position(y=y, x=x)
            visited[y][x] = 1
            dfs(board=board, pos=cur_pos, cnt=1, cur_sum=board[y][x], visited=visited, result=result)
            visited[y][x] = 0

            except_tetromino(board=board, pos=cur_pos, result=result)
    return result.val


def dfs(board, pos, cnt, cur_sum, visited, result):
    if cnt == 4:
        if cur_sum > result.val:
            result.val = cur_sum
        return

    for dy, dx in directions:
        ny, nx = pos.y + dy, pos.x + dx
        if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]):
            continue
        if visited[ny][nx]:
            continue
        visited[ny][nx] = 1
        dfs(board=board,
            pos=Position(y=ny, x=nx),
            cnt=cnt+1,
            cur_sum=cur_sum + board[ny][nx],
            visited=visited,
            result=result)
        visited[ny][nx] = 0


def get_cell(board, pos):
    return board[pos.y][pos.x]


def except_tetromino(board, pos, result):
    pos2 = Position(pos.y, pos.x+1)
    pos3 = Position(pos.y, pos.x+2)
    pos4 = Position(pos.y-1, pos.x+1)

    pos5 = Position(pos.y+1, pos.x)
    pos6 = Position(pos.y+2, pos.x)
    pos7 = Position(pos.y+1, pos.x+1)

    pos8 = Position(pos.y+1, pos.x-1)

    def get_sum(a, b, c, d):
        sum = get_cell(board, a) + get_cell(board, b) + get_cell(board, c) + get_cell(board, d)
        return sum
    summ = 0
    # ㅗ
    if 0 <= pos.y - 1 and pos.x + 2 < len(board[0]):
        sum1 = get_sum(pos, pos2, pos3, pos4)
        summ = max(sum1, summ)

    # ㅏ
    if pos.y + 2 < len(board) and pos.x + 1 < len(board[0]):
        sum1 = get_sum(pos, pos5, pos6, pos7)
        summ = max(sum1, summ)
    # ㅓ
    if pos.y +2 < len(board) and pos.x - 1 >= 0:
        sum1 = get_sum(pos, pos5, pos6, pos8)
        summ = max(sum1, summ)
    # ㅜ
    if pos.y + 1 < len(board) and pos.x + 2 < len(board[0]):
        sum1 = get_sum(pos, pos2, pos3, pos7)
        summ = max(sum1, summ)

    if summ > result.val:
        result.val = summ


main()

# test code
# def test_solve(board, expected):
#     actual = solve(board)
#     print('expected=', expected, ' actual=', actual)
#     assert expected == actual
#
# test_solve([[0, 0, 0, 0],
#             [0, 0, 0, 0],
#             [0, 0, 0, 0],
#             [1, 2, 3, 4]], 10)
# test_solve(
#     [[0, 0, 0, 1],
#     [0, 0, 0, 2],
#     [0, 0, 0, 3],
#     [0, 0, 0,4]], 10)
# test_solve(
#     [[0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 1, 2],
#     [0, 0, 3, 4]], 10)
# test_solve([[0, 0, 0, 0],
#             [0, 0, 1, 0],
#             [0, 0, 2, 0],
#             [0, 0, 3, 4]], 10)
# test_solve([
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 1 ,2, 3],
#     [0, 4, 0 ,0]], 10)
# test_solve([[1, 2, 3, 4, 5],
#             [5, 4, 3, 2, 1],
#             [2, 3, 4, 5, 6],
#             [6, 5, 4, 3, 2],
#             [1, 2, 1, 2, 1]], 19)
# test_solve([[1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5]], 20)
# test_solve([[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
#             [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
#             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
#             [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]], 7)
