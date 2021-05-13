import sys
from itertools import combinations
input = sys.stdin.readline

def calc(a, b, c):
    # param a : (y, x)
    #       b : (y, x)
    #       c : (y, x)

    ret = 0
    flow = set()

    for flower in [a,b,c]:
        flow.add(flower)
        y, x = flower

        ret += board[y][x]
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            flow.add((ny, nx))
            ret += board[ny][nx]

    if len(flow) != 15:
        return MAX_V
    return ret

dy, dx = [0,0,-1,1], [1,-1,0,0]
MAX_V = 99999
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = MAX_V

get_yx = lambda k: (k//N, k%N)
is_bound = lambda yx: yx[0] == 0 or yx[0] == N-1 or yx[1] ==0 or yx[1] == N-1
#x_adj = lambda yx1, yx2: yx1[0] == yx2[0] and abs(yx1[1]-yx2[1])==1
#y_adj = lambda yx1, yx2: yx1[1] == yx2[1] and abs(yx1[0]-yx2[0])==1

for a,b,c in combinations(range(N*N), 3):
    if abs(a-b) == 1 or abs(b-c) == 1 or abs(a-c)==1:
        continue
    a, b, c = get_yx(a), get_yx(b), get_yx(c)
    if is_bound(a) or is_bound(b) or is_bound(c):
        continue
    #if x_adj(a,b) or x_adj(b,c) or x_adj(a,c):
    #    continue
    #if y_adj(a,b) or y_adj(b,c) or y_adj(a,c):
    #    continue
    
    ans = min(ans, calc(a, b, c))

print(ans)
