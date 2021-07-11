import sys
from typing import List
input = sys.stdin.readline

def find(x):
    if parents[x] < 0:
        return x
    p = find(parents[x])
    parents[x] = p
    return p


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    high, low = (x, y) if parents[x] < parents[y] else (y, x)
    parents[high] += parents[low]
    parents[low] = high


def is_know_party(people):
    for person in people:
        for know_person in know:
            if find(person) == find(know_person):
                return True

    return False


N, M = map(int, input().split())
know = []
parents = [-1 for i in range(N+1)]

line2 = list(map(int, input().split()))
K = line2[0]
for i in range(1, K + 1):
    know.append(line2[i])

party_people: List[List] = [[int(person) for person in input().split()][1:]
                             for party in range(M)]

for people in party_people:
    first = people[0]
    for i in range(1, len(people)):
        union(first, people[i])

ans = sum(1 for people in party_people if not is_know_party(people))
print(ans)
