import sys
input = sys.stdin.readline

def solve(w, s):
    if len(w) == 2:
        global ret
        ret = max(ret, s)
        return
    for i in range(1, len(w)-1):
        solve(w[:i]+w[i+1:] ,s+w[i-1]*w[i+1])
    
N = int(input())
W = [int(_) for _ in input().split()]
ret = -sys.maxsize

solve(w=W, s=0)
print(ret)
