from collections import deque


board = []
def main():
    n = int(input())
    global board
    board = [[0]*n for i in range(n)]
    shark = None
    for y in range(n):
        s = input().split()
        for x in range(n):
            board[y][x] = int(s[x])
            if board[y][x] == 9:
                shark = (y, x)
                board[y][x] = 0

    sec = 0
    size = 2
    fish_cnt = 0
    while True:
        # print_board(shark)
        new_shark, time = bfs(shark, size)
        if new_shark[0] is None:
            print(sec)
            break

        fish_cnt += 1
        if fish_cnt == size:
            size += 1
            fish_cnt = 0
        # print(new_shark)
        board[new_shark[0]][new_shark[1]] = 0
        sec += time
        shark = new_shark


def print_board(pos):
    for y in range(len(board)):
        print(y, end='   ')
        for x in range(len(board)):
            if y == pos[0] and x == pos[1]:
                print('#', end='')
            else:
                print(board[y][x], end='')
        print()


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(pos, size):
    global board
    queue = deque()
    queue.append((pos, 0))
    visited = [[False]*len(board) for i in range(len(board))]
    visited[pos[0]][pos[1]] = True

    prev_y, prev_x = None, None
    prev_time = None
    while queue:
        yx, time = queue.popleft()
        y,x = yx
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or nx >= len(board) or ny >= len(board):
                continue
            if visited[ny][nx]:
                continue
            if board[ny][nx] > size:
                continue
            if board[ny][nx] == size or board[ny][nx] == 0:
                queue.append(((ny, nx), time+1))
                visited[ny][nx] = True
                continue

            # 처음 잡는 놈은 일단 잡는다.
            if prev_time is None:
                queue.append(((ny, nx), time+1))
                visited[ny][nx] = True
                prev_y, prev_x, prev_time = ny, nx, time + 1
                continue

            # 가장 가까운놈 처리
            if prev_time > time + 1:
                queue.append(((ny, nx), time+1))
                visited[ny][nx] = True
                prev_y, prev_x, prev_time = ny, nx, time +1
            # 가장 위에놈 처리
            elif prev_time == time + 1 and prev_y > ny:
                queue.append(((ny, nx), time+1))
                visited[ny][nx] = True
                prev_y, prev_x, prev_time = ny, nx, time +1
                continue
            # 가장 왼쪽놈 처리
            elif prev_time == time + 1 and prev_y == ny and prev_x > nx:
                queue.append(((ny, nx), time+1))
                visited[ny][nx] = True
                prev_y, prev_x, prev_time = ny, nx, time +1
                continue

    return (prev_y, prev_x), prev_time

main()