import sys
sys.setrecursionlimit(10000000)

def main():
    n, m = [int(_) for _ in input().split()]
    ans = [' ' for _ in range(m)]
    visited = [False for _ in range(n+1)]

    go(0, n, m, ans, visited)


def go(idx, n, m, ans, visited):
    if idx == m:
        print(' '.join(ans))
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        ans[idx] = str(i)
        visited[i] = True
        go(idx+1, n, m, ans, visited)
        visited[i] = False


main()