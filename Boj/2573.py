from collections import deque

board = []
ices = set()
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    global board
    global ices

    n, m = [int(_) for _ in input().split()]
    board = [[0] * m for i in range(n)]

    for y in range(n):
        s = input().split()
        for x in range(m):
            board[y][x] = int(s[x])
            if board[y][x] != 0:
                ices.add((y, x))

    time = 0
    while True:
        # print('time ', time)
        group_cnt = get_group_cnt()
        if group_cnt == 0:
            print(0)
            break
        if group_cnt >= 2:
            print(time)
            break
        # print(group_cnt)
        # break
        simulate()
        time += 1


def simulate():
    # print(ices)
    remove_list = []
    for y, x in ices:
        blank = get_adj_blanks((y, x))
        # print('y=', y, 'x=',x, 'bl=', blank)
        # board[y][x] -= blank
        remove_list.append((y, x, blank))
    for y, x, val in remove_list:
        board[y][x] -= val
        if board[y][x] <= 0:
            ices.remove((y, x))

def get_group_cnt():
    cnt = 0
    for ice in ices:
        # print_board()
        cnt = bfs(ice)
        break
    if cnt == 0:
        return 0
    if cnt != len(ices):
        return 2
    return 1

def print_board():
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

def bfs(pos):
    # print('pos=',pos)
    queue = deque()
    queue.append(pos)
    # visited = [[False] * len(board[0]) for i in range(len(board))]
    visited = {pos}
    # visited[pos[0]][pos[1]] = True
    cnt = 1
    while queue:
        y, x = queue.popleft()
        # print(y, x)
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[1]):
                continue
            if board[ny][nx] > 0 and (ny, nx) not in visited:
                queue.append((ny, nx))
                # visited[ny][nx] = True
                visited.add((ny, nx))
                cnt += 1
    return cnt


def get_adj_blanks(pos):
    y, x = pos
    cnt = 0
    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx
        if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[1]):
            continue
        if board[ny][nx] <= 0:
            cnt += 1
    return cnt


main()