import sys
sys.setrecursionlimit(100000000)
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for y in range(N)]
is_rangeout = lambda y, x: y < 0 or x < 0 or y >= N or x >= N
dirs = [(1,0),(-1,0), (0,1),(0,-1)]

def is_moveable(from_yx, to_yx):
    fy, fx = from_yx
    ty, tx = to_yx
    return L<= abs(board[fy][fx]-board[ty][tx])<=R

def move_people():
    visited = [[False]*N for _ in range(N)]

    def get_area_sum(y, x, settable):
        visited[y][x] = True
        settable.append((y,x))
        ret = board[y][x] # sum

        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if is_rangeout(ny, nx) or visited[ny][nx]:
                continue
            if not is_moveable((y, x), (ny, nx)):
                continue
            ret += get_area_sum(ny, nx, settable)
        return ret
    
    def set_area(v, settable):
        for y, x in settable:
            board[y][x] = v
    
    flag = False
    for y in range(N):
        for x in range(N):
            if visited[y][x]:
                continue
            settable = []
            area_sum = get_area_sum(y, x, settable)
            if len(settable) <= 1:
                continue
            
            set_area(area_sum//len(settable), settable)
            flag = True

    return flag

for cnt in range(1, 2001):
    if not move_people():
        print(cnt-1)
        break

