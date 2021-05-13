import collections

N = int(input())
words = []
alpha = [0]*26

for _ in range(N):
    word = input().rstrip()
    
    m = 10**(len(word)-1)
    for ch in word:
        alpha[ord(ch)-ord('A')] += m
        m //= 10

alpha.sort(reverse=True)
ret = 0

print(sum(alpha[i]*(9-i) for i in range(10)))
