

S = input().rstrip()
ans = 0
for i in range(1, len(S)):
    if S[i-1] != S[i]:
        ans += 1

print(ans//2 + ans%2)
