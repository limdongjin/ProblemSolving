import sys
input = sys.stdin.readline

def solve(i, s):
    # i 로 시작하는 부분수열중 합이 s 인 개수 
    # global nums, cache, N

    if (i, s) in cache:
        return cache[(i, s)]

    cnt = 0
    new_s = s-nums[i]
    if new_s == 0:
        cnt += 1
    
    for j in range(i+1, N):
        cnt += solve(j, new_s)
    cache[(i, s)] = cnt

    return cnt

N, S = map(int, input().split())
nums = [int(_) for _ in input().split()]
cache = {}
ret = 0
for i in range(N):
    ret += solve(i, S)
print(ret)
