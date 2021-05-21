from sys import stdin
from collections import deque
input = stdin.readline

def solve(n):
    if n <= 9:
        return n
    if n > 1022:
        return -1

    q = deque(range(1,10))
    cur_idx = cur_v = 9
    while cur_idx < n:
        val = q.popleft()

        for i in range(val%10):
            cur_idx, cur_v = cur_idx+1, val*10+i
            q.append(cur_v)
    
    for _ in range(cur_idx-n):
        q.pop()
    
    return q.pop()
    
N = int(input())
print(solve(N))
