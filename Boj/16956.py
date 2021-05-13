import sys

R, C = map(int, input().split())
board = [ list(input()) for i in range(R)]

flag = False
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
for y in range(R):
    for x in range(C):
        if board[y][x] == 'W':
            for w in range(4):
                ny, nx = y+dy[w], x+dx[w]
                if ny < 0 or nx < 0 or ny >= R or nx >= C:
                    continue
                if board[ny][nx] == 'S':
                    flag = True

if flag:
    print(0)
    sys.exit(0)

for y in range(R):
    for x in range(C):
        if board[y][x] not in 'SW':
            board[y][x] = 'D'
print(1)
for row in board:
    print(''.join(row))
