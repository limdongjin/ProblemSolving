import sys
input = sys.stdin.readline

def solve(day, coupon):
    # day일에서 쿠폰을 coupon 개 갖고 시작했을때
    # 마지막날까지의 최소 비용 
    if day > N:
        return 0
    if dp[day][coupon] != -1:
        return dp[day][coupon]
    if day in NOGO:
        return solve(day+1, coupon)

    ans = 10000+solve(day+1, coupon)
    ans = min(ans, 25000+solve(day+3, coupon+1))
    ans = min(ans, 37000+solve(day+5,coupon+2))
    
    if coupon >= 3:
        ans = min(ans, solve(day+1, coupon-3))
    
    dp[day][coupon] = ans
    return dp[day][coupon]

N, M = map(int, input().split())
NOGO = {int(day): 1 for day in input().split()}

# dp[day][coupon]
# 쿠폰을 coupon 개를 가진 상태에서 
# day 일부터 시작했을때 마지막 날까지의 최소비용.
dp = [[-1]*101 for _ in range(101)]

print(solve(1, 0))
