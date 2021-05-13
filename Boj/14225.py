import sys
input=sys.stdin.readline
def solve(idx, s):
    check[s] = True
    
    if idx == N:
        return
     
    solve(idx+1, s+A[idx])
    solve(idx+1, s)

N = int(input())
A = [int(_) for _ in input().split()]
check = {}

solve(idx=0, s=0)
for i in range(1, 100000*20 + 1):
    if i not in check:
        print(i)
        break

