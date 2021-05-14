import sys
input=sys.stdin.readline
N, K = map(int, input().split())
M = [list(input().rstrip()) for _ in range(N)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
def new_array(N):
    return [[0]*10 for _ in range(N)]

def dfs(y, x):
    ck[y][x] = True
    ret = 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= 10:
            continue
        if ck[ny][nx] or M[y][x] != M[ny][nx]:
            continue
        ret += dfs(ny, nx)
    return ret

def dfs2(y, x, val):
    ck2[y][x] = True
    M[y][x] = '0'
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= 10:
            continue
        if ck2[ny][nx] or val != M[ny][nx]:
            continue
        dfs2(ny, nx, val)

def down():
    for x in range(10):
        tmp = []
        for y in range(N):
            if M[y][x] != '0':
                tmp.append(M[y][x])
        for y in range(N-len(tmp)):
            M[y][x] = '0'
        for y in range(N-len(tmp), N):
            M[y][x] = tmp[y-(N-len(tmp))]


while True:
    exist = False
    
    # 그룹화 방문 여부
    ck = new_array(N)

    # 지우는 작업 방문 여부
    ck2 = new_array(N)
   
    for y in range(N):
        for x in range(10):
            if M[y][x] == '0' or ck[y][x]:
                continue
            res = dfs(y, x)
            if res >= K:
                dfs2(y, x, M[y][x])
                exist = True
    if not exist:
        break
    down()

for row in M:
   print(''.join(row))
