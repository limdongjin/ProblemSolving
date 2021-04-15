import sys
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())
    board = [[' ']*n for i in range(n)]
    for r in range(n):
        s = input()
        for c in range(n):
            board[r][c] = s[c]

    # board2 = [[' ']*n for i in range(n)]
    # for r in range(n):
    #     for c in range(n):
    #         if board[r][c] == 'R':
    #             board2[r][c] = 'G'
    #         else:
    #             board2[r][c] = board[r][c]


    visited = [[False]*n for _ in range(n)]
    ret = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                ret = ret + 1
                bfs(board, visited, (r, c), board[r][c], False)
    area_cnt1 = ret

    visited = [[False]*n for _ in range(n)]
    ret = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                # print(r, c)
                ret = ret + 1
                bfs(board, visited, (r, c), board[r][c], True)
    # print(bfs(board2))
    print(area_cnt1, ret)


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(board, visited, pos, color, option):
    queue = deque()
    queue.append(pos)
    visited[pos[0]][pos[1]] = True

    n = len(board)
    while queue:
        r, c = queue.popleft()
        for dy, dx in directions:
            nr = r + dy
            nc = c + dx
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] != color:
                if not option:
                    continue
                elif color == 'R' and board[nr][nc] == 'G':
                    queue.append((nr, nc))
                    visited[nr][nc] = True
                    continue
                elif color == 'G' and board[nr][nc] == 'R':
                    queue.append((nr, nc))
                    visited[nr][nc] = True
                    continue
                else:
                    continue
            queue.append((nr, nc))
            visited[nr][nc] = True


main()