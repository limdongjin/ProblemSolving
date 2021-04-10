from collections import deque

board = []


def main():
    n = int(input())
    global board
    board = [[0] * n for _ in range(n)]

    pos = None
    for y in range(n):
        s = input().split()
        for x in range(n):
            board[y][x] = int(s[x])
            if board[y][x] == 9:
                pos = (y, x)
                board[y][x] = 0

    sec = 0
    fish_cnt = 0
    size = 2
    while True:
        # print('bfs sec=', sec, 'size=', size, 'pos=', pos)
        ret = bfs(pos, size)
        if not ret:
            print(sec)
            break

        # 잡은 물고기, 걸린 시간
        pos, diffsec = ret

        # 잡은 물고기 개수를 1 증가
        fish_cnt += 1

        if size == fish_cnt:
            size += 1 # 사이즈업
            fish_cnt = 0

        # 잡은 물고기의 위치는 빈칸으로 설정
        board[pos[0]][pos[1]] = 0

        # 시간을 증가시킨다.
        sec += diffsec

        # for r in range(len(board)):
        #     print(r, '  ', end='')
        #     for c in range(len(board[0])):
        #         if r == pos[0] and c == pos[1]:
        #             print('@', end='')
        #         else:
        #             print(board[r][c], end='')
        #     print()


# 방향 기반 우선순위 탐색은 제대로 작동하지않는다.
# 그래서 잡을수있는 물고기 다 찾고, 로직으로 우선순위를 검증해야한다.
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def bfs(pos, size):
    queue = deque()
    queue.append((pos[0], pos[1], 0))  # pos, sec
    visited = [[False] * len(board[0]) for i in range(len(board))]
    ret = None
    while queue:
        y, x, sec = queue.popleft()
        # print('y=',y,'x=',x,'sec=',sec)
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            # print('ny=',ny,'nx=',nx,'sec=',sec, 'direc=',(dy,dx))

            # 범위 초과
            if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]):
                continue
            # 큰 물고기
            if board[ny][nx] > size:
                continue
            # 이미 방문
            if visited[ny][nx]:
                continue
            # 사이즈가 같은 물고기 또는 빈칸
            if board[ny][nx] == size or board[ny][nx] == 0:
                queue.append((ny, nx, sec + 1))
                visited[ny][nx] = True
                continue
            # print('catch? ', (ny, nx, sec + 1))

            # 첫 물고기
            if ret is None:
                # print('[c0]old=', ret, 'new=', (ny,nx,sec+1))
                ret = ((ny, nx), sec + 1)
                visited[ny][nx] = True
            # 이전 물고기보다 시간이 적게 걸리므로, 이 물고기를 잡는다.
            elif ret[1] > sec + 1:
                # print('[c00]old=', ret, 'new=', (ny,nx,sec+1))
                ret = ((ny, nx), sec + 1)
                visited[ny][nx] = True
            # 이전 물고기와 시간이 같은 경우
            elif ret[1] == sec + 1:
                # 기존 물고기보다 위에 있기에 잡는다.
                # y 축은 값이 작을수록 위에 있다
                if ret[0][0] > ny:
                    # print('[c2]old=', ret, 'new=', (ny,nx,sec+1))
                    ret = ((ny, nx), sec + 1)
                    visited[ny][nx] = True
                # y 좌표는 같은 상황에서, 기존 물고기보다 왼쪽이므로 잡는다.
                elif ret[0][0] == ny and ret[0][1] > nx:
                    # print('[c3]old=', ret, 'new=', (ny,nx,sec+1))
                    ret = ((ny, nx), sec + 1)
                    visited[ny][nx] = True
    # print('finally catch! ', ret)
    return ret


main()
