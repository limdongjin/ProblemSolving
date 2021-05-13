import sys
input = sys.stdin.readline

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# L R U D

def solve(cnt):
    if cnt > 10:
        return

    global min_cnt
    if min_cnt <= cnt:
        return
    old0, old1 = coins[0], coins[1]
    
    for d in range(4):
        if min_cnt <= cnt:
            return
        coins[0] = simul(coins[0], d)
        coins[1] = simul(coins[1], d)
        if (*coins[0], *coins[1]) == (*old0, *old1):
            continue
        fall_coin = 0
        for i in range(2):
            if coins[i] == (-1, -1):
                fall_coin += 1
        if fall_coin == 1:
            min_cnt = min(cnt+1, min_cnt)
            return

        if fall_coin == 2:
            coins[0] = old0
            coins[1] = old1
            continue
        
        solve(cnt+1)
        
        coins[0] = old0
        coins[1] = old1
    
def simul(coin, d):
    y, x = coin
    ny, nx = y + directions[d][0], x + directions[d][1]
    if ny < 0 or nx < 0 or ny >= H or nx >= W:
        return (-1, -1)
    if board[ny][nx] == '#':
        return (y, x)
    return (ny, nx)
H, W = map(int, input().split())
board = [['.']*W for y in range(H)]
coins = []

for y in range(H):
    s = input().rstrip()
    for x in range(W):
        board[y][x] = s[x]
        if s[x] == 'o':
            board[y][x] = '.'
            coins.append((y,x))

min_cnt = sys.maxsize
solve(cnt=0)
if min_cnt <= 10:
    print(min_cnt)
else:
    print(-1)
