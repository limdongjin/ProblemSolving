from collections import deque
visited = []
board = []
def main():
    global board
    global visited
    h, w, k = [int(_) for _ in input().split()]
    board = [[0]*(w) for i in range(h)]
    for i in range(k):
        lx, ly,rx, ry = [int(_) for _ in input().split()]
        for y in range(ly, ry):
            for x in range(lx, rx):
                board[y][x] = 1

    ret = []
    visited = [[False]*(w) for i in range(h)]
    for y in range(h):
        for x in range(w):
            if board[y][x] == 0 and not visited[y][x]:
                ret.append(bfs((y, x)))
    print(len(ret))
    ret.sort()
    for x in ret:
        print(x, end=" ")


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(pos):
    queue = deque()
    queue.append((pos[0],pos[1], 1))
    global visited
    visited[pos[0]][pos[1]] = True
    ret = 1
    c = 1
    while queue:
        y, x, cnt = queue.popleft()

        ret = max(ret, cnt)
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]):
                continue
            if board[ny][nx] == 0 and not visited[ny][nx]:
                queue.append((ny, nx, cnt + 1))
                visited[ny][nx] = True
                c += 1
    return c
main()