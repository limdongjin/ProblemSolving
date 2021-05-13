
N, L, K = map(int, input().split())

easy, hard = 0, 0
for _ in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

ans = min(hard, K)*140 + (hard < K)*min(K-hard, easy)*100

print(ans)
    
