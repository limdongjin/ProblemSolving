def solution(n, k, coins):
    cnt = 0
    cur_amount = k
    coin_idx = n - 1

    while cur_amount != 0 and coin_idx >= 0:
        if coins[coin_idx] > cur_amount:
            coin_idx = coin_idx - 1
            continue
        x, cur_amount = divmod(cur_amount, coins[coin_idx])
        cnt += x

    return cnt


n, k = (int(x) for x in input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

print(solution(n=n, k=k, coins=coins))
