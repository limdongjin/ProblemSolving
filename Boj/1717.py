import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000001)


def find(parent, target):
    if target == parent[target]:
        return target
    parent[target] = find(parent, parent[target])
    return parent[target]


def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a == b:
        return
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b


def main():
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0:
            union(parent, a, b)
        else:
            if find(parent, a) == find(parent, b):
                print('YES')
            else:
                print('NO')

    return


main()