import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
print = sys.stdout.write

mo = ['a', 'e', 'i', 'o', 'u']


def main():
    L, C = map(int, input().split())
    alpha = input().rstrip().split()
    alpha.sort()

    go(idx=0, l=L, alpha=alpha, password="")


def go(idx, l, alpha, password):
    if len(password) == l:
        mo_cnt = 0

        for ch in password:
            if ch in mo:
                mo_cnt += 1

        if mo_cnt >= 1 and l - mo_cnt >= 2:
            print(password + '\n')
        return

    if idx >= len(alpha):
        return
    go(idx+1, l, alpha, password+alpha[idx])
    go(idx+1, l, alpha, password)


main()