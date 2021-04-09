from collections import deque

board = []
visited = []


def main():
    h, w = [int(_) for _ in input().split()]
    global board
    board = [['.'] * w for _ in range(h)]
    red = None
    blue = None
    for r in range(h):
        s = input()
        for c in range(w):
            board[r][c] = s[c]
            if s[c] == 'R':
                red = (r, c)
            elif s[c] == 'B':
                blue = (r, c)

    print(bfs(red, blue))


def get_cell(pos):
    return board[pos[0]][pos[1]]


def visit(pos1, pos2):
    visited[pos1[0]][pos1[1]][pos2[0]][pos2[1]] = True


def move(pos, dydx):
    y, x = pos
    while True:
        cell = get_cell((y+dydx[0], x+dydx[1]))
        if cell == '#':
            return y, x
        y += dydx[0]
        x += dydx[1]
        if cell == 'O':
            return y, x


def is_same_pos(yx1, yx2):
    return yx1[0] == yx2[0] and yx1[1] == yx2[1]


def is_visited(pos1, pos2):
    return visited[pos1[0]][pos1[1]][pos2[0]][pos2[1]]


def bfs(red, blue):
    global board
    queue = deque()
    queue.append((red, blue, 0))
    h = len(board)
    w = len(board[0])

    global visited
    visited = [[[[False] * w for i in range(h)] for k in range(w)] for _ in range(h)]
    visit(red, blue)

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        red_pos, blue_pos, cnt = queue.popleft()
        if cnt >= 10:
            return -1
        for dydx in directions:
            # 공을 움직인다.
            moved_red = move(red_pos, dydx)
            moved_blue = move(blue_pos, dydx)

            if get_cell(moved_blue) != 'O':
                if get_cell(moved_red) == 'O': # 레드가 홀에 빠졌다.
                    return cnt + 1

                # 둘이 같은 위치에 있다. 이는 서로 충돌한 케이스
                if is_same_pos(moved_red, moved_blue):
                    diff_red = abs(red_pos[0] - moved_red[0]) + abs(red_pos[1] - moved_red[1])
                    diff_blue = abs(blue_pos[0] - moved_blue[0]) + abs(blue_pos[1] - moved_blue[1])
                    if diff_blue < diff_red:
                        moved_red = (moved_red[0] - dydx[0], moved_red[1] - dydx[1])
                    else:
                        moved_blue = (moved_blue[0] - dydx[0], moved_blue[1] - dydx[1])

                # 방문하지않은 셀이라면 방문처리하고 큐에 넣음
                if not is_visited(moved_red, moved_blue):
                    visit(moved_red, moved_blue)
                    queue.append((moved_red, moved_blue, cnt+1))
    return -1


main()