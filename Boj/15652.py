

def main():
    n, m = map(int, input().split())
    ans = [0 for i in range(n+1)]
    go(1, 0, ans, n, m)


def go(idx, selected, ans, n, m):
    if selected == m:
        for i in range(1, n+1):
            for j in range(1, ans[i]+1):
                print(i, end=' ')
        print()
        return

    if idx > n:
        return
    for i in range(m-selected, 0, -1):
        ans[idx] = i
        go(idx+1, selected+i, ans, n, m)
    ans[idx] = 0
    go(idx+1, selected, ans, n, m)


main()