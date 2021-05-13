

MAX_V = 99999
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [0,0,1,-1], [1,-1,0,0]

def calc(a, b, c):
    ret = 0
    flow = []
    for flower in [a, b, c]:
        y = flower // N
        x = flower % N
        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return MAX_V
        
        ret += board[y][x]
        flow.append((y,x))
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            flow.append((ny, nx))
            ret += board[ny][nx]
    
    if len(set(flow)) != 15:
        return MAX_V

    return ret

ans = MAX_V
for f in range(N*N):     # (y, x) = y*N + x
    for s in range(N*N):
        for t in range(N*N):
            ans = min(ans, calc(f, s, t))

print(ans)
