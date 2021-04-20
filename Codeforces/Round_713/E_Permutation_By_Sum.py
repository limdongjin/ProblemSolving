def main():
    tc = int(input())
    for _ in range(tc):
        n, l, r, s = [int(_) for _ in input().split()]
        l -= 1
        r -= 1

        solve(n, l, r, s)


def solve(n, l, r, s):
    # element num of between L .... R
    len_lr = r - l + 1

    for first in range(1, n - len_lr + 2):
        # first = 1, 2, 3, ... , n - len_lr, n - len_lr + 1
        # ex, r = 3, l = 2, n = 5: first = 1, 2, 3, 4

        # minimum sum. sum([first, first+1, .. ])
        min_sum = sum(range(first, first + r - l + 1))
        diff = s - min_sum

        if 0 <= diff <= len_lr:
            start = r - diff + 1
            ans = [0] * n
            non_blocked = set(range(1, n + 1))
            for i in range(l, r + 1):
                ans[i] = first + (i - l)
                if i >= start:
                    ans[i] += 1
                if ans[i] in non_blocked:
                    non_blocked.remove(ans[i])

            if ans[r] > n:
                continue
            if ans[r] in non_blocked:
                non_blocked.remove(ans[r])

            for i in range(0, l):
                ans[i] = non_blocked.pop()
            for i in range(r + 1, n):
                ans[i] = non_blocked.pop()

            print(' '.join([str(_) for _ in ans]))
            return
    print(-1)


main()
