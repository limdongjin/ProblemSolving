import sys
input = sys.stdin.readline

def incr(n):
    for i in range(1, len(n)):
        if int(n[i-1]) > int(n[i]):
            return False
    return True

# dp[85][15] 
# dp[자리수][시작하는숫자] : 가능한 개수 
dp = [[1]*11 for _ in range(83)]

for i in range(2, 83):
    for v in range(0, 10):
        dp[i][v] = sum(dp[i-1][k] for k in range(v, 10))

for _ in range(int(input())):
    n = input().rstrip()
    ln = len(n)
    if not incr(n):
        print(-1)
        continue
     
    ans = dp[ln+1][0]
    for i in range(ln):
        ans -= sum(dp[ln-i][j] for j in range(int(n[i])+1, 10))
    print(ans-1)
