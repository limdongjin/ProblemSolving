import sys
input=sys.stdin.readline
def solve(a, cnt, start, cur_sum):
    if cur_sum > M:
        return
    if cnt == 3:
        global ans
        ans = max(ans, cur_sum)
        return

    for i in range(start, N):
        solve(a, cnt+1, i+1, cur_sum+a[i])

N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = -1
solve(a=A, cnt=0, start=0, cur_sum=0)

print(ans)
