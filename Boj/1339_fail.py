import sys
input=sys.stdin.readline

def next_permutation(a):
    n = len(a)
    i = n - 1
    while i > 0 and not(a[i-1] < a[i]):
        i -= 1
    if i == 0:
        return False

    j = n - 1
    while j > 0 and not(a[i-1] < a[j]):
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    k = n -1
    while i < k:
        a[i], a[k] = a[k], a[i]
        i += 1
        k -= 1

    return True

def calc(alpha, words):
    ret = 0
    mapper = {chr(alpha[i]+ord('A')): 9-i for i in range(len(alpha))}
    print(locals())
    for word in words:
        ret += transform(word, mapper)
    return ret

def transform(word, mapper):
    ret = 0
    m = 1
    for i in range(len(word)-1, -1, -1):
        ret += mapper[word[i]]*m
        m *= 10
    return ret

N = int(input())
words = []
alpha = []

for _ in range(N):
    word = input().rstrip()
    words.append(word)

    for ch in word:
        k = ord(ch) - ord('A')
        if k not in alpha:
            alpha.append(k)

alpha.sort()
ret = calc(alpha, words)

while next_permutation(alpha):
    ret = max(ret, calc(alpha, words))

print(ret)
