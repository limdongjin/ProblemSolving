from collections import deque
import sys
sys.setrecursionlimit(20000000)
input = sys.stdin.readline

max_ret = -1


def bfs(board, position):
    queue = deque()
    queue.append(position)
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    while queue:
        r, c = queue.popleft()
        for direction in range(4):
            nr = r + dy[direction]
            nc = c + dx[direction]
            if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]):
                continue
            if board[nr][nc] != 0:
                continue
            queue.append((nr, nc))
            board[nr][nc] = 2


def bug_on(board):
    global bugs

    for bug_position in bugs:
        bfs(board, (bug_position[0], bug_position[1]))


def construct_wall(board, position, cnt):
    r, c = position
    board[r][c] = 1
    global max_ret

    if cnt == 3:
        tmp_board = []
        for row in board:
            tmp_board.append([])
            for cell in row:
                tmp_board[-1].append(cell)

        bug_on(tmp_board)

        ret = 0
        for row in tmp_board:
            for col in row:
                if col == 0:
                    ret = ret + 1
        max_ret = max(ret, max_ret)
    else:
        for next_c in range(c+1, len(board[0])):
            if board[r][next_c] == 0:
                construct_wall(board, (r, next_c), cnt+1)
        for next_r in range(r+1, len(board)):
            for next_c in range(len(board[0])):
                if board[next_r][next_c] == 0:
                    construct_wall(board, (next_r, next_c), cnt+1)

    board[r][c] = 0


height, width = [int(_) for _ in input().split()]
board = []
bugs = []
for r in range(height):
    board.append([])
    for c in input().split():
        num = int(c)
        board[r].append(num)
        if num == 2:
            bugs.append((r, len(board[r])-1))

for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == 0:
            construct_wall(board, (r, c), 1)

print(max_ret)