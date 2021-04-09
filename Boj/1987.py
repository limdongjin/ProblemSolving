import sys
input = sys.stdin.readline
board = []
def main():
    r, c = [int(_) for _ in input().split()]
    global board
    board = [[' ']*c for y in range(r)]
    for y in range(r):
        s = input()
        for x in range(c):
            board[y][x] = s[x]
    print(solve((0, 0)))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def solve(pos):
    alp = board[pos[0]][pos[1]]

    queue = {(pos[0], pos[1], alp)}
    max_cnt = 1
    while queue:
        y, x, alpp = queue.pop()
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]):
                continue
            if board[ny][nx] in alpp:
                continue

            queue.add((ny, nx, alpp + board[ny][nx]))
            max_cnt = max(max_cnt, len(alpp) + 1)

    return max_cnt

main()