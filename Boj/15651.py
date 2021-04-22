import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def main():
    n, m = [int(_) for _ in input().split()]
    # visited = [False for _ in range(n+1)]
    ans = [0 for _ in range(m)]
    go(0, n, m, ans)
    # go(0, n, m, visited, ans)

# def go(idx, n, m, visited, ans):
def go(idx, n, m, ans):
    if idx == m:
        print(' '.join([str(_) for _ in ans]))
        return
    # start = 1 if idx == 0 else ans[idx - 1]
    for i in range(1, n+1):
        # if visited[i]:
        #     continue
        # visited[i] = True
        ans[idx] = i
        go(idx+1, n, m, ans)
        # visited[i] = False
main()