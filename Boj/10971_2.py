import itertools
import sys

def main():
    n = int(input())
    costs = [[0]*n for _ in range(n)]
    for y in range(n):
        s = list(map(int, input().split()))
        for i in range(n):
            costs[y][i] = s[i]

    perms = itertools.permutations(range(n))
    ret = sys.maxsize
    for perm in perms:
        if costs[perm[-1]][perm[0]] == 0:
            continue
        cost = 0
        flag = True
        for i in range(n-1):
            from_v = perm[i]
            to_v = perm[i+1]
            if costs[from_v][to_v] == 0:
                flag = False
                break
            cost += costs[from_v][to_v]
            if cost >= ret:
                flag = False
                break
        if flag == False:
            continue
        cost += costs[perm[-1]][perm[0]]
        ret = min(ret, cost)

    print(ret)

main()
