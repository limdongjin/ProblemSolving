from sys import stdin
from collections import deque
input = stdin.readline

def solve(N, K):
    people = deque(range(1, N+1))

    while len(people) > 2:
        people.popleft()
         
        # move k-1
        for _ in range((K-1)%len(people)):
            people.append(people.popleft())
    
    a, b = people[0], people[1]
    if a > b:
        a, b = b, a

    print(a, b)


for _ in range(int(input())):
    N, K = map(int, input().split())

    solve(N, K)
