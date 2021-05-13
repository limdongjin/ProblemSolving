import sys
input = sys.stdin.readline

def solve(idx, s):
    global ret
    if idx == N:
        return
    if s+nums[idx] == S:
        ret += 1
    
    solve(idx+1, s)
    solve(idx+1, s+nums[idx])

N, S = map(int, input().split())
nums = [int(_) for _ in input().split()]
ret = 0
solve(idx=0, s=0)

print(ret)
