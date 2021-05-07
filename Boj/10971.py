import sys
input = sys.stdin.readline

def main():
    n = int(input())
    costs = [[0]*n for _ in range(n)]
    for i in range(n):
        s = list(map(int, input().split()))
        for j in range(n):
            costs[i][j] = s[j]

    path = list(range(0, n))
    ans = calc_cost(path, costs)

    while next_perm(path):
        if path[0] != 0:
            break
        ans = min(ans, calc_cost(path, costs))
    print(ans)

def next_perm(p):
    def swap(i, j):
        p[i], p[j] = p[j], p[i]
    n = len(p)

    i = n - 1
    while i > 0 and p[i-1] >= p[i]:
        i -= 1

    if i <= 0:
        return False

    j = n - 1
    while p[i-1] >= p[j]:
        j -= 1

    swap(i-1, j)

    # reverse
    j = n - 1
    while i < j:
        swap(i, j)
        i += 1
        j -= 1
    return True

def calc_cost(path, costs):
    ret = 0
    is_possible = True
    for i in range(len(path) - 1):
        from_, to_ = path[i], path[i+1]
        if costs[from_][to_] == 0:
            is_possible = False
            break
        ret += costs[from_][to_]
    ret += costs[path[-1]][path[0]]
    if not is_possible or costs[path[-1]][path[0]] == 0:
        return sys.maxsize

    return ret



main()
