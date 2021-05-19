from collections import deque

def next_v(v):
    ret = v*214013 + 2531011
    ret %= a232
    return ret

def solve(k, n):
    ret = 0
    signal = 1983
    range_sum = 0
    rang = deque()
    for head in range(n):
        signal = signal%10000 + 1
        range_sum += signal
        rang.append(signal)
        
        while range_sum > k and rang:
            range_sum -= rang[0]
            rang.popleft()
        if k == range_sum:
            ret += 1
        signal = next_v(signal)

    return ret

a232 = 2**32
for _ in range(int(input())):
    K, N = map(int, input().split())

    print(solve(K, N))
