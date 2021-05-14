import sys
from itertools import combinations
input = sys.stdin.readline

def calc(a, b, c, cache):
    ret = sum(cache[y][x] for y, x in [a, b, c]) 
    return ret
def check(k1, k2):
    q1, r1 = divmod(k1, N)
    q2, r2 = divmod(k2, N)
    
    is_bound = lambda x: x == 0 or x == N-1
    if is_bound(q1) or is_bound(q2) or is_bound(r1) or is_bound(r2):
        return False
    if (r1 == r2 and abs(q1-q2) <= 2) or (q1 == q2 and abs(r1-r2) <= 2):
        return False
    if abs(q1-q2) == 1 and abs(r1-r2)==1:
        return False
    
    return True

dy, dx = [0,0,-1,1], [1,-1,0,0]
MAX_V = 99999
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = MAX_V
cache = [board[i][:] for i in range(N)]

for y in range(1, N-1):
    for x in range(1, N-1):
        cache[y][x] += sum(board[y+dy[k]][x+dx[k]] for k in range(4))

get_yx = lambda k: divmod(k, N)

for a,b,c in combinations(range(N, N*(N-1)), 3):
    if not check(a, b) or not check(b, c) or not check(a, c):
        continue
     
    a, b, c = get_yx(a), get_yx(b), get_yx(c)
    ans = min(ans, calc(a, b, c, cache))

print(ans)
