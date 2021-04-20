import sys


def main():
    tc = int(input())
    for _ in range(tc):
        solve()


def solve():
    n, c = [int(_) for _ in input().split()]
    a = [int(_) for _ in input().split()]
    b = [int(_) for _ in input().split()] + [0]

    cur_amount = 0
    cur = 0
    ans = sys.maxsize
    for i in range(0, n):
        # (c - cur_amount + a[i] -1)//a[i] : i 포지션에서 계속 있었을때 컴퓨터를 살수있게되는 일수
        ans = min(ans, cur + max(0, (c - cur_amount + a[i] - 1)) // a[i])

        # 다음 포지션까지 가기위해 필요한 시간
        new_days = max(0, b[i] - cur_amount + a[i] - 1) // a[i]

        cur += new_days + 1

        #             다음포지션으로 가기전까지 버는 돈 - 다음포지션까지 가기위해 필요한 돈
        cur_amount += a[i] * new_days - b[i]

    print(ans)


main()
