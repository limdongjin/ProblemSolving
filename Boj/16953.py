from sys import stdin

input = stdin.readline


def solve(a, b):
    assert a != b

    ret = 0
    while a < b:
        if b % 2 == 0:
            b //= 2
            ret += 1
            continue
        elif b % 10 == 1:
            b //= 10
            ret += 1
            continue
        else:
            ret = -1
            break

    if a == b:
        return ret + 1
    else:
        return -1


def main():
    a, b = map(int, input().split())
    print(solve(a, b))


main()


def test():
    print("test start")

    assert solve(4, 21) == -1
    assert solve(4, 42) == -1
    assert solve(4, 42) == -1
    assert solve(2, 162) == 5
    assert solve(100, 40021) == 5

    print("test success")


# test()
