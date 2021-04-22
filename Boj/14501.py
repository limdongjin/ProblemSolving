import sys
input = sys.stdin.readline

ans = 0
def main():
    n = int(input())
    t_p = []
    for i in range(n):
        y, x = map(int, input().split())
        t_p.append((y, x))

    go(n, day=0, p=0, t_p=t_p)
    print(ans)


def go(n, day, p, t_p):
    if day == n:
        global ans
        ans = max(ans, p)
        return
    if day > n:
        return

    go(n, day+1, p, t_p)
    go(n, day+t_p[day][0], p+t_p[day][1], t_p)


main()