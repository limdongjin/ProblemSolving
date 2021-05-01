import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(go(count=0, cur_sum=0, n=n))


def go(count, cur_sum, n):
    if cur_sum == n:
        return 1
    elif cur_sum > n:
        return 0

    ret = 0
    ret += go(count+1, cur_sum + 1, n)
    ret += go(count+1, cur_sum + 2, n)
    ret += go(count+1, cur_sum + 3, n)

    return ret


main()
