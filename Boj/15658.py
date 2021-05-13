import sys
input=sys.stdin.readline

def solve(idx, s, plus, minus, mul, div):
    # A[idx] op A[idx+1] 
    
    if idx == N-1:
        global max_v, min_v
        max_v = max(s, max_v)
        min_v = min(s, min_v)
        return

    if plus > 0:
        solve(idx+1, s+A[idx+1], plus-1, minus, mul, div)
    if minus > 0:
        solve(idx+1, s-A[idx+1], plus, minus-1, mul, div)    
    if mul > 0:
        solve(idx+1, s*A[idx+1], plus, minus, mul-1, div)
    if div > 0:
        res = s//A[idx+1]
        if s < 0:
            s = -s
            res = (s//A[idx+1])*(-1)
        solve(idx+1, res, plus, minus, mul, div-1)
    return
    
N = int(input())
A = [int(_) for _ in input().split()]
plus, minus, mul, div = map(int, input().split())
max_v = -sys.maxsize
min_v = sys.maxsize
solve(0, A[0], plus, minus, mul, div)
print(max_v)
print(min_v)
